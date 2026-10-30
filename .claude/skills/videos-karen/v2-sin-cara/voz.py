#!/usr/bin/env python3
"""Genera la voz de un guion con ElevenLabs y los tiempos por palabra (words.json) para animar.
Uso: python3 -I voz.py <guion.txt> <salida_dir> [--voz ID] [--modelo v2|v3] [--max-silencio 0.35]
  --modelo v3     Eleven v3: admite Audio Tags ([sighs], [pause], [curious], [softly], [warmly]…). Los tags no
                  cuentan como palabras en words.json. Con v2 los tags se leerían como texto.
  --max-silencio  acorta cada silencio real (−45 dB) más largo que eso; deja los tiempos por palabra cuadrados.
                  v3 mete pausas largas (hasta 1.8 s con [pause]); 0.35 s quedó natural en la prueba del 30 oct 2026.
Necesita ELEVENLABS_API_KEY. Escribe <salida_dir>/voz.mp3 y <salida_dir>/words.json ([palabra, inicio, fin] en s)."""
import argparse, base64, json, os, re, subprocess, urllib.request
# Voz por defecto: la clonada de Karen.
VOZ_KAREN = 'sSQiAF9Uq1K3xnyvFi8w'  # voz clonada de Karen (Eduardo, 30 oct 2026)
VOZ_PROVISIONAL = 'dlGxemPxFMTY7iXagmOj'  # Fernando Martínez, la voz de Checa
ap = argparse.ArgumentParser(); ap.add_argument('guion'); ap.add_argument('salida'); ap.add_argument('voz_pos', nargs='?')
ap.add_argument('--voz'); ap.add_argument('--modelo', default='v2', choices=['v2', 'v3']); ap.add_argument('--max-silencio', type=float)
a = ap.parse_args()
vid = a.voz or a.voz_pos or VOZ_KAREN
if vid == VOZ_PROVISIONAL: print('Aviso: voz provisional (Fernando), no es la de Karen.')
txt, out = open(a.guion, encoding='utf-8').read().strip(), a.salida
os.makedirs(out, exist_ok=True)
body = {'text': txt, 'model_id': 'eleven_v3' if a.modelo == 'v3' else 'eleven_multilingual_v2', 'language_code': 'es'}
if a.modelo == 'v2': body['voice_settings'] = {'speed': 1.0}
req = urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{vid}/with-timestamps?output_format=mp3_44100_128',
    data=json.dumps(body).encode(), headers={'xi-api-key': os.environ['ELEVENLABS_API_KEY'], 'Content-Type': 'application/json'})
d = json.load(urllib.request.urlopen(req))
crudo = f'{out}/voz-cruda.mp3' if a.max_silencio else f'{out}/voz.mp3'
open(crudo, 'wb').write(base64.b64decode(d['audio_base64']))
# palabras, sin los [tags]
al = d['alignment']; words = []; cur = ''; st = None; fin = 0; tag = False
for ch, s, e in zip(al['characters'], al['character_start_times_seconds'], al['character_end_times_seconds']):
    if ch == '[': tag = True
    if tag:
        tag = ch != ']'; continue
    if ch in ' \n':
        if cur: words.append([cur, st, fin]); cur = ''; st = None
    else:
        st = s if st is None else st; cur += ch; fin = e
if cur: words.append([cur, st, fin])
if a.max_silencio:
    # silencios reales del audio; de cada uno se quita lo que sobra, conservando la mitad del margen a cada lado
    r = subprocess.run(['ffmpeg', '-i', crudo, '-af', 'silencedetect=noise=-45dB:d=0.2', '-f', 'null', '-'], capture_output=True, text=True).stderr
    ini = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]; fn = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
    m = a.max_silencio; cortes = [(s0 + m / 2, s1 - m / 2) for s0, s1 in zip(ini, fn) if s1 - s0 > m and s0 > 0.05]
    dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', crudo], capture_output=True, text=True).stdout)
    keep = []; t = 0.0
    for c0, c1 in cortes: keep.append((t, c0)); t = c1
    keep.append((t, dur))
    f = ''.join(f'[0:a]atrim={k0:.3f}:{k1:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.01,afade=t=out:st={max(k1-k0-0.01,0):.3f}:d=0.01[a{i}];' for i, (k0, k1) in enumerate(keep))
    f += ''.join(f'[a{i}]' for i in range(len(keep))) + f'concat=n={len(keep)}:v=0:a=1[o]'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', crudo, '-filter_complex', f, '-map', '[o]', '-b:a', '128k', f'{out}/voz.mp3'], check=True)
    def mueve(x):
        q = 0.0
        for c0, c1 in cortes:
            if x >= c1: q += c1 - c0
            elif x > c0: return c0 - q
        return x - q
    words = [[w, round(mueve(s), 3), round(mueve(e), 3)] for w, s, e in words]
    print(f'{len(cortes)} silencios recortados ({sum(c1 - c0 for c0, c1 in cortes):.2f} s)')
json.dump(words, open(f'{out}/words.json', 'w'), ensure_ascii=False)
print(len(words), 'palabras,', round(words[-1][2], 2), 's')
