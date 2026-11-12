#!/bin/bash
# Uso: color.sh <trabajo> [lut.cube]
# Aplica el color grading de Karen (LUT 3D de grade.py) solo al video de ella, antes del render: los gráficos no se tocan.
# Guarda el original como public/input-video-sin-grading.mp4 (la primera vez) y siempre parte de él.
set -e
SK="$(cd "$(dirname "$0")/.." && pwd)"; W="$(realpath "$1")"; LUT="$(realpath "${2:-$SK/assets/karen.cube}")"
[ -f "$W/public/input-video-sin-grading.mp4" ] || mv "$W/public/input-video.mp4" "$W/public/input-video-sin-grading.mp4"
ffmpeg -v error -y -i "$W/public/input-video-sin-grading.mp4" -vf "lut3d=file=$LUT:interp=tetrahedral" -c:v libx264 -crf 17 -g 30 -keyint_min 30 \
  -pix_fmt yuv420p -c:a copy -movflags +faststart "$W/public/input-video.mp4"
echo "grading → $W/public/input-video.mp4 (para la portada: extraer el cuadro con el mismo lut3d y pasar --foto a portada.py)"
