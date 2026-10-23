#!/usr/bin/env python3
"""Fusiona dos tomas del mismo guion (ya pasadas por preparar.sh y encuadre.py).
Uso: fusionar.py <trabajoA> <trabajoB> <salida_trabajo> "T:0-7.9" "A:7.7-58.2" "B:58.1-75.9" ...
  T = toma (A o B) : inicio-fin en segundos de ESA toma. Las piezas van en orden.
Deja <salida>/public/input-video.mp4 (GOP denso, fundidos de audio de 30 ms) y <salida>/words.json con los tiempos ya desplazados.
Antes: copiar fuentes y gsap (public/fonts, gsap.min.js) y hyperframes.json/meta.json a <salida> (como preparar.sh)."""
import sys, json, subprocess, os
a, b, out = sys.argv[1:4]; trozos = []
for s in sys.argv[4:]:
    t, r = s.split(':'); i, f = map(float, r.split('-')); trozos.append((t, i, f))
W = {'A': json.load(open(f'{a}/words.json')), 'B': json.load(open(f'{b}/words.json'))}
V = {'A': f'{a}/public/input-video.mp4', 'B': f'{b}/public/input-video.mp4'}
os.makedirs(f'{out}/public', exist_ok=True)
ins = []; fc = []; t0 = 0.0; words = []
for k, (t, i, f) in enumerate(trozos):
    ins += ['-i', V[t]]; d = f - i
    fc.append(f'[{k}:v]trim={i}:{f},setpts=PTS-STARTPTS,setsar=1[v{k}]')
    fx = (f',afade=t=in:d=0.03' if k else '') + (f',afade=t=out:st={d-0.03:.3f}:d=0.03' if k < len(trozos)-1 else '')
    fc.append(f'[{k}:a]atrim={i}:{f},asetpts=PTS-STARTPTS{fx}[a{k}]')
    for w in W[t]:
        if i <= w['s'] < f: x = dict(w); x['s'] = round(w['s'] - i + t0, 2); words.append(x)
    t0 += d
fc.append(''.join(f'[v{k}][a{k}]' for k in range(len(trozos))) + f'concat=n={len(trozos)}:v=1:a=1[v][a]')
subprocess.run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', ';'.join(fc), '-map', '[v]', '-map', '[a]', '-r', '30',
  '-c:v', 'libx264', '-crf', '17', '-g', '30', '-keyint_min', '30', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
  '-movflags', '+faststart', f'{out}/public/input-video.mp4'], check=True)
json.dump(words, open(f'{out}/words.json', 'w'), ensure_ascii=False)
print(f'{t0:.1f} s, {len(words)} palabras')
