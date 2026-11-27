#!/bin/bash
# Uso: nuevo-hook.sh <trabajo> "<carpeta del hook>"   Copia la plantilla vigente (estilo de referencias, 008 v2; la anterior está en plantilla-hooks-v1), gsap, fuentes,
# la voz (voz.mp3) y los tiempos por palabra (words.json → words.js).
set -e; SK="$(cd "$(dirname "$0")/.." && pwd)"; mkdir -p "$1"
cp "$SK"/plantilla-hooks/* "$1"/; cp "$SK"/assets/gsap.min.js "$SK"/assets/fonts/*.woff2 "$1"/
if [ -n "$2" ]; then cp "$2/voz.mp3" "$1/"
  python3 -I -c 'import json,sys;w=json.load(open(sys.argv[1]));open(sys.argv[2],"w").write("window.WORDS="+json.dumps([[a,round(s,2),round(e,2)] for a,s,e in w],ensure_ascii=False)+";")' "$2/words.json" "$1/words.js"; fi
echo "listo: $1 (reescribir las escenas en index.html; el tiempo sale de words.js)"
