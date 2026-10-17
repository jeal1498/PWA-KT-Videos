#!/bin/bash
# Uso: revisar.sh <video_final.mp4> <portada.png> <copy.md> [spec.json]
# Lista de verificación automática antes de guardar (etapa 6). Sale con código 1 si algo falla.
# Revisa: formato 1080x1920, audio, ≈30 fps, tamaño <100 MB, volumen ≈ -16 LUFS, portada como primer cuadro,
# copy (sección «Por confirmar», web, frases prohibidas) y, si se pasa el spec, que las escenas sumen ≤ 40 %.
V="$1"; P="$2"; C="$3"; SPEC="$4"; FAIL=0
ok(){ echo "  ✓ $1"; }; no(){ echo "  ✗ $1"; FAIL=1; }; av(){ echo "  ! $1"; }
echo "Revisando $V"
W=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$V")
[ "$W" = "1080,1920" ] && ok "1080x1920" || no "tamaño $W (debe ser 1080,1920)"
FPS=$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$V" | awk -F/ '{printf "%d", $1/$2}')
[ "$FPS" = "30" ] && ok "30 fps" || av "fps $FPS (se esperan 30)"
ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of csv=p=0 "$V" | grep -q . && ok "tiene audio" || no "sin audio"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V" | awk '{printf "%.1f", $1}'); ok "duración ${DUR} s"
MB=$(( $(stat -c %s "$V") / 1048576 )); [ "$MB" -lt 95 ] && ok "${MB} MB (límite de GitHub 100 MB)" || no "${MB} MB: recomprimir con -crf 26"
LU=$(ffmpeg -nostats -i "$V" -af ebur128=peak=none -f null - 2>&1 | awk '/I:/ {v=$2} END {print v}')
if [ -n "$LU" ]; then awk -v l="$LU" 'BEGIN{exit !(l>-19 && l<-13)}' && ok "volumen ${LU} LUFS" || av "volumen ${LU} LUFS (objetivo -16)"; fi
SS=$(ffmpeg -nostats -i "$V" -i "$P" -filter_complex "[0:v]trim=end_frame=1,setpts=PTS-STARTPTS[a];[1:v]scale=1080:1920[b];[a][b]ssim" -f null - 2>&1 | grep -o 'All:[0-9.]*' | head -1 | cut -d: -f2)
[ -n "$SS" ] && awk -v s="$SS" 'BEGIN{exit !(s>0.9)}' && ok "la portada es el primer cuadro (ssim $SS)" || av "el primer cuadro no parece la portada (ssim ${SS:-n/d})"
grep -qi "por confirmar" "$C" && ok "copy con «Por confirmar»" || no "falta la sección «Por confirmar con Karen» en el copy"
grep -q "psicologakarentrujillo.com.mx" "$C" && ok "copy con la web" || av "el copy no menciona psicologakarentrujillo.com.mx"
if grep -qiE "\b(cura|curar|curamos|garantiza|garantizado|transforma tu vida)\b" "$C"; then no "el copy tiene una frase prohibida (cura, garantiza, transforma tu vida)"; else ok "sin frases prohibidas"; fi
if [ -n "$SPEC" ]; then
  python3 - "$SPEC" <<'PY' && ok "escenas dentro del tope" || { echo "  ✗ las escenas pasan del 40 % del video"; exit 1; }
import json, sys
s = json.load(open(sys.argv[1])); d = s['duracion']; e = sum(x['fin'] - x['ini'] for x in s.get('escenas', []))
print(f"  · escenas: {e:.1f} s de {d:.1f} s ({100*e/d:.0f} %)"); sys.exit(0 if e / d <= 0.40 else 1)
PY
  [ $? -eq 0 ] || FAIL=1
fi
echo; echo "A ojo, antes de guardar:"
echo "  [ ] subtítulos en frases cortas, sin errores de transcripción"
echo "  [ ] rótulo con nombre, cargo y cédula 11009616 al inicio"
echo "  [ ] ninguna escena tapa el rótulo, el gancho o una tarjeta"
echo "  [ ] cierre con acción, web y el aviso «Este video orienta y no diagnostica»"
echo "  [ ] sin datos que identifiquen a nadie; lo que Karen no dijo está marcado «Ejemplo»"
exit $FAIL
