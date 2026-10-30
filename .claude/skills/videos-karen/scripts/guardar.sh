#!/bin/bash
# Guarda uno o un lote de videos ya aprobados en UN solo commit y lo sube a la rama actual (en el trabajo normal, main).
# Uso:  guardar.sh <trabajo> <NN> "<Nombre>" "<gancho>" ["<fecha>"]
#       guardar.sh <lote.tsv>      una línea por video, separada por tabuladores: trabajo  NN  Nombre  gancho  [fecha]
# Cada <trabajo> lleva final.mp4 (con la portada como primer cuadro), portada.png, copy.md y guion.md.
# Hace: carpeta «NN - Nombre/», fila en calendario.md (Hecho), fila en tabla-publicacion.md, web/ (exportar_web.py),
# qc.py --repo de todo el lote (si algo falla, no hace commit) y commit + push.
set -e
SK="$(cd "$(dirname "$0")/.." && pwd)"; R="$(cd "$SK/../../.." && pwd)"; PY="python3 -I"
if [ $# -eq 1 ]; then LOTE="$(realpath "$1")"; else LOTE=$(mktemp); printf '%s\t%s\t%s\t%s\t%s\n' "$(realpath "$1")" "$2" "$3" "$4" "$5" > "$LOTE"; fi
cd "$R"; git pull -q --rebase origin "$(git branch --show-current)" || true
CARPETAS=(); NUMS=()
while IFS=$'\t' read -r W NN NOM G FE; do
  [ -z "$W" ] && continue
  D="$NN - $NOM"; mkdir -p "$D"
  for f in final.mp4:video.mp4 portada.png:portada.png copy.md:copy.md guion.md:guion.md; do
    [ -f "$W/${f%%:*}" ] || { echo "✗ falta $W/${f%%:*}"; exit 1; }; cp "$W/${f%%:*}" "$D/${f##*:}"
  done
  $PY "$SK/scripts/calendario.py" fila "$NN" "$D" "$G" ${FE:+"$FE"}
  $PY "$SK/scripts/calendario.py" tabla "$D"
  CARPETAS+=("$D"); NUMS+=("$NN")
done < "$LOTE"
$PY scripts/exportar_web.py
$PY "$SK/scripts/calendario.py" revisar
$PY "$SK/scripts/qc.py" "${CARPETAS[@]}" --repo || { echo "✗ No se guardó: corregir y volver a correr (los archivos ya están copiados)."; exit 1; }
git add "${CARPETAS[@]}" calendario.md tabla-publicacion.md web
git commit -q -m "Videos ${NUMS[*]}: hechos (lote aprobado)

Co-Authored-By: Claude <noreply@anthropic.com>"
git push -u origin HEAD
