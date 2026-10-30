#!/usr/bin/env python3
"""Arma <trabajo>/copy.md con lo mecánico ya puesto y deja {HUECOS} para lo que se escribe a mano (qc.py los marca).
Uso: python3 -I copy.py <trabajo> <NN> "<Nombre>" "<gancho>" [--de NN] [--evitar "02, 23"]
  --de      número del video original (v2 sin cara): llena «Relación» y los «Por confirmar» de siempre.
  --evitar  videos del mismo tema que no deben publicarse seguidos de este.
Toma la duración de final.mp4 (si existe) y los subtítulos de words.json (mismos cortes que build.py, +0.2 s de portada)
o de subtitulos.json (videos con cara, de componer.py)."""
import argparse, json, os, subprocess

ap = argparse.ArgumentParser(); ap.add_argument("trabajo"); ap.add_argument("nn"); ap.add_argument("nombre"); ap.add_argument("gancho")
ap.add_argument("--de"); ap.add_argument("--evitar")
a = ap.parse_args(); W = a.trabajo


def subtitulos():
    if os.path.exists(f"{W}/subtitulos.json"):
        return [(c["ini"], c["texto"]) for c in json.load(open(f"{W}/subtitulos.json"))]
    ch, cur = [], []
    for w in json.load(open(f"{W}/words.json")):  # mismo corte que build.py
        cur.append(w); n = len(" ".join(x[0] for x in cur))
        if w[0][-1] in ".?:" or (w[0][-1] == "," and n > 16) or n > 30: ch.append(cur); cur = []
    if cur: ch.append(cur)
    return [(max(0.02, c[0][1] - 0.02) + 0.2, " ".join(x[0] for x in c)) for c in ch]


dur = "{DURACION}"
if os.path.exists(f"{W}/final.mp4"):
    d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{W}/final.mp4"], capture_output=True, text=True).stdout
    dur = f"{float(d):.1f} s (incluye 0.2 s de portada al inicio)"
v2 = bool(a.de)
rel = ""
if v2:
    ev = f"del {a.de}" + (f" ni del {a.evitar}" if a.evitar else "")
    rel = (f"| Relación | Versión B del {a.de} para prueba A/B: mismo tema, guion nuevo, sin la cara de Karen "
           f"(animación a dos tintas y voz clonada). No publicarlo seguido {ev} |\n")
elif a.evitar:
    rel = f"| Relación | No publicarlo seguido del {a.evitar} |\n"
conf = ("- ✅ **Voz y estilo aprobados por Karen** (30 oct 2026): voz clonada en Eleven v3 con Audio Tags y animación a dos tintas.\n"
        f"- **Guion escrito por el editor**, no por Karen (versión B del {a.de}). {{POR_CONFIRMAR_GUION}}\n"
        "- Rótulos del editor: {ROTULOS}.\n"
        "- Personaje ilustrado (Open Peeps, licencia CC0, sin atribución): confirmar que a Karen le parece bien que la represente una ilustración.\n"
        f"- Número {a.nn}: la fecha de subida la deciden Karen o Eduardo.") if v2 else "- {POR_CONFIRMAR}"
subs = "\n".join(f"| {t:.1f} | {x} |" for t, x in subtitulos())
titulo = f"Video {a.nn}" + (f" (v2 del {a.de})" if v2 else "") + f": {a.nombre}"
md = f"""# {titulo}

| | |
|---|---|
| Formato | 9:16, 1080×1920, {dur} |
| Gancho de portada | **{a.gancho}** |
| Plataformas | Instagram Reels, TikTok, YouTube Shorts, Facebook Reels |
| Archivos | `video.mp4`, `portada.png` |
{rel}
## Título (YouTube Shorts)

{{TITULO_YT}}

## Texto para Instagram y Facebook

{{TEXTO_IG}}

Este video orienta y no diagnostica.

Karen Trujillo, Neuropsicóloga Clínica
psicologakarentrujillo.com.mx

## Texto para TikTok

{{TEXTO_TIKTOK}}

## Hashtags

#TDAH #neuropsicologia #saludmental {{HASHTAGS_TEMA}} #Cancun

## Subtítulos finales (para revisar)

Los segundos ya incluyen los 0.2 s de portada.

| Segundo | Texto |
|---|---|
{subs}

## Por confirmar con Karen

{conf}
"""
open(f"{W}/copy.md", "w", encoding="utf-8").write(md)
print(f"copy → {W}/copy.md (llenar los {{HUECOS}})")
