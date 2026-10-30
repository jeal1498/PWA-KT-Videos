#!/usr/bin/env python3
"""Calendario, tabla de publicación y orden de subida. Se corre desde cualquier carpeta.
  calendario.py fechas [n]                  próximas n fechas libres, marcadas «sin cara» / «con Karen» (alternancia desde el sáb 31 oct 2026)
  calendario.py fila NN "Carpeta" "gancho" ["fecha"]   agrega o reemplaza la fila NN (Hecho, Publicado = No; sin fecha conserva la que tenía)
  calendario.py tabla "Carpeta"             agrega o reemplaza su fila en tabla-publicacion.md a partir de su copy.md
  calendario.py revisar                     avisa si dos videos del mismo tema caen en días seguidos
La fecha se escribe como en el calendario: «sáb 14 nov 2026 (plan)»."""
import datetime as dt, os, re, sys, urllib.parse

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *[".."] * 4))
CAL, TAB = os.path.join(RAIZ, "calendario.md"), os.path.join(RAIZ, "tabla-publicacion.md")
MESES = "ene feb mar abr may jun jul ago sep oct nov dic".split()
DIAS = "lun mar mié jue vie sáb dom".split()
INICIO_ALTERNANCIA = dt.date(2026, 10, 31)  # sin cara; al día siguiente, con Karen
URL = "https://github.com/jeal1498/PWA-KT-Videos/raw/main/"


def leer(p): return open(p, encoding="utf-8").read()
def escribir(p, t): open(p, "w", encoding="utf-8").write(t)


def fecha(txt):
    m = re.search(r"(\d{1,2})\s+(" + "|".join(MESES) + r")[a-z]*\s*(\d{4})?", txt or "")
    if not m: return None
    return dt.date(int(m.group(3) or 2026), MESES.index(m.group(2)) + 1, int(m.group(1)))


def bonita(d): return f"{DIAS[d.weekday()]} {d.day} {MESES[d.month - 1]} {d.year}"
def tipo(d): return "sin cara" if (d - INICIO_ALTERNANCIA).days % 2 == 0 else "con Karen"


def filas():
    for l in leer(CAL).splitlines():
        m = re.match(r"\|\s*(\d\d)\s*\|\s*\[([^\]]+)\]", l)
        if m: yield m.group(1), m.group(2), [x.strip() for x in l.strip().strip("|").split("|")]


def fechas(n=6):
    usadas = {fecha(c[3]) for _, _, c in filas()} - {None}
    d = dt.date.today(); out = []
    while len(out) < n:
        d += dt.timedelta(days=1)
        if d not in usadas: out.append(d)
    for d in out: print(f"{bonita(d)} (plan) · {tipo(d)}")


def fila(nn, carpeta, gancho, fe=None):
    t = leer(CAL).splitlines(keepends=True)
    viejo = next((c for n, _, c in filas() if n == nn), None)
    fe = fe or (viejo[3] if viejo else "por definir")
    nueva = f"| {nn} | [{carpeta}](./{urllib.parse.quote(carpeta)}/) | {gancho} | {fe} | Hecho | No |\n"
    t = [l for l in t if not l.startswith(f"| {nn} |")]
    i = max([k for k, l in enumerate(t) if re.match(r"\| \d\d \|", l) and l[2:4] < nn] or
            [max(k for k, l in enumerate(t) if l.startswith("|---"))]) + 1
    t.insert(i, nueva); escribir(CAL, "".join(t)); print(f"calendario: {nueva.strip()[:90]}…")


def seccion(md, titulo):
    m = re.search(r"^## " + re.escape(titulo) + r"[^\n]*\n(.*?)(?=^## |\Z)", md, re.S | re.M)
    return m.group(1).strip() if m else ""


def tabla(carpeta):
    md = leer(os.path.join(RAIZ, carpeta, "copy.md")); br = lambda s: s.replace("\n", "<br>").replace("|", "\\|")
    tags = seccion(md, "Hashtags")
    copy = (f"**Instagram/Facebook:**<br>{br(seccion(md, 'Texto para Instagram y Facebook'))}<br><br>{tags}<br><br>"
            f"**TikTok:**<br>{br(seccion(md, 'Texto para TikTok'))}<br><br>{tags}<br><br>"
            f"**YouTube Shorts (título):**<br>{br(seccion(md, 'Título'))}")
    nueva = f"| {carpeta} | [Descargar]({URL}{urllib.parse.quote(carpeta)}/video.mp4) | {copy} |\n"
    t = [l for l in leer(TAB).splitlines(keepends=True) if not l.startswith(f"| {carpeta} |")]
    i = max([k for k, l in enumerate(t) if re.match(r"\| \d\d - ", l) and l[2:4] < carpeta[:2]] or
            [max(k for k, l in enumerate(t) if l.startswith("|---"))]) + 1
    t.insert(i, nueva); escribir(TAB, "".join(t)); print(f"tabla: {carpeta}")


def revisar():
    vids = []
    for nn, carpeta, c in filas():
        d = fecha(c[3]); p = os.path.join(RAIZ, carpeta, "copy.md")
        rel = re.search(r"\|\s*Relación\s*\|\s*(.*?)\s*\|", leer(p)) if os.path.exists(p) else None
        rel = rel.group(1) if rel else ""
        base = re.search(r"(?:v2|[Vv]ersión B) del (\d\d)", rel + carpeta)
        sg = re.search(r"seguid[oa]s?\b(.*)", rel)
        evitar = set(re.findall(r"\b(\d\d)\b", sg.group(1))) if sg else set()
        if d: vids.append((d, nn, base.group(1) if base else nn, evitar))
    vids.sort(); avisos = 0
    for (d1, a, ba, ea), (d2, b, bb, eb) in zip(vids, vids[1:]):
        if (d2 - d1).days <= 1 and (ba == bb or b in ea or a in eb or bb in ea or ba in eb):
            avisos += 1; print(f"! {a} ({bonita(d1)}) y {b} ({bonita(d2)}) tratan el mismo tema y quedan seguidos")
    print("✓ ningún tema repetido en días seguidos" if not avisos else f"{avisos} aviso(s)")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    {"fechas": lambda: fechas(int(a[1]) if len(a) > 1 else 6), "fila": lambda: fila(*a[1:5]),
     "tabla": lambda: tabla(a[1]), "revisar": revisar}[a[0]]()
