#!/usr/bin/env python3
"""Control de calidad automático de uno o varios videos. Sale con código 1 si algo falla (✗); los avisos (!) no frenan.
Uso: python3 -I qc.py <carpeta> [<carpeta> ...] [--repo]
  <carpeta>  la del repo (`NN - Nombre/`: video.mp4, portada.png, copy.md, guion.md) o la de trabajo
             (final.mp4, portada.png, copy.md, guion.txt). Un video es «v2» si su nombre o su guion dice «v2» o tiene voz.mp3.
  --repo     revisa además calendario.md, tabla-publicacion.md, web/data.json y los archivos de más de 95 MB.
Revisa: mp4 (1080x1920, 30 fps, audio, <95 MB, −16 LUFS, portada como primer cuadro, tramos quietos), portada
(v2: nada fuera de y=300–1620), guion (palabras, tags, no abrir con [pause]), copy (secciones, web, aviso, huecos
sin llenar, frases prohibidas, rayas largas, título ≤100) y, con --repo, que todo esté dado de alta."""
import json, os, re, subprocess, sys
import numpy as np
from PIL import Image, ImageFilter

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *[".."] * 4))
PROHIBIDAS = r"\b(cura|curar|curamos|se cura|garantiza\w*|transforma\w* tu vida|te diagnostico|diagn[oó]stico seguro)\b"
FALLOS = 0


def ok(t): print(f"  ✓ {t}")
def av(t): print(f"  ! {t}")
def no(t):
    global FALLOS; FALLOS += 1; print(f"  ✗ {t}")


def sh(*a): return subprocess.run(a, capture_output=True, text=True)
def probe(v, q): return sh("ffprobe", "-v", "error", *q, "-of", "csv=p=0", v).stdout.strip()
def leer(p): return open(p, encoding="utf-8").read() if os.path.exists(p) else None
def primero(d, *n): return next((os.path.join(d, x) for x in n if os.path.exists(os.path.join(d, x))), None)


def video(v, portada, v2):
    w = probe(v, ["-select_streams", "v:0", "-show_entries", "stream=width,height"])
    ok("1080x1920") if w == "1080,1920" else no(f"tamaño {w} (debe ser 1080x1920)")
    fps = probe(v, ["-select_streams", "v:0", "-show_entries", "stream=r_frame_rate"]).split("/")
    f = round(int(fps[0]) / int(fps[1])) if len(fps) == 2 else 0
    ok("30 fps") if f == 30 else av(f"{f} fps (se esperan 30)")
    ok("tiene audio") if probe(v, ["-select_streams", "a:0", "-show_entries", "stream=codec_name"]) else no("sin audio")
    dur = float(probe(v, ["-show_entries", "format=duration"]) or 0)
    mb = os.path.getsize(v) / 1048576
    (ok if mb < 95 else no)(f"{mb:.0f} MB (límite de GitHub 100 MB)")
    (ok if 30 <= dur <= 95 else av)(f"duración {dur:.1f} s")
    lu = re.findall(r"I:\s+(-?[0-9.]+) LUFS", sh("ffmpeg", "-nostats", "-i", v, "-af", "ebur128", "-f", "null", "-").stderr)
    if lu: (ok if -19 < float(lu[-1]) < -13 else av)(f"volumen {lu[-1]} LUFS (objetivo −16)")
    if portada:
        s = re.search(r"All:([0-9.]+)", sh("ffmpeg", "-nostats", "-i", v, "-i", portada, "-filter_complex",
                      "[0:v]trim=end_frame=1,setpts=PTS-STARTPTS[a];[1:v]scale=1080:1920,format=yuv420p[b];[a][b]ssim", "-f", "null", "-").stderr)
        (ok if s and float(s.group(1)) > 0.9 else no)(f"la portada es el primer cuadro (ssim {s.group(1) if s else 'n/d'})")
    if v2:  # tramos de más de 4 s casi sin cambios (el trazo vibra siempre, por eso n=0.01)
        q = re.findall(r"freeze_duration: ([0-9.]+)", sh("ffmpeg", "-nostats", "-i", v, "-vf", "freezedetect=n=0.01:d=4", "-map", "0:v", "-f", "null", "-").stderr)
        ok("sin tramos quietos de más de 4 s") if not q else av(f"{len(q)} tramo(s) quieto(s) de más de 4 s: revisar la hoja de vistazo")


def portada_v2(p):
    im = Image.open(p).convert("L")
    if im.size != (1080, 1920): return no(f"portada de {im.size} (debe ser 1080x1920)")
    # bordes (texto, trazos) fuera de la zona segura; el fondo es un degradado liso
    e = np.asarray(im.filter(ImageFilter.FIND_EDGES), dtype=np.uint8)
    fuera = [(a, b) for a, b in ((0, 290), (1630, 1920)) if (e[a:b, 8:-8] > 60).mean() > 0.002]
    ok("portada dentro de y=300–1620") if not fuera else av(f"portada con contenido fuera de la zona segura en y={fuera}")


