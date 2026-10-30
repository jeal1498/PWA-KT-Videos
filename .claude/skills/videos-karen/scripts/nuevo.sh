#!/bin/bash
# Uso: nuevo.sh <trabajo> [guion.txt]
# Crea la carpeta de trabajo de una v2 sin cara desde plantilla-v2/ (la del 25): build.py, scenes.py, anim.js,
# portada.html y public/ con gsap y fuentes. Usar una carpeta en el scratchpad, no en el repo.
set -e
SK="$(cd "$(dirname "$0")/.." && pwd)"; W="$1"
mkdir -p "$W/public/fonts"
for f in build.py scenes.py anim.js portada.html; do [ -e "$W/$f" ] || cp "$SK/plantilla-v2/$f" "$W/"; done
cp "$SK"/assets/fonts/*.woff2 "$W/public/fonts/"; cp "$SK/assets/gsap.min.js" "$W/public/"
[ -n "$2" ] && cp "$2" "$W/guion.txt"
echo "listo: $W (siguiente: voz.py guion.txt $W --modelo v3 --max-silencio 0.35)"
