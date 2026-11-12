#!/usr/bin/env python3
"""Arma public/index.html (HyperFrames) para un video de Karen.
Uso: python3 componer.py <carpeta_trabajo> <spec.json>
Necesita en <carpeta_trabajo>: words.json, public/input-video.mp4, public/gsap.min.js, public/fonts/*.woff2
Escribe: public/index.html y subtitulos.json"""
import json, math, re, html, sys, os
work, specp = sys.argv[1], sys.argv[2]
SK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = json.load(open(specp)); W = json.load(open(f'{work}/words.json'))
AJ = spec.get('ajustes', {})   # {"1.16": null, "1.88": "qué"}: quitar/cambiar la palabra que empieza en ese segundo
W = [w for w in W if AJ.get(f"{w['s']:.2f}", w['t']) is not None]
for w in W: w['t'] = AJ.get(f"{w['s']:.2f}", spec.get('correcciones', {}).get(w['t'], w['t']))
FPS = 30; q = lambda x: round(round(x*FPS)/FPS, 4); esc = html.escape
norm = lambda t: re.sub(r'[.,¿?¡!«»"]', '', t).lower()
def wt(word, after=0, off=0.0):
    for w in W:
        if w['s'] >= after and norm(w['t']) == word.lower(): return w['s'] + off
    raise KeyError(f'palabra no encontrada: {word} (después de {after})')
anc = lambda a: wt(a[0], a[1], a[2] if len(a) > 2 else 0.0)
def seq(words, desde):
    # busca las palabras en orden (por posición), aunque dos empiecen en el mismo instante
    i = next(k for k, w in enumerate(W) if w['s'] >= desde); out = []
    for word in words:
        j = next((k for k in range(i, len(W)) if norm(W[k]['t']) == word.lower()), None)
        if j is None: raise KeyError(f'palabra no encontrada: {word} (después de {desde})')
        out.append(W[j]['s']); i = j + 1
    return out
# ---- subtítulos por oración, trozos balanceados ----
sents = []; cur = []
for w in W:
    cur.append(w)
    if w['t'].endswith(('.', '?')): sents.append(cur); cur = []
if cur: sents.append(cur)
KEY = {k.lower() for k in spec.get('claves', [])}
def split(ws):
    n = len(' '.join(x['t'] for x in ws)); k = max(1, math.ceil(n/47))
    if k == 1: return [ws]
    pos = []; a = 0
    for x in ws: a += len(x['t'])+1; pos.append(a)
    cuts = []
    for j in range(1, k):
        tg = n*j/k
        cuts.append(min(range(len(ws)-1), key=lambda i: abs(pos[i]-tg) - (14 if ws[i]['t'].endswith(',') else 0)) + 1)
    out = []; prev = 0
    for c in sorted(set(cuts)): out.append(ws[prev:c]); prev = c
    out.append(ws[prev:]); return [o for o in out if o]
caps = []
for s in sents:
    for g in split(s):
        caps.append({'s': g[0]['s'], 'e': g[-1]['e']+0.3, 'w': [(x['t'], norm(x['t']) in KEY) for x in g], 'ts': [x['s'] for x in g]})