def guion(t, v2):
    if not t: return no("falta el guion")
    m = re.search(r"## Guion[^\n]*\n(.*?)(?=^## |\Z)", t, re.S | re.M)
    texto = m.group(1) if m else t
    tags = re.findall(r"\[[a-z ]+\]", texto)
    n = len(re.sub(r"\[[a-z ]+\]", " ", texto).split())
    if v2:
        (ok if 150 <= n <= 200 else av)(f"guion de {n} palabras (150 a 200 ≈ 60 a 75 s)")
        (ok if len(tags) <= 6 else av)(f"{len(tags)} Audio Tags (máx. 6, solo en giros emocionales)")
        no("el guion abre con [pause]: un video no empieza en silencio") if texto.strip().startswith("[pause]") else ok("no abre con [pause]")
    if re.search(PROHIBIDAS, texto, re.I): no("el guion tiene una frase prohibida (cura, garantiza, diagnóstico…)")


def copy(t):
    if not t: return no("falta copy.md")
    for s in ["Título", "Texto para Instagram y Facebook", "Texto para TikTok", "Hashtags", "Por confirmar con Karen"]:
        if not re.search(r"^## " + s, t, re.M): no(f"al copy le falta «{s}»")
    hueco = re.findall(r"\{[A-Z_]{3,}\}|\{[a-z][^}]{3,}\}", t)
    no(f"huecos sin llenar en el copy: {hueco[:3]}") if hueco else ok("copy sin huecos")
    ok("web en el copy") if "psicologakarentrujillo.com.mx" in t else no("falta psicologakarentrujillo.com.mx en el copy")
    ok("aviso en el copy") if "orienta y no diagnostica" in t else av("el copy no trae «Este video orienta y no diagnostica.»")
    no("frase prohibida en el copy") if re.search(PROHIBIDAS, t, re.I) else ok("sin frases prohibidas")
    if "—" in t: av("rayas largas (—) en el copy")
    ti = re.search(r"^## Título[^\n]*\n+(.+)", t, re.M)
    if ti and len(ti.group(1).strip()) > 100: no(f"título de YouTube de {len(ti.group(1).strip())} caracteres (máx. 100)")
    ht = re.search(r"^## Hashtags\n+(.+)", t, re.M)
    if ht and not all(h in ht.group(1) for h in ["#neuropsicologia", "#Cancun"]): av("faltan hashtags base (#neuropsicologia, #Cancun)")


def repo(carpetas):
    print("Repo")
    cal, tab = leer(os.path.join(RAIZ, "calendario.md")), leer(os.path.join(RAIZ, "tabla-publicacion.md"))
    web = json.load(open(os.path.join(RAIZ, "web", "data.json"), encoding="utf-8"))
    for d in carpetas:
        nom = os.path.basename(os.path.normpath(d)); nn = nom[:2]
        if not re.match(r"\d\d - ", nom): continue
        (ok if re.search(rf"^\| {nn} \| \[{re.escape(nom)}\]", cal, re.M) else no)(f"{nn} en calendario.md")
        (ok if f"| {nom}" in tab else no)(f"{nn} en tabla-publicacion.md")
        e = next((x for x in web if x["n"] == nn), None)
        (ok if e and e.get("v") and e.get("ig") else no)(f"{nn} en web/data.json (correr exportar_web.py)")
    rutas = [os.path.join(RAIZ, f) for f in sh("git", "-C", RAIZ, "ls-files", "-z").stdout.split("\0") if f]
    grandes = [r for r in rutas if os.path.exists(r) and os.path.getsize(r) > 95 * 1048576]
    no(f"archivos de más de 95 MB: {grandes}") if grandes else ok("ningún archivo pasa de 95 MB")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args: sys.exit(__doc__)
    for d in args:
        print(f"\n{os.path.basename(os.path.normpath(d))}")
        g = primero(d, "guion.md", "guion.txt"); gt = leer(g) if g else None
        ct = leer(os.path.join(d, "copy.md"))
        v2 = "v2" in d or any(x and "v2" in x[:300] for x in (gt, ct)) or os.path.exists(os.path.join(d, "voz.mp3"))
        v, p = primero(d, "video.mp4", "final.mp4"), primero(d, "portada.png")
        video(v, p, v2) if v else no("falta el video (video.mp4 o final.mp4)")
        if not p: no("falta portada.png")
        elif v2: portada_v2(p)
        guion(gt, v2); copy(ct)
    if "--repo" in sys.argv: repo(args)
    print("\nA ojo: subtítulos sin errores · ningún texto tapa al personaje · sin cuadros vacíos (vistazo) · objetos reconocibles · signos de la portada (≠, ¿?)")
    print("✗ hay fallos: corregir antes de guardar" if FALLOS else "✓ todo bien")
    sys.exit(1 if FALLOS else 0)


if __name__ == "__main__":
    main()
