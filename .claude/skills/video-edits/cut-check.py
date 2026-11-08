"""cut-check.py: run on every version of a cut before a human sees it. Prints PASS or FAIL.
Needs python3 and ffmpeg only (no numpy). Set FFMPEG=<path> when ffmpeg is not on PATH.

Usage:
  python cut-check.py --voice VOICE.wav --clips clips.json [--out CUT.mp4]
                      [--edges edges.json --fps 30]

clips.json   [[start, end], ...] in seconds on the VOICE file's own timeline: the pieces the cut keeps.
--out        the rendered cut; checked for pauses (a pause full of breathing passes this, so also
             compare the cut's own transcript for gaps between words, see SKILL.md step 9).
edges.json   {"aroll": [frame, ...], "broll": [frame, ...]}: every a-roll cut and every B-roll start and
             end in the finished video, as whole frame numbers.

Checks:
 1. Ends:   the last 50 ms inside each piece is below -30 dB, so no word is cut off. Pieces shorter
            than 0.3 s are flagged: almost always a stray syllable.
 2. Starts: the 30 ms before each piece (after the first) is below -30 dB, so no piece starts mid-word.
 3. Gaps:   no silence of 0.25 s or more in --out, except the final hold. Needs --out.
 4. Frames: no segment between two edges under 9 frames at 30 fps (0.3 s), and no B-roll edge within
            9 frames of an a-roll cut without sitting on it. Needs --edges and --fps.
This is a measurement, not a verdict on taste: a PASS means no chopped word or stray flash was found.
Adapted from the cut check in alyshadotmd/video-editing (no licence; idea and thresholds only, own code).
"""
import argparse, array, json, math, os, re, subprocess, sys

FFMPEG = os.environ.get('FFMPEG', 'ffmpeg')
PRIO = getattr(subprocess, 'BELOW_NORMAL_PRIORITY_CLASS', 0)
SPEECH_DB = -30.0
MIN_PIECE = 0.3
MIN_SEGMENT_S = 0.3


def pcm(path, start, length, sr=16000):
    cmd = [FFMPEG, '-v', 'error', '-ss', f'{max(0.0, start):.4f}', '-t', f'{length:.4f}', '-i', path,
           '-ac', '1', '-ar', str(sr), '-f', 's16le', '-']
    raw = subprocess.run(cmd, capture_output=True, creationflags=PRIO).stdout
    a = array.array('h')
    a.frombytes(raw[: len(raw) // 2 * 2])
    return a


def db(samples):
    if not samples:
        return -99.0
    rms = math.sqrt(sum(s * s for s in samples) / len(samples))
    return 20 * math.log10(rms / 32768 + 1e-9)


def check_pieces(voice, clips):
    fails = 0
    print('1-2. ENDS AND STARTS')
    for i, (a, b) in enumerate(clips):
        notes = []
        end = db(pcm(voice, b - 0.05, 0.05))
        pre = db(pcm(voice, a - 0.03, 0.03)) if i > 0 and a >= 0.03 else -99.0
        if end > SPEECH_DB:
            notes.append('END cuts off a word: move it later to where the level drops')
        if pre > SPEECH_DB:
            notes.append('START cuts into a word: move it earlier to where the level is quiet')
        if b - a < MIN_PIECE:
            notes.append(f'under {MIN_PIECE} s: a stray syllable unless it holds a whole word')
        fails += len(notes)
        print(f'  piece {i + 1} {a:.2f}-{b:.2f}: before start {pre:.0f} dB, last 50 ms {end:.0f} dB',
              ('  <-- ' + '; '.join(notes)) if notes else '')
    return fails


def check_gaps(out):
    print('3. GAPS')
    r = subprocess.run([FFMPEG, '-nostats', '-i', out, '-af', 'silencedetect=n=-30dB:d=0.25', '-f', 'null', '-'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace', creationflags=PRIO).stderr
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r)
    dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else None
    fails = 0
    for t in re.findall(r'silence_start: ([\d.]+)', r):
        t = float(t)
        if dur is None or t < dur - 0.8:
            fails += 1
            print(f'  gap at {t:.2f} s  <--')
    if not fails:
        print('  none')
    return fails


def check_frames(edges, fps):
    print('4. FRAMES')
    near = round(fps * MIN_SEGMENT_S)
    aroll = sorted(set(edges.get('aroll', [])))
    broll = sorted(set(edges.get('broll', [])))
    allpts = sorted(set(aroll) | set(broll))
    fails = 0
    for p, q in zip(allpts, allpts[1:]):
        if q - p < near:
            fails += 1
            print(f'  segment frames {p}-{q} is {q - p} frames (under {near}): a flash  <--')
    for e in broll:
        for c in aroll:
            if 0 < abs(e - c) < near:
                fails += 1
                print(f'  B-roll edge at frame {e} is {abs(e - c)} frames from the cut at {c}: move it onto the cut  <--')
    if not fails:
        print('  none')
    return fails


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--voice', required=True)
    ap.add_argument('--clips', required=True)
    ap.add_argument('--out')
    ap.add_argument('--edges')
    ap.add_argument('--fps', type=float, default=30)
    A = ap.parse_args()
    with open(A.clips, encoding='utf-8-sig') as f:
        clips = json.load(f)
    fails = check_pieces(A.voice, clips)
    if A.out:
        fails += check_gaps(A.out)
    if A.edges:
        with open(A.edges, encoding='utf-8-sig') as f:
            fails += check_frames(json.load(f), A.fps)
    print('RESULT', 'PASS' if not fails else f'FAIL ({fails})')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
