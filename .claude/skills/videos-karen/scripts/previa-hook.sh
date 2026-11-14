#!/bin/bash
# Uso: previa-hook.sh <trabajo> [--hoja]   Con --hoja: un cuadro por segundo (g_*.png) para revisar huecos y encimados.
# Sin --hoja: previa.mp4 (1080×1920) y previa-720.mp4 (para SendUserFile). Correr con run_in_background (≈4 min).
set -e; cd "$1"; export NODE_PATH=/opt/node22/lib/node_modules
if [ "$2" = "--hoja" ]; then rm -f g_*.png; node hoja.cjs; ls g_*.png | wc -l; exit 0; fi
node render.cjs full
ffmpeg -v error -y -i previa.mp4 -vf scale=720:-2 -crf 27 previa-720.mp4
ls -la previa.mp4 previa-720.mp4