for i in range(len(caps)-1): caps[i]['e'] = min(caps[i]['e'], caps[i+1]['s']-0.03)
DUR = spec['duracion']; caps[-1]['e'] = min(caps[-1]['e'], DUR-0.2)
SV = lambda d: f'<svg viewBox="0 0 24 24">{d}</svg>'
CHECK = SV('<path d="M5 12.5l4.5 4.5L19 7.5"/>'); ARROW = SV('<path d="M12 4v15m0 0l-6-6m6 6l6-6"/>')
ALARM = SV('<circle cx="12" cy="13" r="7.5"/><path d="M12 9v4.2l2.8 1.8M4 5.5l3-2.4M20 5.5l-3-2.4"/>')
QUEST = SV('<circle cx="12" cy="12" r="9"/><path d="M9.5 9.2a2.7 2.7 0 015.2.9c0 1.8-2.7 2.3-2.7 4M12 17.2v.1"/>')
BOOK = SV('<path d="M6.5 3.5h11a1 1 0 011 1V21l-6.5-4.5L5.5 21V4.5a1 1 0 011-1z"/>')
words = lambda t: ''.join(f'<span class="w">{esc(x)}</span> ' for x in t.split())
H = [f'<div id="video-wrap"><video id="bg-video" src="input-video.mp4" playsinline data-has-audio="true" data-start="0" data-duration="{DUR}" data-track-index="1"></video></div>']
J = ["const tl=gsap.timeline({paused:true});", "gsap.set('#video-wrap',{transformOrigin:'50% 28%'});"]
fin = lambda sel, t, y=24, d=0.45: J.append(f"tl.fromTo('{sel}',{{opacity:0,y:{y}}},{{opacity:1,y:0,duration:{d},ease:'power2.out'}},{q(t)});")
fout = lambda sel, t, d=0.35: J.append(f"tl.to('{sel}',{{opacity:0,duration:{d},ease:'power2.in'}},{q(t)});")
shake = lambda sel, t: J.append(f"tl.fromTo('{sel}',{{rotation:-12}},{{rotation:12,duration:0.09,repeat:5,yoyo:true,ease:'sine.inOut',transformOrigin:'50% 60%'}},{q(t)});")
g = spec.get('gancho')
if g:
    H.append(f'<div class="gancho clip" id="gh" data-start="{g["ini"]}" data-duration="{round(g["fin"]-g["ini"]+0.4,2)}" data-track-index="2"><span class="gi">{QUEST}</span><b>{esc(g["texto"])}</b></div>')
    J.append(f"tl.fromTo('#gh',{{opacity:0,y:-24}},{{opacity:1,y:0,duration:0.38,ease:'power2.out'}},{g['ini']});"); fout('#gh', g['fin'])
nt = spec.get('nametag')
if nt:
    H.append(f'<div class="nametag clip" id="nt" data-start="{nt["ini"]}" data-duration="{nt["fin"]-nt["ini"]}" data-track-index="2"><i class="bar"></i><div><b>{esc(nt["nombre"])}</b><span>{esc(nt["cargo"])}</span>{'<span class="ced">Cédula profesional '+esc(nt["cedula"])+'</span>' if nt.get("cedula") else ''}</div></div>')
    J.append(f"tl.fromTo('#nt',{{opacity:0,x:-50}},{{opacity:1,x:0,duration:0.5,ease:'power3.out'}},{nt['ini']});"); fout('#nt', nt['fin']-0.4)
for pi, p in enumerate(spec.get('pastillas', []), 1):
    pid = f"p{pi}"; ic = f'<span class="ic" id="{pid}ic">{ALARM}</span>' if p.get('icono_alarma_en') else ''
    H.append(f'<div class="pill clip" id="{pid}" data-start="{p["ini"]}" data-duration="{round(p["fin"]-p["ini"]+0.5,2)}" data-track-index="2">{'<span class="n">'+str(p["n"])+'</span>' if p.get("n") else ''}{esc(p["texto"])}{ic}</div>')
    J.append(f"tl.fromTo('#{pid}',{{opacity:0,y:-20,scale:.94}},{{opacity:1,y:0,scale:1,duration:0.45,ease:'back.out(1.5)'}},{p['ini']});"); fout('#'+pid, p['fin'])
    if p.get('icono_alarma_en'):
        t = anc(p['icono_alarma_en']); shake(f'#{pid}ic', t); J.append(f"tl.to('#{pid}ic',{{rotation:0,duration:.1}},{q(t+0.6)});")
for b in spec.get('antes_despues', []):
    c = b['id']
    H.append(f'''<div class="card ba clip" id="{c}" data-start="{b['ini']}" data-duration="{round(b['fin']-b['ini']+0.5,2)}" data-track-index="3">
 <div class="row r1"><span class="tag">{esc(b.get("etiquetas",["Antes","Después"])[0])}</span><span class="tx" id="{c}-a"><span class="t">{esc(b['antes'])}</span><i class="strike"></i></span></div>
 <div class="arrow">{ARROW}</div>
 <div class="row r2"><span class="tag ok">{esc(b.get("etiquetas",["Antes","Después"])[1])}</span><span class="tx" id="{c}-d">{words(b['despues'])}</span><span class="chk">{CHECK}</span></div>
</div>''')
    ts = seq(b['despues_en'], b['despues_desde']); strike = anc(b['tachar_en']) - 0.1 if b.get('tachar_en') else 0
    fin(f'#{c}', b['ini']+0.05, 30, 0.5)
    J.append(f"tl.set('#{c} .r1,#{c} .arrow,#{c} .r2',{{opacity:0}},0);")
    fin(f'#{c} .r1', anc(b['antes_en']), 14, 0.4)
    if b.get('tachar', True):
        J.append(f"tl.fromTo('#{c} .strike',{{scaleX:0}},{{scaleX:1,duration:0.35,ease:'power2.inOut',transformOrigin:'0 50%'}},{q(strike)});")
        J.append(f"tl.to('#{c}-a .t',{{opacity:.45,duration:.3}},{q(strike)});")
        J.append(f"tl.to('#{c} .arrow',{{opacity:1,duration:.3}},{q(strike+0.3)});")
    else:
        J.append(f"tl.to('#{c} .arrow',{{opacity:1,duration:.3}},{q(ts[0]-0.45)});")
    J.append(f"tl.to('#{c} .r2',{{opacity:1,duration:.25}},{q(ts[0]-0.15)});")
    J.append(f"tl.set('#{c}-d .w',{{opacity:0,y:12}},0);")
    for k, tt in enumerate(ts): J.append(f"tl.to('#{c}-d .w:nth-child({k+1})',{{opacity:1,y:0,duration:0.28,ease:'power2.out'}},{q(tt-0.05)});")
    J.append(f"tl.fromTo('#{c} .chk',{{scale:0,opacity:0}},{{scale:1,opacity:1,duration:0.4,ease:'back.out(2)'}},{q(ts[-1]+0.5)});")
    fout(f'#{c}', b['fin'], 0.4)
