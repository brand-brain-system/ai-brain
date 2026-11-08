"""frame-check.py: contact sheets and measurements for looking at a finished video before a human does.

Usage: python frame-check.py <video> [--out <folder>] [--strip 4.2 7.5 ...] [--hook-only]

Writes to <folder> (default: frame-check/ next to the video):
  contact.png       24 frames spread over the whole video, each labelled with its time
  phone-<n>.png     frames at true phone width (360 px): 0, 0.5, 1, 2 s, then every 3 s and the last frame
  strip-<t>.png     8 consecutive frames starting at t (fast moments: transitions, pops, caption swaps)
  report.md         size, length, black stretches, still stretches (>= 2.5 s), loudness, the sheet list,
                    and the blank verdict table from video-edits SKILL.md ("Frame check")
--hook-only writes only phone-1.png (the first 2 seconds), for the other hook versions of the same body.

Light on the PC: it decodes, it never encodes video, and runs ffmpeg at below-normal priority with half the
cores. Every sheet stays within ~1500 px so Claude reads it without downscaling.
Adapted from the motion-design course's "make Opus watch its own frames" (movez Substack, Oct 2026).
"""
import argparse, json, os, re, subprocess, sys, tempfile, shutil

PRIO = getattr(subprocess, 'BELOW_NORMAL_PRIORITY_CLASS', 0)
THREADS = str(max(1, (os.cpu_count() or 2) // 2))
FONT = 'C\\:/Windows/Fonts/arial.ttf' if os.name == 'nt' else '/System/Library/Fonts/Helvetica.ttc'
MAXSHEET = 1500


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', creationflags=PRIO)


def probe(path):
    r = run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,width,height,r_frame_rate:format=duration',
             '-of', 'json', path])
    d = json.loads(r.stdout)
    v = next(s for s in d['streams'] if s['codec_type'] == 'video')
    num, den = v['r_frame_rate'].split('/')
    return {'w': int(v['width']), 'h': int(v['height']), 'fps': float(num) / float(den),
            'dur': float(d['format']['duration']), 'audio': any(s['codec_type'] == 'audio' for s in d['streams'])}


def label(t):
    return (f"drawtext=fontfile='{FONT}':text='{t:.2f}s':x=6:y=6:fontsize=18:fontcolor=white"
            f":box=1:boxcolor=black@0.65:boxborderw=4")


def grab(video, t, width, out):
    """One frame at time t, scaled to width, with its time drawn on it. Falls back to no label."""
    base = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-threads', THREADS, '-ss', f'{t:.3f}', '-i', video,
            '-frames:v', '1']
    r = run(base + ['-vf', f'scale={width}:-2,{label(t)}', out])
    if r.returncode != 0 or not os.path.exists(out):
        run(base + ['-vf', f'scale={width}:-2', out])
    return os.path.exists(out)


