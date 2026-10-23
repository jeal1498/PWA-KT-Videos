#!/usr/bin/env python3
"""Genera web/data.json y web/t/NN.jpg para la página de calendario (index.html, en la raíz).

Uso (desde la raíz del repo):  python3 -I scripts/exportar_web.py

Lee `calendario.md` (tabla: # | carpeta | gancho | fecha de subida | hecho | publicado) y, de cada
`NN - Nombre/copy.md`, el título de YouTube, el texto de Instagram/Facebook, el de TikTok, los hashtags,
la fila «Relación» y la sección «Por confirmar con Karen». Las miniaturas salen de portada.png.
Estado: «Sí» en Publicado → pub; si no, «Hecho» o «Entregado» → listo; si no → proceso.
Fecha: «sáb 24 oct 2026 (propuesta)» → 2026-10-24 (propuesta = true). Sin fecha → null (sale en «Sin fecha»).
El video se sirve desde su carpeta (misma ruta relativa); nada se copia.
"""
import json, os, re, subprocess, urllib.parse

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
MESES = {m: i + 1 for i, m in enumerate("ene feb mar abr may jun jul ago sep oct nov dic".split())}


def fecha(txt):
    m = re.search(r"(\d{1,2})\s+(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)[a-z]*\s*(\d{4})?", txt)
    if not m:
        return None
    mes = MESES[m.group(2)]
    return f"{m.group(3) or (2027 if mes <= 3 else 2026)}-{mes:02d}-{int(m.group(1)):02d}"


def seccion(md, titulo):
    m = re.search(r"^## " + re.escape(titulo) + r"[^\n]*\n(.*?)(?=^## |\Z)", md, re.S | re.M)
    return m.group(1).strip() if m else None


def main():
    os.makedirs(os.path.join(RAIZ, "web", "t"), exist_ok=True)
    out = []
    for linea in open(os.path.join(RAIZ, "calendario.md"), encoding="utf-8"):
        m = re.match(r"\|\s*(\d\d)\s*\|\s*\[([^\]]+)\]", linea)
        if not m:
            continue
        c = [x.strip() for x in linea.strip().strip("|").split("|")]
        num, carpeta = m.group(1), m.group(2)
        gancho, fe, hecho, pub = c[2], c[3], c[4], c[5]
        d = os.path.join(RAIZ, carpeta)
        if not os.path.isdir(d):
            continue
        md = open(os.path.join(d, "copy.md"), encoding="utf-8").read() if os.path.exists(os.path.join(d, "copy.md")) else ""
        rel = re.search(r"\|\s*Relación\s*\|\s*(.*?)\s*\|", md)
        estado = "pub" if re.match(r"\W*S[ií]\b", pub) else ("listo" if re.search(r"Hecho|Entregado", hecho) else "proceso")
        th = None
        png = os.path.join(d, "portada.png")
        if os.path.exists(png):
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", png, "-vf", "scale=216:384", "-q:v", "5", os.path.join(RAIZ, "web", "t", num + ".jpg")], check=True)
            th = f"web/t/{num}.jpg"
        vid = os.path.join(d, "video.mp4")
        out.append(dict(
            n=num, t=carpeta.split(" - ", 1)[1], gancho=gancho, f=fecha(fe), propuesta="propuesta" in fe.lower(),
            e=estado, p=fecha(pub) if estado == "pub" else None, th=th,
            v=urllib.parse.quote(carpeta) + "/video.mp4" if os.path.exists(vid) else None,
            mb=round(os.path.getsize(vid) / 1048576, 1) if os.path.exists(vid) else None,
            titulo=seccion(md, "Título"), ig=seccion(md, "Texto para Instagram y Facebook"), tiktok=seccion(md, "Texto para TikTok"),
            tags=seccion(md, "Hashtags"), relacion=rel.group(1) if rel else None, confirmar=seccion(md, "Por confirmar con Karen")))
    json.dump(out, open(os.path.join(RAIZ, "web", "data.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(out)} videos → web/data.json")


if __name__ == "__main__":
    main()