for L in spec.get('listas', []):
    c = L['id']; items = ''.join(f'<span class="li" id="{c}-{k}">{esc(it["texto"])}</span>' for k, it in enumerate(L['items']))
    H.append(f'''<div class="card lista clip" id="{c}" data-start="{L['ini']}" data-duration="{round(L['fin']-L['ini']+0.5,2)}" data-track-index="3">
 <div class="lt">{esc(L['titulo'])}</div><div class="lis">{items}</div></div>''')
    fin(f'#{c}', L['ini']+0.05, 30, 0.5); J.append(f"tl.set('#{c} .li',{{opacity:0,scale:.9}},0);")
    for k, it in enumerate(L['items']): J.append(f"tl.to('#{c}-{k}',{{opacity:1,scale:1,duration:0.35,ease:'back.out(1.6)'}},{q(anc(it['en'])-0.1)});")
    fout(f'#{c}', L['fin'], 0.4)
for D in spec.get('destacados', []):
    c = D['id']
    H.append(f'<div class="card dest clip" id="{c}" data-start="{D["ini"]}" data-duration="{round(D["fin"]-D["ini"]+0.5,2)}" data-track-index="3"><i></i><p>{esc(D["texto"])}</p></div>')
    fin(f'#{c}', anc(D['en']) - 0.2, 30, 0.5); fout(f'#{c}', D['fin'], 0.4)
a = spec.get('alarma')
if a:
    H.append(f'''<div class="card alarm clip" id="al" data-start="{a['ini']}" data-duration="{round(a['fin']-a['ini']+0.4,2)}" data-track-index="3">
 <div class="al-top"><span class="ic">{ALARM}</span><span class="lab">{esc(a.get("etiqueta","Alarma"))}</span>{"<span class=\"ej\">Ejemplo</span>" if a.get("ejemplo", True) else ""}</div>
 <div class="al-main"><b class="time">{esc(a['hora'])}</b><div><div class="ttl">{esc(a['titulo'])}</div><div class="sub">{esc(a.get('detalle_antes',''))}<u>{esc(a['detalle'])}</u></div></div></div>
</div>''')
    fin('#al', a['ini']+0.05, 40, 0.5); J.append("tl.set('#al .al-top,#al .al-main',{opacity:1},0);"); shake('#al .ic', a['ini']+0.25)
    J.append(f"tl.fromTo('#al u',{{backgroundSize:'0% 3px'}},{{backgroundSize:'100% 3px',duration:0.6,ease:'power2.out'}},{q(anc(a['subrayar_en']))});"); fout('#al', a['fin'], 0.4)