def tile(frames, cols, out):
    """Tile a list of same-size PNGs into one sheet, cols across, padding the last row."""
    if len(frames) == 1:
        shutil.copy(frames[0], out)
        return
    rows = -(-len(frames) // cols)
    inputs, chain = [], ''
    for f in frames:
        inputs += ['-i', f]
    n = len(frames)
    pads = cols * rows - n
    if pads:  # pad with black frames of the same size so xstack has a full grid
        r = run(['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height', '-of', 'csv=p=0', frames[0]])
        fw, fh = r.stdout.strip().split(',')[:2]
        chain += f'color=c=black:s={fw}x{fh}:d=1,format=rgb24,split={pads}' + ''.join(f'[p{i}]' for i in range(pads)) + ';'
    labels = [f'[{i}]' for i in range(n)] + [f'[p{i}]' for i in range(pads)]
    layout = '|'.join(f'{"+".join(["w0"] * (i % cols)) or "0"}_{"+".join(["h0"] * (i // cols)) or "0"}'
                      for i in range(cols * rows))
    chain += ''.join(labels) + f'xstack=inputs={cols * rows}:layout={layout}:fill=black'
    r = run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y'] + inputs + ['-filter_complex', chain, '-frames:v', '1', out])
    if r.returncode != 0:
        sys.exit('tiling failed: ' + r.stderr[-400:])


def fit(n, w, h):
    """Columns and tile width so n frames of aspect w:h fit inside MAXSHEET x MAXSHEET, tiles as big as possible."""
    best = (1, 60)
    for cols in range(2, 13):
        rows = -(-n // cols)
        tw = min(MAXSHEET // cols, int(MAXSHEET / rows * w / h))
        tw -= tw % 2
        if tw > best[1]:
            best = (cols, tw)
    return best


CHANGE_SCORE = 3.5 # scdet score. Calibrated 14 Oct 2026 on two versions of one 540x960 UGC edit: B-roll
                   # cuts 15-19, punch-ins 5-7, a zoom back out 4.0, a person talking and caption swaps 1-2,
                   # a cut between two takes with the same framing 3.0 (invisible to a viewer too: don't count it)
MAX_GAP = 3.0      # the lead strategist's rule: something new on screen every 2-3 s


def gaps_without_change(changes, dur):
    """Stretches longer than MAX_GAP with no visual change. Changes closer than 0.3 s count once."""
    merged = []
    for t in sorted(changes):
        if not merged or t - merged[-1] > 0.3:
            merged.append(t)
    pts = [0.0] + merged + [dur]
    return merged, [(a, b) for a, b in zip(pts, pts[1:]) if b - a > MAX_GAP]


def measure(video, info):
    """One decode pass at low resolution: black stretches, still stretches, visual changes, loudness."""
    cmd = ['ffmpeg', '-hide_banner', '-nostats', '-threads', THREADS, '-i', video,
           '-vf', 'scale=320:-2,blackdetect=d=0.1:pix_th=0.10,freezedetect=n=-60dB:d=2.5,'
                  f'scdet=threshold={CHANGE_SCORE}:sc_pass=1,metadata=print:key=lavfi.scd.time']
    if info['audio']:
        cmd += ['-af', 'ebur128=peak=true']
    cmd += ['-f', 'null', '-']
    err = run(cmd).stderr
    black = [(float(a), float(b)) for a, b in re.findall(r'black_start:([\d.]+) black_end:([\d.]+)', err)]
    fs = [float(x) for x in re.findall(r'freeze_start: ([\d.]+)', err)]
    fe = [float(x) for x in re.findall(r'freeze_end: ([\d.]+)', err)]
    freezes = [(s, fe[i] if i < len(fe) else info['dur']) for i, s in enumerate(fs)]
    changes = [float(x) for x in re.findall(r'lavfi\.scd\.time=([\d.]+)', err)]
    lufs = re.findall(r'I:\s+(-?[\d.]+) LUFS', err)
    peak = re.findall(r'Peak:\s+(-?[\d.]+) dBFS', err)
    return black, freezes, changes, (float(lufs[-1]) if lufs else None), (float(peak[-1]) if peak else None)


VERDICTS = """## Verdicts (fill in: pass or fix, with the time that shows it; a pass without a frame is not a pass)

| Check | Verdict | Evidence (time, sheet) | Fix |
|---|---|---|---|
| Hook: frame 0 works alone, something moves by 0.5 s | | | |
| Readable at phone size | | | |
| Safe area | | | |
| Something new every 2-3 s (the report's empty stretches; holds are planned) | | | |
| Motion: no overlap, pops, blurry text, flashes | | | |
| Product as in assets/, big enough | | | |
| No AI defaults | | | |
| End: CTA readable, held long enough | | | |
| Sound: about -14 LUFS, hits on cuts | | | |

Three worst, in order:
1.
2.
3.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('video')
    ap.add_argument('--out')
    ap.add_argument('--strip', nargs='*', type=float, default=[])
    ap.add_argument('--hook-only', action='store_true')
    a = ap.parse_args()
    video = os.path.abspath(a.video)
    out = a.out or os.path.join(os.path.dirname(video), 'frame-check')
    os.makedirs(out, exist_ok=True)
    info = probe(video)
    dur, w, h = info['dur'], info['w'], info['h']
    end = max(0.0, dur - 1.5 / info['fps'])
    tmp = tempfile.mkdtemp(prefix='fc-')
    sheets = []
    try:
        # Phone sheets: true 360 px wide frames.
        times = [t for t in (0, 0.5, 1, 2) if t < dur]
        if not a.hook_only:
            t = 3.0
            while t < end - 1:
                times.append(t)
                t += 3
            times.append(end)
        ph = 360 * h / w
        per = max(1, int(MAXSHEET // 360)) * max(1, int(MAXSHEET // ph))
        for s in range(0, len(times), per):
            chunk = times[s:s + per]
            files = []
            for i, t in enumerate(chunk):
                f = os.path.join(tmp, f'ph{s + i:03d}.png')
                if grab(video, t, 360, f):
                    files.append(f)
            name = f'phone-{s // per + 1}.png'
            tile(files, min(len(files), int(MAXSHEET // 360)), os.path.join(out, name))
            sheets.append((name, 'phone width 360 px: ' + ', '.join(f'{t:.1f}s' for t in chunk)))
        if not a.hook_only:
            # Contact sheet: 24 frames spread over the video.
            n = 24 if dur >= 4 else max(4, int(dur * 6))
            cols, tw = fit(n, w, h)
            files = []
            for i in range(n):
                f = os.path.join(tmp, f'c{i:03d}.png')
                if grab(video, (i + 0.5) * dur / n, tw, f):
                    files.append(f)
            tile(files, cols, os.path.join(out, 'contact.png'))
            sheets.insert(0, ('contact.png', f'{n} frames over {dur:.1f}s'))
            # Strips: 8 consecutive frames from each requested time.
            for t0 in a.strip:
                cols, tw = fit(8, w, h)
                files = []
                for i in range(8):
                    f = os.path.join(tmp, f's{i:03d}.png')
                    if grab(video, min(end, t0 + i / info['fps']), tw, f):
                        files.append(f)
                name = f'strip-{t0:.2f}.png'
                tile(files, cols, os.path.join(out, name))
                sheets.append((name, f'8 consecutive frames from {t0:.2f}s'))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    black, freezes, changes, lufs, peak = ([], [], [], None, None) if a.hook_only else measure(video, info)
    lines = [f'# Frame check: {os.path.basename(video)}', '',
             f'- **Video:** {w}x{h}, {info["fps"]:.2f} fps, {dur:.2f} s, audio: {"yes" if info["audio"] else "no"}']
    if not a.hook_only:
        lines.append('- **Black stretches (>= 0.1 s):** ' + (', '.join(f'{s:.2f}-{e:.2f}s' for s, e in black) or 'none'))
        lines.append('- **Still stretches (>= 2.5 s, nothing moves):** ' +
                     (', '.join(f'{s:.2f}-{e:.2f}s' for s, e in freezes) or 'none') +
                     '. A still stretch is fine only if it is a planned hold (end card, CTA)')
        merged, empty = gaps_without_change(changes, dur)
        lines.append(f'- **Visual changes (cuts, B-roll, punch-ins, cards; scene score >= {CHANGE_SCORE}):** '
                     f'{len(merged)}, one every {dur / (len(merged) + 1):.1f} s on average')
        lines.append(f'- **Stretches over {MAX_GAP:.0f} s with nothing new on screen:** ' +
                     (', '.join(f'{s:.1f}-{e:.1f}s ({e - s:.1f})' for s, e in empty) or 'none') +
                     (f'; {sum(e - s for s, e in empty):.0f} s of {dur:.0f} s' if empty else '') +
                     '. A talking head, gestures and caption swaps do not count as new; a small pop-up may not '
                     'register, so check the contact sheet before calling a stretch empty')
        if info['audio']:
            lines.append(f'- **Loudness:** {lufs} LUFS integrated, true peak {peak} dBFS (target about -14 LUFS, peak below -1)')
    lines += ['', '## Sheets', ''] + [f'- `{n}`: {d}' for n, d in sheets] + ['', VERDICTS]
    with open(os.path.join(out, 'report.md'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lines))
    print('\n'.join(lines[:8]))
    print(f'\nwrote {len(sheets)} sheets and report.md to {out}')


if __name__ == '__main__':
    main()
