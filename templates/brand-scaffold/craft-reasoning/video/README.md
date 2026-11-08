# Creative / video

Where the `video-edits` skill saves its output for this brand: one folder per run,
`<YYYY-MM-DD>-<brief-id>/`, holding:

- `transcript.json`: the timed transcript of the raw footage
- `edl.md`: the edit decision list the human approved (which takes, in what order, and why)
- `trimmed.mp4` + `hooks/`: the trimmed cut and hook clips for approval 1
- `broll/`: supplied, HTML-built and generated B-roll used in the edit
- `timeline/`: only when a human editor will finish an ad (FCPXML for DaVinci Resolve / Final Cut)
- `render.py`: the script that renders the whole hook × length matrix
- `<brief-id>_H<n>_<length>s.mp4`: the rendered ads, styled Danish captions burned in
- `captions-da.srt`: the same captions as a separate file
- `grid.html`: the review grid for picking
- `gaps.md`: the parts left for a human editor (masks, advanced effects)

Raw footage is **not** copied here. It stays where creators upload it (see `tool-map.md`, the
"Raw footage" role); the run folder points to it.
