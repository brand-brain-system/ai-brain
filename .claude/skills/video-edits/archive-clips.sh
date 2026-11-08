#!/usr/bin/env bash
# Internet Archive film -> shot list -> 9:16 clip with a blurred fill. See video-edits/SKILL.md step 6.
#   archive-clips.sh fetch <identifier> <dir>            check licence, download the 640x480 file, write <dir>/<id>.meta
#   archive-clips.sh shots <dir>/<id>.mp4                list shots (start, end, length) cut on real scene changes
#   archive-clips.sh cut   <file> <start> <len> <out>    one 9:16 clip: the 4:3 frame whole, over its own blurred copy
# Needs curl and ffmpeg (set FFMPEG if it is not on PATH). No key, no Python. Preview size by default (540x960);
# set W=1080 H=1920 for the final.
set -euo pipefail
FFMPEG="${FFMPEG:-ffmpeg}"
W="${W:-540}"; H="${H:-960}"; SCENE="${SCENE:-0.35}"; MINLEN="${MINLEN:-1.5}"

case "${1:-}" in
fetch)
  id="$2"; dir="$3"; mkdir -p "$dir"
  meta="$(curl -fsS "https://archive.org/metadata/$id")"
  lic="$(printf '%s' "$meta" | grep -o '"licenseurl": *"[^"]*"' | head -1 | sed 's/.*: *"\(.*\)"/\1/' || true)"
  title="$(printf '%s' "$meta" | grep -o '"title": *"[^"]*"' | head -1 | sed 's/.*: *"\(.*\)"/\1/' || true)"
  case "$lic" in
    *publicdomain*|*/zero/*) ;;
    *) echo "STOP: $id has no public-domain licence field (licenseurl='${lic:-none}'). A person must clear it first." >&2; exit 2;;
  esac
  # the plain h.264 file is 640x480; the _512kb one is 320x240
  file="$id.mp4"
  curl -fsSL -o "$dir/$id.mp4" "https://archive.org/download/$id/$file"
  printf 'id=%s\ntitle=%s\nlicenseurl=%s\nurl=https://archive.org/details/%s\nfile=%s\n' "$id" "$title" "$lic" "$id" "$file" > "$dir/$id.meta"
  cat "$dir/$id.meta";;
shots)
  f="$2"
  dur="$("$FFMPEG" -hide_banner -i "$f" 2>&1 | sed -n 's/.*Duration: \([0-9:.]*\).*/\1/p' | head -1 | awk -F: '{printf "%.2f",$1*3600+$2*60+$3}' || true)"
  "$FFMPEG" -hide_banner -nostats -i "$f" -an -vf "select='gt(scene,$SCENE)',showinfo" -f null - 2>&1 \
    | sed -n 's/.*pts_time:\([0-9.]*\).*/\1/p' \
    | awk -v dur="$dur" -v min="$MINLEN" 'BEGIN{s=0} {if($1-s>=min){printf "%.2f\t%.2f\t%.2f\n",s,$1,$1-s; s=$1}} END{if(dur-s>=min)printf "%.2f\t%.2f\t%.2f\n",s,dur,dur-s}';;
cut)
  f="$2"; ss="$3"; len="$4"; out="$5"
  "$FFMPEG" -hide_banner -loglevel error -y -ss "$ss" -t "$len" -i "$f" -an -filter_complex \
    "[0:v]split[a][b];[a]scale=${W}:${H}:force_original_aspect_ratio=increase,crop=${W}:${H},boxblur=20:2,eq=brightness=-0.15[bg];[b]scale=${W}:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1,fps=30" \
    -c:v libx264 -preset veryfast -crf 22 -pix_fmt yuv420p "$out";;
*) sed -n '2,8p' "$0"; exit 1;;
esac