c = spec.get('cierre')
if c:
    chips = ''.join(f'<span class="chip"><i>{i+1 if c.get("numerados", True) else ""}</i>{esc(t)}</span>' for i, t in enumerate(c['chips']))
    H.append(f'''<div class="card close clip" id="cl" data-start="{c['ini']}" data-duration="{round(DUR-c['ini'],2)}" data-track-index="3">
 <div class="cl-top"><span class="bm">{QUEST if c.get('icono')=='pregunta' else BOOK}</span><b{" style=\"font-size:"+str(c["titulo_tam"])+"px\"" if c.get("titulo_tam") else ""}>{esc(c['titulo'])}</b></div>
 <div class="chips">{chips}</div>
 <div class="url">{esc(c['url'])}</div>{'<div class="aviso">Este video orienta y no diagnostica.</div>' if c.get('aviso', True) else ''}
</div>''')
    fin('#cl', c['ini']+0.05, 40, 0.55); tv = anc(c['icono_en']) + 0.1
    if c.get('icono') != 'pregunta': J.append(f"tl.fromTo('#cl .bm path',{{fillOpacity:0}},{{fillOpacity:1,duration:0.5,ease:'power2.out'}},{q(tv)});")
    J.append(f"tl.fromTo('#cl .bm',{{scale:1}},{{scale:1.25,duration:0.22,yoyo:true,repeat:1,ease:'power2.inOut'}},{q(tv)});")
    J.append("tl.set('#cl .chip,#cl .url,#cl .aviso',{opacity:0},0);"); te = anc(c['chips_en'])
    for k in range(len(c['chips'])):
        tk = anc(c['chips_anclas'][k]) - 0.1 if c.get('chips_anclas') else te - 0.9 + 0.3*k
        J.append(f"tl.fromTo('#cl .chip:nth-child({k+1})',{{opacity:0,y:20}},{{opacity:1,y:0,duration:0.4,ease:'power2.out'}},{q(tk)});")
    J.append(f"tl.to('#cl .url',{{opacity:1,duration:0.5}},{q(anc(c['url_en'])-0.4)});")
    if c.get('aviso', True): J.append(f"tl.to('#cl .aviso',{{opacity:1,duration:0.5}},{q(anc(c['url_en'])+0.1)});")
