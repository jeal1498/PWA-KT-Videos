#!/bin/bash
# Uso: loop.sh <final.mp4> <portada.png> — deja el último cuadro igual al primero (la portada) para que el video haga loop.
# Funde el cierre a la portada (0.5 s) y la sostiene 0.6 s. Reemplaza final.mp4 (queda +0.6 s). Correr antes de sacar prueba-720.
set -e
V="$(realpath "$1")"; P="$(realpath "$2")"; D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
O="${V%.mp4}-loop.mp4"
ffmpeg -v error -y -i "$V" -loop 1 -framerate 30 -t 1.1 -i "$P" -filter_complex \
 "[1:v]scale=1080:1920,format=yuv420p,setsar=1,fps=30[p];[0:v]format=yuv420p,setsar=1,fps=30[v];[v][p]xfade=transition=fade:duration=0.5:offset=$(python3 -c "print(round($D-0.5,3))")[o];[0:a]apad=pad_dur=1.2[a]" \
 -map "[o]" -map "[a]" -t "$(python3 -c "print(round($D+0.6,3))")" -c:v libx264 -preset medium -crf 18 -c:a aac -b:a 160k -movflags +faststart "$O"
mv -f "$O" "$V"; echo "loop: $V $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V") s"
