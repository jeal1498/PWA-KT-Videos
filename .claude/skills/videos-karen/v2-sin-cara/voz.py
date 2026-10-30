#!/usr/bin/env python3
"""Genera la voz de un guion con ElevenLabs y los tiempos por palabra (words.json) para animar.
Uso: python3 -I voz.py <guion.txt> <salida_dir> [voice_id]
Necesita ELEVENLABS_API_KEY. Voz por defecto: provisional de Checa (Fernando Martínez); cambiarla por la clonada de Karen.
Escribe <salida_dir>/voz.mp3 y <salida_dir>/words.json ([palabra, inicio, fin] en segundos)."""
import base64, json, os, sys, urllib.request
txt, out = open(sys.argv[1], encoding='utf-8').read().strip(), sys.argv[2]
# Voz por defecto: la clonada de Karen.
VOZ_KAREN = 'sSQiAF9Uq1K3xnyvFi8w'  # voz clonada de Karen (Eduardo, 30 oct 2026)
VOZ_PROVISIONAL = 'dlGxemPxFMTY7iXagmOj'  # Fernando Martínez, la voz de Checa
vid = sys.argv[3] if len(sys.argv) > 3 else (VOZ_KAREN or VOZ_PROVISIONAL)
if vid == VOZ_PROVISIONAL: print('Aviso: voz provisional (Fernando), no es la de Karen.')
os.makedirs(out, exist_ok=True)
req = urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{vid}/with-timestamps?output_format=mp3_44100_128',
    data=json.dumps({'text': txt, 'model_id': 'eleven_multilingual_v2', 'language_code': 'es', 'voice_settings': {'speed': 1.0}}).encode(),
    headers={'xi-api-key': os.environ['ELEVENLABS_API_KEY'], 'Content-Type': 'application/json'})
d = json.load(urllib.request.urlopen(req))
open(f'{out}/voz.mp3', 'wb').write(base64.b64decode(d['audio_base64']))
a = d['alignment']; words = []; cur = ''; st = None; fin = 0
for ch, s, e in zip(a['characters'], a['character_start_times_seconds'], a['character_end_times_seconds']):
    if ch in ' \n':
        if cur: words.append([cur, st, fin]); cur = ''; st = None
    else:
        st = s if st is None else st; cur += ch; fin = e
if cur: words.append([cur, st, fin])
json.dump(words, open(f'{out}/words.json', 'w'), ensure_ascii=False)
print(len(words), 'palabras,', round(words[-1][2], 2), 's')
