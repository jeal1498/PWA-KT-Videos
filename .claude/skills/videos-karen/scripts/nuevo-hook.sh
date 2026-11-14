#!/bin/bash
# Uso: nuevo-hook.sh <trabajo>   Copia la plantilla de hooks virales (la del 001) con gsap y fuentes.
set -e; SK="$(cd "$(dirname "$0")/.." && pwd)"; mkdir -p "$1"
cp "$SK"/plantilla-hooks/* "$1"/; cp "$SK"/assets/gsap.min.js "$SK"/assets/fonts/*.woff2 "$1"/
echo "listo: $1 (editar SEC y escenas en index.html)"
