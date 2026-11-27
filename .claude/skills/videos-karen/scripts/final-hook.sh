#!/bin/bash
# Uso: final-hook.sh <trabajo> "<carpeta del hook>"   Tras aprobar previa y portada: video en bucle + portada como primer cuadro.
# Bucle: el último cuadro (aviso + web) se funde 0.5 s en la portada; como el video abre con la portada, la repetición no se nota.
# Guarda en la carpeta: video.mp4, portada.png, graficos/index.html, graficos/words.js y graficos/portada.html. Deja loop-720.mp4 en <trabajo>.
set -e; SK="$(cd "$(dirname "$0")/.." && pwd)"; W="$(realpath "$1")"; D="$2"
[ -f "$W/portada.png" ] || bash "$SK/scripts/portada.sh" "$W"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$W/previa.mp4")
OFF=$(python3 -c "print(round($DUR-0.2,2))"); END=$(python3 -c "print(round($DUR+0.5,2))")
ffmpeg -y -v error -i "$W/previa.mp4" -loop 1 -framerate 30 -t 0.7 -i "$W/portada.png" -filter_complex \
 "[1:v]scale=1080:1920,format=yuv420p,setsar=1,fps=30,settb=1/30[p];[0:v]format=yuv420p,setsar=1,fps=30,settb=1/30[v];[v][p]xfade=transition=fade:duration=0.5:offset=$OFF[o];[0:a]apad=whole_dur=$END[a]" \
 -map "[o]" -map "[a]" -r 30 -c:v libx264 -crf 18 -preset medium -c:a aac -b:a 192k "$W/loop.mp4"
mkdir -p "$D/graficos"
bash "$SK/scripts/portada_primer_cuadro.sh" "$W/loop.mp4" "$W/portada.png" "$D/video.mp4"
cp "$W/portada.png" "$D/"; cp "$W/index.html" "$W/words.js" "$W/portada.html" "$D/graficos/"
ffmpeg -y -v error -i "$D/video.mp4" -vf scale=720:-2 -crf 27 -c:a copy "$W/loop-720.mp4"
ls -la "$D/video.mp4" "$D/portada.png"; echo "revisar el cierre: ffmpeg -sseof -0.6 … y mandar $W/loop-720.mp4"