# ---- escenas gráficas: sustituyen las tomas grabadas; la voz y los subtítulos no se cortan ----
SERV = {'infantil': ('#C6BCE2', 'TDAH infantil'), 'autismo': ('#F9DEE3', 'Autismo (TEA)'), 'adultos': ('#F5E7D6', 'TDAH adultos'), 'informativo': ('#E1E9EA', '')}
ICO = {'prueba': '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>',
       'informe': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/>',
       'pregunta': '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
       'atencion': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
       'escuela': '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
       'familia': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>'}
STAR = '<path d="m12 2 3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/>'
for e in spec.get('escenas', []):
    c = e['id']; ini, fin, tipo = e['ini'], e['fin'], e['tipo']
    bg, chip = SERV[e.get('servicio', 'informativo')]; chip = e.get('chip', chip)
    base = ini + 0.55; times = []; extra = []
    def part(cls, inner, t, style=''):
        k = len(times); times.append(t)
        return f'<div class="e-it {cls}" id="{c}-{k}" style="{style}">{inner}</div>'
    when = lambda it, i: anc(it['en']) - 0.1 if it.get('en') else base + 0.3*i
    body = ''
    if tipo == 'ficha':
        if chip: body += part('e-chip', esc(chip), base)
        body += part('e-h', esc(e['titulo']), base + 0.1, f"font-size:{e['titulo_tam']}px" if e.get('titulo_tam') else '')
        if e.get('icono'): body += part('e-ic', f'<svg viewBox="0 0 24 24">{ICO[e["icono"]]}</svg>', base + 0.2)
        body += part('e-dt', esc(e.get('etiqueta', 'Qué mide')), base + 0.4) + part('e-dd', esc(e['texto']), base + 0.45)
    elif tipo == 'lista':
        body += part('e-titulo', esc(e['titulo']), base)
        n = len(e['items']); y0 = 560
        for i, it in enumerate(e['items']):
            body += part('e-li', f'<i></i><span>{esc(it["texto"])}</span>', when(it, i + 1), f'top:{y0 + i*(560//max(n-1,1) if n > 1 else 0)}px')
    elif tipo == 'dividida':
        bg = '#FAFAFA'
        body += part('e-top', f'<span class="e-pil">{esc(e.get("etiqueta_mito", "Mito"))}</span><p>{esc(e["mito"])}</p>', base)
        body += part('e-bot', f'<span class="e-pil">{esc(e.get("etiqueta_realidad", "Realidad"))}</span><p>{esc(e["realidad"])}</p>', anc(e['realidad_en']) - 0.1 if e.get('realidad_en') else base + 1.2)
    elif tipo == 'proceso':
        body += part('e-titulo', esc(e['titulo']), base)
        n = len(e['pasos']); step = 740 / max(n-1, 1)
        extra.append(f'<svg class="e-it e-pl" id="{c}-ln" viewBox="0 0 20 760"><path pathLength="1" d="M10 10V750"/></svg>')
        for i, it in enumerate(e['pasos']):
            y = 530 + i*step
            body += part('e-node', '', when(it, i + 1), f'top:{y-20:.0f}px') + part('e-pas', esc(it['texto']), when(it, i + 1) + 0.05, f'top:{y-33:.0f}px')
    elif tipo == 'numero':
        body += part('e-big', esc(e['numero']), base)
        body += part('e-st', ''.join(f'<svg viewBox="0 0 24 24">{STAR}</svg>' for _ in range(e.get('estrellas', 0))), base + 0.2) if e.get('estrellas') else ''
        body += part('e-tx', esc(e['texto']), base + 0.3)
    elif tipo == 'esquema':
        POS = [(290, 520), (790, 520), (290, 1140), (790, 1140)]; cx, cy = 540, 830
        body += part('e-c', esc(e['centro']), base, f'left:{cx-260}px;top:{cy-50}px')
        extra.append('<svg class="e-it e-ln" id="%s-ln" viewBox="0 0 1080 1920">%s</svg>' % (c, ''.join(f'<path pathLength="1" d="M{cx} {cy}L{x} {y}"/>' for x, y in POS[:len(e['nodos'])])))
        for i, it in enumerate(e['nodos']):
            body += part('e-n', esc(it['texto']), when(it, i + 1), f'left:{POS[i][0]-200}px;top:{POS[i][1]-50}px')
    # las líneas van detrás de los nodos
    H.append(f'<div class="escena clip" id="{c}" data-layout-allow-occlusion style="background:{bg}" data-start="{ini}" data-duration="{round(fin-ini+0.5,2)}" data-track-index="4">{"".join(extra)}{body}</div>')
    H.append(f'<div class="barrido clip" id="{c}-sw" data-layout-allow-occlusion data-start="{ini}" data-duration="{round(fin-ini+0.5,2)}" data-track-index="4"></div>')
    # transición: una línea con nodo barre de izquierda a derecha y deja la escena a su paso; al terminar regresa igual
    J.append(f"tl.set('#{c}-sw',{{opacity:0}},0);")
    J.append(f"tl.set('#{c}-sw',{{opacity:1}},{q(ini)});")
    J.append(f"tl.fromTo('#{c}-sw',{{x:0}},{{x:1080,duration:0.38,ease:'power3.out'}},{q(ini)});")
    J.append(f"tl.fromTo('#{c}',{{clipPath:'inset(0 100% 0 0)'}},{{clipPath:'inset(0 0% 0 0)',duration:0.38,ease:'power3.out'}},{q(ini)});")
    J.append(f"tl.set('#{c}-sw',{{opacity:0}},{q(ini+0.38)});")
    J.append(f"tl.set('#{c}-sw',{{opacity:1}},{q(fin)});")
    J.append(f"tl.fromTo('#{c}-sw',{{x:1080}},{{x:0,duration:0.38,ease:'power3.in',immediateRender:false}},{q(fin)});")
    J.append(f"tl.fromTo('#{c}',{{clipPath:'inset(0 0% 0 0)'}},{{clipPath:'inset(0 100% 0 0)',duration:0.38,ease:'power3.in',immediateRender:false}},{q(fin)});")
    J.append(f"tl.set('#{c}-sw',{{opacity:0}},{q(fin+0.38)});")
    J.append(f"tl.set('#{c} .e-it',{{opacity:0,y:20}},0);")
    for k, tt in enumerate(times): J.append(f"tl.to('#{c}-{k}',{{opacity:1,y:0,duration:0.35,ease:'power2.out'}},{q(tt)});")
    if extra:
        J.append(f"tl.set('#{c}-ln',{{opacity:1,y:0}},0);")
        J.append(f"tl.fromTo('#{c}-ln path',{{strokeDashoffset:1}},{{strokeDashoffset:0,duration:0.5,ease:'power2.inOut'}},{q(base)});")

# ---- gráficos de referencia (objetos a dos tintas sobre ella, y 1050 a 1380) ----
S = 'stroke="#2E2545" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"'
REF = {
 'mochila': f'<path d="M38 22Q38 7 50 7Q62 7 62 22" fill="none" {S}/><rect x="13" y="55" width="10" height="28" rx="5" fill="#F9DEE3" {S}/><rect x="77" y="55" width="10" height="28" rx="5" fill="#F9DEE3" {S}/><path d="M22 38Q22 20 40 20H60Q78 20 78 38V86Q78 93 71 93H29Q22 93 22 86Z" fill="#C6BCE2" {S}/><rect x="30" y="56" width="40" height="29" rx="9" fill="#fff" {S}/><path d="M30 64H70M30 38Q50 32 70 38" fill="none" {S}/><circle cx="50" cy="75" r="3" fill="#2E2545"/>',
 'grifo': f'<path d="M10 20H58Q80 20 80 42V54H64V44Q64 36 56 36H10Z" fill="#C6BCE2" {S}/><path d="M30 20V9M20 9H40" fill="none" {S}/><rect x="60" y="54" width="24" height="9" rx="3" fill="#fff" {S}/><path d="M72 68Q80 80 72 87Q64 80 72 68Z" fill="#C6BCE2" {S}/><circle cx="28" cy="78" r="9" fill="#fff" {S}/><circle cx="46" cy="90" r="6" fill="#fff" {S}/><circle cx="20" cy="56" r="5" fill="#fff" {S}/>',
 'plato': f'<circle cx="50" cy="52" r="30" fill="#fff" {S}/><circle cx="50" cy="52" r="18" fill="#F9DEE3" {S}/><path d="M9 20V40Q9 46 14 46V84M14 20V40M19 20V40Q19 46 14 46" fill="none" {S}/><path d="M88 22Q78 34 82 54H88V82Z" fill="#fff" {S}/>',
 'globo': f'<path d="M14 20Q14 12 22 12H78Q86 12 86 20V58Q86 66 78 66H46L28 85V66H22Q14 66 14 58Z" fill="#C6BCE2" {S}/><circle cx="36" cy="39" r="4.5" fill="#2E2545"/><circle cx="50" cy="39" r="4.5" fill="#2E2545"/><circle cx="64" cy="39" r="4.5" fill="#2E2545"/>',
 'globo0': f'<path d="M14 20Q14 12 22 12H78Q86 12 86 20V58Q86 66 78 66H46L28 85V66H22Q14 66 14 58Z" fill="#fff" {S}/>',
 'ojo': f'<path d="M5 50Q50 6 95 50Q50 94 5 50Z" fill="#fff" {S}/><circle cx="50" cy="50" r="20" fill="#C6BCE2" {S}/><circle cx="50" cy="50" r="8" fill="#2E2545"/><circle cx="56" cy="44" r="3" fill="#fff"/>',
 'casa': f'<rect x="22" y="46" width="56" height="44" rx="4" fill="#fff" {S}/><path d="M9 50L50 12L91 50Z" fill="#F9DEE3" {S}/><rect x="42" y="62" width="16" height="28" rx="3" fill="#C6BCE2" {S}/><rect x="28" y="56" width="10" height="10" rx="2" fill="#C6BCE2" {S}/><rect x="62" y="56" width="10" height="10" rx="2" fill="#C6BCE2" {S}/>',
 'check': f'<circle cx="50" cy="50" r="38" fill="#fff" {S}/><path d="M30 52L45 67L72 34" fill="none" stroke="#10b77f" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>',
 'mascara': f'<path d="M14 26Q50 12 86 26V52Q86 82 50 94Q14 82 14 52Z" fill="#C6BCE2" {S}/><ellipse cx="34" cy="48" rx="10" ry="6" fill="#fff" {S}/><ellipse cx="66" cy="48" rx="10" ry="6" fill="#fff" {S}/><path d="M38 72Q50 80 62 72" fill="none" {S}/><path d="M20 30Q50 20 80 30" fill="none" stroke="#F9DEE3" stroke-width="3"/>',
 'amigas': f'<path d="M42 90Q42 58 66 58Q90 58 90 90Z" fill="#C6BCE2" {S}/><path d="M10 90Q10 56 34 56Q58 56 58 90Z" fill="#F9DEE3" {S}/><circle cx="66" cy="36" r="14" fill="#C6BCE2" {S}/><circle cx="34" cy="34" r="14" fill="#F9DEE3" {S}/>',
 'informe': f'<rect x="22" y="12" width="56" height="80" rx="7" fill="#fff" {S}/><rect x="38" y="6" width="24" height="12" rx="4" fill="#C6BCE2" {S}/><path d="M33 36H67M33 50H67M33 64H54" fill="none" {S}/><path d="M60 72L66 78L76 66" fill="none" stroke="#10b77f" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>',
 'bateria': f'<rect x="10" y="30" width="70" height="40" rx="9" fill="#fff" {S}/><rect x="80" y="42" width="9" height="16" rx="3" fill="#2E2545"/><rect x="16" y="36" width="12" height="28" rx="4" fill="#F9DEE3" {S}/>',
 'cerebro': f'<path d="M50 16Q36 6 24 18Q10 20 12 36Q4 48 16 58Q14 78 34 80Q44 90 50 84Z" fill="#F9DEE3" {S}/><path d="M50 16Q64 6 76 18Q90 20 88 36Q96 48 84 58Q86 78 66 80Q56 90 50 84Z" fill="#C6BCE2" {S}/><path d="M50 16V84M26 36Q36 38 38 48M74 36Q64 38 62 48M30 62Q40 60 42 70M70 62Q60 60 58 70" fill="none" {S}/>',
 'puzzle': f'<g transform="translate(4 6) scale(.9)"><path d="M16 30H40Q34 12 50 12Q66 12 60 30H84V54Q98 48 98 62Q98 76 84 70V90H16Z" fill="#C6BCE2" {S}/><circle cx="40" cy="62" r="7" fill="#F9DEE3" {S}/></g>',
 'reloj': f'<circle cx="50" cy="54" r="34" fill="#fff" {S}/><circle cx="22" cy="24" r="10" fill="#F9DEE3" {S}/><circle cx="78" cy="24" r="10" fill="#F9DEE3" {S}/><path d="M50 54V34M50 54L64 62" fill="none" {S}/><circle cx="50" cy="54" r="3" fill="#2E2545"/>',
 'celular': f'<rect x="28" y="8" width="44" height="84" rx="10" fill="#fff" {S}/><rect x="34" y="20" width="32" height="52" rx="4" fill="#C6BCE2" {S}/><circle cx="50" cy="82" r="3.5" fill="#2E2545"/><path d="M47 34L56 34L50 46L58 46L46 62L49 50L42 50Z" fill="#fff" {S}/>',
 'luna': f'<g transform="translate(8 8) scale(3.5)"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" fill="#C6BCE2" stroke="#2E2545" stroke-width="0.86" stroke-linejoin="round"/></g><circle cx="78" cy="26" r="4" fill="#F9DEE3" {S}/><circle cx="66" cy="14" r="2.5" fill="#F9DEE3" {S}/>',
 'cama': f'<rect x="8" y="34" width="10" height="50" rx="3" fill="#C6BCE2" {S}/><rect x="8" y="56" width="84" height="22" rx="6" fill="#C6BCE2" {S}/><rect x="22" y="40" width="26" height="16" rx="7" fill="#fff" {S}/><path d="M14 78V86M86 78V86" fill="none" {S}/>',
 'x': f'<circle cx="50" cy="50" r="40" fill="#F9DEE3" {S}/><path d="M32 32L68 68M68 32L32 68" fill="none" stroke="#2E2545" stroke-width="6" stroke-linecap="round"/>',
}
REFS = spec.get('referencias', [])
if REFS:
    H.append('<svg width="0" height="0" style="position:absolute"><defs><filter id="rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence id="rtb" type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="1"/><feDisplacementMap in="SourceGraphic" scale="5"/></filter></defs></svg>')
    for k in range(int(DUR*12)): J.append(f"tl.set('#rtb',{{attr:{{seed:{k%7+1}}}}},{q(k/12)});")
    for ri, r in enumerate(REFS):
        rid = f'rf{ri}'; ini = anc(r['en']) - 0.1 if r.get('en') else r['ini']; fin = r['fin']; tam = r.get('tam', 140)
        card = r.get('icono') != 'x'
        sty = f'left:{r["x"]}px;top:{r["y"]}px;width:{tam}px;height:{int(tam*1.12) if card else tam}px'
        cls = 'ref card' if card else 'ref'
        H.append(f'<div class="{cls} clip" id="{rid}" data-start="{q(ini)}" data-duration="{q(fin-ini+0.4)}" data-track-index="3" style="{sty}"><svg viewBox="0 0 100 100">{REF[r["icono"]]}</svg></div>')
        J.append(f"tl.fromTo('#{rid}',{{scale:0,rotation:{r.get('rot',-3)-14},opacity:0,transformOrigin:'50% 60%'}},{{scale:1,rotation:{r.get('rot',-3)},opacity:1,duration:0.75,ease:'elastic.out(1,0.5)'}},{q(ini)});")
        J.append(f"tl.to('#{rid}',{{scale:1.05,y:-5,duration:0.9,yoyo:true,repeat:{max(1,int((fin-ini)/0.9))},ease:'sine.inOut'}},{q(ini+0.8)});")
        J.append(f"tl.to('#{rid}',{{opacity:0,scale:0.6,duration:0.3,ease:'power2.in'}},{q(fin)});")

# ---- bloque animado a medida (escenario sobre ella; html con [[icono|id|tam]] y js de GSAP con la línea de tiempo `tl`) ----
CU = spec.get('custom')
if CU:
    def _ic(m):
        n, i, s = m.group(1), m.group(2), float(m.group(3))
        return f'<g id="{i}" class="zo"><g transform="translate({-s/2} {-s/2}) scale({s/100})">{REF[n]}</g></g>'
    body = re.sub(r'\[\[(\w+)\|(\w+)\|([\d.]+)\]\]', _ic, CU['html'])
    H.append(f'<div id="stg" class="clip" data-start="{CU["ini"]}" data-duration="{round(CU["fin"]-CU["ini"],2)}" data-track-index="3">{body}</div>')
    for k in range(int(CU['ini']*12), int(CU['fin']*12)): J.append(f"tl.set('#rtb',{{attr:{{seed:{k%7+1}}}}},{q(k/12)});")
    J.append(CU['js'])
for (t0, t1, s) in spec.get('zooms', []): J.append(f"tl.to('#video-wrap',{{scale:{s},duration:{q(t1-t0)},ease:'power2.inOut'}},{t0});")
for i, cp in enumerate(caps):
    if spec.get('subs_palabra'):   # palabra por palabra, sincronizada con la voz, con rebote
        inner = ' '.join(f'<span class="pw{" k" if k else ""}" id="c{i}w{j}">{esc(t)}</span>' for j, (t, k) in enumerate(cp['w']))
        H.append(f'<div class="cap capw clip" id="cap{i}" data-start="{q(cp["s"])}" data-duration="{q(cp["e"]-cp["s"])}" data-track-index="5">{inner}</div>')
        J.append(f"tl.set('#cap{i} .pw',{{opacity:0,scale:0.4,y:12,transformOrigin:'50% 80%'}},0);")
        for j, ts in enumerate(cp['ts']): J.append(f"tl.to('#c{i}w{j}',{{opacity:1,scale:1,y:0,duration:0.32,ease:'back.out(3.2)'}},{q(ts)});")
        continue
    inner = ' '.join(f'<em>{esc(t)}</em>' if k else esc(t) for t, k in cp['w'])
    H.append(f'<div class="cap clip" id="cap{i}" data-start="{q(cp["s"])}" data-duration="{q(cp["e"]-cp["s"])}" data-track-index="5"><span class="plate">{inner}</span></div>')
    J.append(f"tl.fromTo('#cap{i} .plate',{{opacity:0,y:14}},{{opacity:1,y:0,duration:0.18,ease:'power2.out'}},{q(cp['s'])});")
J.append(f"window.__timelines=window.__timelines||{{}};window.__timelines['{spec['id']}']=tl;")
css = open(f'{SK}/plantillas/estilo.css').read()
if spec.get('layout') == 'split':   # gráficos arriba, ella abajo; subtítulos sobre la costura (y≈900)
    css += '#root{background:radial-gradient(ellipse at 50% 30%,#433860 0%,#2E2545 70%)}#video-wrap{top:900px;height:1020px}#video-wrap video{object-position:50% 30%}.cap{top:850px}#stg{top:440px!important}.card{top:500px}'

doc = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=1080, height=1920">
<style>
@font-face{{font-family:"Outfit";src:url("fonts/Outfit-700-latin.woff2") format("woff2");font-weight:500 700;font-display:block}}
@font-face{{font-family:"Maven Pro";src:url("fonts/MavenPro-700-latin.woff2") format("woff2");font-weight:400 700;font-display:block}}
{css}
</style></head><body>
<div id="root" data-composition-id="{spec['id']}" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920" data-fps="30">
{chr(10).join(H)}
<script src="gsap.min.js"></script>
<script>(function(){{
{chr(10).join(J)}
}})();</script>
</div></body></html>'''
open(f'{work}/public/index.html', 'w').write(doc)
json.dump([{'ini': round(c['s'], 2), 'fin': round(c['e'], 2), 'texto': ' '.join(t for t, _ in c['w'])} for c in caps], open(f'{work}/subtitulos.json', 'w'), ensure_ascii=False, indent=1)
print(len(caps), 'subtítulos →', f'{work}/public/index.html')
