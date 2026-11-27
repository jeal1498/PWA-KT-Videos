#!/bin/bash
# Uso: previa-hook.sh <trabajo> [--hoja]   Con --hoja: un cuadro por segundo (g_NNN.png) y hojas de contacto (hoja_N.png) para revisar huecos y encimados.
# Sin --hoja: previa.mp4 (1080×1920, 30 fps, con voz.mp3) y previa-720.mp4 (para SendUserFile). Correr con run_in_background (≈5 min).
set -e; cd "$1"; export NODE_PATH=/opt/node22/lib/node_modules
if [ "$2" = "--hoja" ]; then rm -f g_*.png hoja_*.png; node hoja.cjs; n=$(ls g_*.png | wc -l)
  for k in $(seq 0 $(( (n-1)/12 ))); do montage $(ls g_*.png | sed -n "$((k*12+1)),$((k*12+12))p") -tile 6x2 -geometry 300x+4+4 -background '#444' hoja_$k.png; done; ls hoja_*.png; exit 0; fi
node render.cjs
ffmpeg -v error -y -i previa.mp4 -vf scale=720:-2 -crf 27 previa-720.mp4
ls -la previa.mp4 previa-720.mp4
