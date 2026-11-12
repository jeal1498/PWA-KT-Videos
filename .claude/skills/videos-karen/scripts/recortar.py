#!/usr/bin/env python3
"""Recorta los silencios de un video con cara y reajusta todos los tiempos.
Uso: python3 -I recortar.py <trabajo> [--max 0.5] [--margen 0.15] [--extra "54.6-56.78,69.2-72.78"] [--respirar "54,70"]
- Corta toda pausa entre palabras de más de --max s, dejando --margen s a cada lado.
- --extra: tramos sin voz que también se cortan (p. ej. ella sonriendo callada); --respirar: segundos cuya pausa se respeta.
- La primera vez guarda public/input-video-sin-recorte.mp4, words-sin-recorte.json y spec-sin-recorte.json; siempre parte de ellos.
- Escribe cortes.json (para pasar tiempos de la animación con M(t)), public/input-video.mp4, words.json y spec.json
  (ajustes, ini/fin y anclas [palabra, t] remapeados)."""
import json, os, subprocess, argparse, shutil
ap = argparse.ArgumentParser(); ap.add_argument('trabajo'); ap.add_argument('--max', type=float, default=0.5)
ap.add_argument('--margen', type=float, default=0.15); ap.add_argument('--extra', default=''); ap.add_argument('--respirar', default='')
a = ap.parse_args(); os.chdir(a.trabajo)
for src, dst in (('public/input-video.mp4', 'public/input-video-sin-recorte.mp4'), ('words.json', 'words-sin-recorte.json'), ('spec.json', 'spec-sin-recorte.json')):
    if not os.path.exists(dst): shutil.copy(src, dst)
W0 = json.load(open('words-sin-recorte.json'))
D = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', 'public/input-video-sin-recorte.mp4'], capture_output=True, text=True).stdout)
resp = [float(x) for x in a.respirar.split(',') if x]
cuts = [(round(x['e'] + a.margen, 2), round(y['s'] - a.margen, 2)) for x, y in zip(W0, W0[1:])
        if y['s'] - x['e'] > a.max and not any(x['e'] < r < y['s'] for r in resp)]
cuts += [tuple(float(v) for v in t.split('-')) for t in a.extra.split(',') if t]
cuts = sorted(cuts); json.dump(cuts, open('cortes.json', 'w'))
def M(t):
    r = t
    for x, y in cuts:
        if t >= y: r -= y - x
        elif t > x: r -= t - x
    return r
keep = []; p = 0
for x, y in cuts: keep.append((p, x)); p = y
keep.append((p, D))
fc = ''.join(f"[0:v]trim={x}:{y},setpts=PTS-STARTPTS[v{i}];[0:a]atrim={x}:{y},asetpts=PTS-STARTPTS[a{i}];" for i, (x, y) in enumerate(keep))
fc += ''.join(f"[v{i}][a{i}]" for i in range(len(keep))) + f"concat=n={len(keep)}:v=1:a=1[v][a]"
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'public/input-video-sin-recorte.mp4', '-filter_complex', fc, '-map', '[v]', '-map', '[a]',
                '-c:v', 'libx264', '-crf', '17', '-g', '30', '-keyint_min', '30', '-pix_fmt', 'yuv420p', '-ar', '48000', '-c:a', 'aac', '-b:a', '192k',
                '-movflags', '+faststart', 'public/input-video.mp4'], check=True)
json.dump([dict(t=w['t'], s=round(M(w['s']), 2), e=round(M(w['e']), 2)) for w in W0], open('words.json', 'w'), ensure_ascii=False)
def remap(o, k=None):
    if isinstance(o, dict): return {kk: remap(v, kk) for kk, v in o.items()}
    if isinstance(o, list):
        if len(o) in (2, 3) and isinstance(o[0], str) and isinstance(o[1], (int, float)): return [o[0], round(M(o[1]), 2)] + o[2:]
        return [remap(v) for v in o]
    if k in ('ini', 'fin') and isinstance(o, (int, float)): return round(M(o), 2)
    return o
sp = remap(json.load(open('spec-sin-recorte.json')))
sp['ajustes'] = {f"{M(float(k)):.2f}": v for k, v in sp.get('ajustes', {}).items()}
sp['duracion'] = round(M(D), 4)
json.dump(sp, open('spec.json', 'w'), ensure_ascii=False, indent=1)
print(f'{len(cuts)} cortes, {D:.1f} s → {M(D):.1f} s (spec.json y words.json remapeados; animación a medida: usar M(t) con cortes.json)')
