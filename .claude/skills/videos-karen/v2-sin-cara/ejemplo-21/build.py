import json, html as H
AV=json.load(open('avs.json')); W=json.load(open('words.json'))
# Las escenas se escribieron con los tiempos de la voz anterior: se trasladan a la nueva con una
# interpolación por palabra (warp.json = [[t_viejo, t_nuevo], ...]); el JS hace lo mismo con cada posición.
KN=json.load(open('warp.json'))
def wp(t):
    for (a0,b0),(a1,b1) in zip(KN,KN[1:]):
        if t<=a1: return round(b0+(t-a0)*(b1-b0)/max(a1-a0,1e-6),3)
    return round(KN[-1][1]+(t-KN[-1][0]),3)
DUR=round(W[-1][2]+0.1,2)
L,R,A,D,G='#C6BCE2','#F9DEE3','#F5E7D6','#2E2545','#10b77f'
# ---- subtítulos ----
ch=[];cur=[]
def fl():
    global cur
    if cur: ch.append([' '.join(x[0] for x in cur),cur[0][1],cur[-1][2]]); cur=[]
for w in W:
    cur.append(w); n=len(' '.join(x[0] for x in cur))
    if w[0][-1] in '.?:' or (w[0][-1]==',' and n>16) or n>30: fl()
fl()
caps=[]
for i,(t,a,b) in enumerate(ch):
    nx=ch[i+1][1]-0.04 if i+1<len(ch) else DUR
    e=min(max(b+0.12,a+0.3),nx); a=max(0.02,a-0.02)
    caps.append((t,round(a,2),round(e-a,2)))
SC=[]  # (id,a,b,html)
def sc(i,a,b,body): SC.append((i,wp(a),wp(b) if b<74 else DUR,body))
def av(k,cls,style): return f'<div class="av {cls}" style="{style}">{AV[k]}</div>'
def svg(inner,txt=''): return f'<svg class="full" viewBox="0 0 1080 1920"><g filter="url(#rough)">{inner}</g>{txt}</svg>'
def chip(t,col=A,top=330): return f'<div class="chip" style="top:{top}px;background:{col}">{t}</div>'
def card(x,y,w=300,h=320,fill=A): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="34" fill="{fill}" stroke="{D}" stroke-width="8"/>'
def T(x,y,t,size=40,col=D,cls=''): return f'<text class="tx {cls}" x="{x}" y="{y}" font-size="{size}" fill="{col}">{t}</text>'

def pill(n,t): return f'<div class="pill"><b>{n}</b>{t}</div>'
def heart(cx,cy,s=1): return f'<path d="M{cx} {cy+70*s}c{-60*s}-{60*s} {-110*s}-{10*s} {-70*s} {40*s}l{70*s} {70*s} {70*s}-{70*s}c{40*s}-{50*s}-{10*s}-{100*s}-{70*s}-{40*s}z" transform="translate(0,{-60*s})" fill="{L}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/>'
def play(cx,cy,r=84): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{L}" stroke="{D}" stroke-width="8"/><path d="M{cx-r*.28} {cy-r*.48}l{r*.78} {r*.48}-{r*.78} {r*.48}z" fill="{D}" stroke="{D}" stroke-width="6" stroke-linejoin="round"/>'
# 1 gancho
sc('s1',0,6.6, chip('Neuropsicóloga Karen Trujillo · Cédula 11009616',A,300).replace('class="chip"','class="chip ced"')+
 '<div class="t" style="top:390px;font-size:92px"><span class="w">«Si</span> <span class="w">de</span> <span class="w">verdad</span> <span class="w">quisieras,</span> <span class="w">ya</span> <span class="w">lo</span> <span class="w">habrías</span> <span class="st w">hecho.»</span></div>'+
 av('preocupada','a1','left:290px;top:790px;width:480px;height:480px')+
 '<div class="q" style="top:1290px;font-size:72px">Termina <span class="st">creyéndolo</span></div>')
# 2 querer / arrancar
sc('s2',6.7,9.6, svg(f'<g class="c1"><rect x="70" y="800" width="400" height="400" rx="48" fill="{R}" stroke="{D}" stroke-width="8"/>{heart(270,970)}</g>'
 f'<g class="c2"><rect x="610" y="800" width="400" height="400" rx="48" fill="{A}" stroke="{D}" stroke-width="8"/>{play(810,1000)}</g>'
 f'<g class="ne"><path d="M505 960h70M505 1040h70" stroke="{A}" stroke-width="16" stroke-linecap="round"/><path d="M515 1090L565 920" stroke="{R}" stroke-width="16" stroke-linecap="round"/></g>',
 T(270,1260,'querer',56,'#fff','l1')+T(810,1260,'arrancar',56,'#fff','l2'))+
 '<div class="q" style="top:1330px;font-size:70px">No son lo <span class="st">mismo</span></div>')
# 3 dificultad
ic1=f'<path d="M150 900v110M150 900h90l-24 26 24 26h-90" fill="{R}" stroke="{D}" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>'
ic2=f'<circle cx="540" cy="940" r="56" fill="{R}" stroke="{D}" stroke-width="8"/><circle cx="540" cy="940" r="28" fill="{A}" stroke="{D}" stroke-width="8"/><circle cx="540" cy="940" r="9" fill="{D}"/>'
ic3=f'<path d="M810 1000h60v-50h60v-50h60" fill="none" stroke="{D}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
sc('s3',9.7,17.9, chip('En el TDAH',R)+'<div class="t" style="top:430px">Cuesta <span class="st">empezar</span></div>'+
 svg(f'<g class="k1">{card(60,740,300,330)}{ic1}</g><g class="k2">{card(390,740,300,330)}{ic2}</g><g class="k3">{card(720,740,300,330)}{ic3}</g>'
 f'<rect x="120" y="1190" width="840" height="64" rx="32" fill="{L}" fill-opacity=".35" stroke="{D}" stroke-width="7"/><rect id="gn" x="120" y="1190" width="840" height="64" rx="32" fill="{G}" stroke="{D}" stroke-width="7"/>',
 T(210,1030,'Empezar',38,D,'l1')+T(540,1030,'Atención',38,D,'l2')+T(870,1030,'Los pasos',36,D,'l3')+T(540,1320,'ganas',44,'#fff','gl'))+
 '<div class="cap2" style="top:1340px;font-size:44px;opacity:0" id="gcap"></div>')
# 4 esfuerzo
sc('s4',18.0,24.0, '<div class="t" style="top:430px">Se esfuerza <span class="st">muchísimo</span></div>'+
 av('cansada','aT','left:300px;top:640px;width:460px;height:460px')+
 svg(f'<rect x="90" y="1190" width="900" height="60" rx="30" fill="{L}" fill-opacity=".3" stroke="{D}" stroke-width="7"/><rect id="ef" x="90" y="1190" width="900" height="60" rx="30" fill="{G}" stroke="{D}" stroke-width="7"/>'
     f'<rect x="90" y="1300" width="900" height="60" rx="30" fill="{R}" fill-opacity=".3" stroke="{D}" stroke-width="7"/><rect id="rs" x="90" y="1300" width="420" height="60" rx="30" fill="{R}" stroke="{D}" stroke-width="7"/>',
 T(540,1178,'esfuerzo',38,'#fff','e1')+T(540,1288,'resultado',38,'#fff','e2')))
# 5 pregunta
sc('s5',24.2,31.9, chip('Cambia la pregunta')+
 svg(f'<g class="b1"><rect x="80" y="720" width="920" height="170" rx="46" fill="{L}" stroke="{D}" stroke-width="8"/></g><path id="stk" d="M170 806H910" stroke="{D}" stroke-width="12" stroke-linecap="round"/>'
     f'<path id="dn" d="M540 920v90m-34-34l34 34 34-34" fill="none" stroke="{R}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
     f'<g class="b2"><rect x="80" y="1050" width="920" height="250" rx="46" fill="{A}" stroke="{D}" stroke-width="8"/></g>',
 T(540,822,'¿Por qué no lo hago?',56,D,'p1')+T(540,1150,'¿Qué parte me',64,D,'p2')+T(540,1235,'está costando?',64,D,'p2')))
# 6 paso diminuto
sc('s6',32.0,38.8, '<div class="t" style="top:430px">Un primer paso <span class="st">diminuto</span></div>'+
 svg(f'<g class="big"><rect x="70" y="800" width="450" height="360" rx="40" fill="{L}" fill-opacity=".5" stroke="{D}" stroke-width="8" stroke-dasharray="22 14"/></g>'
     f'<g class="sml"><rect x="620" y="1040" width="380" height="120" rx="34" fill="{A}" stroke="{D}" stroke-width="8"/><circle cx="960" cy="1030" r="34" fill="{G}" stroke="{D}" stroke-width="6"/><path d="M946 1030l10 10 18-22" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>'
     f'<path id="sta" d="M530 1000q50-70 100 0" fill="none" stroke="{R}" stroke-width="10" stroke-linecap="round" stroke-dasharray="2 18"/>',
 T(295,960,'limpiar',52,'#fff','bg')+T(295,1030,'la casa',52,'#fff','bg')+T(810,1112,'sacar la basura',38,D,'sm')))
# 7 convives
sc('s7',38.9,48.7, chip('Si convives con alguien así')+'<div class="t" style="top:430px">En lugar de <span class="st">exigir</span></div>'+
 svg(f'<g class="ex"><rect x="80" y="760" width="920" height="170" rx="56" fill="{R}" stroke="{D}" stroke-width="8"/></g>'
     f'<g class="bub"><rect x="80" y="760" width="920" height="170" rx="56" fill="{A}" stroke="{D}" stroke-width="8"/><path d="M200 928l-30 60 90-50z" fill="{A}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/></g>'
     f'<g class="co"><circle cx="270" cy="1130" r="38" fill="{L}" stroke="{D}" stroke-width="7"/><circle cx="370" cy="1130" r="38" fill="{R}" stroke="{D}" stroke-width="7"/><path d="M220 1220q50-60 100 0M320 1220q50-60 100 0" fill="none" stroke="{D}" stroke-width="8" stroke-linecap="round"/></g>'
     f'<g class="re"><path d="M730 1220q0-90 80-100 80 10 80 100z" fill="{A}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/><circle cx="810" cy="1240" r="18" fill="{D}"/></g>',
 T(540,870,'¡Hazlo ya!',60,D,'et')+T(540,870,'¿Cómo te ayudo a empezar?',52,D,'bt')+T(320,1290,'compañía',42,'#fff','x1')+T(810,1310,'recordatorio',42,'#fff','x2')))
# 8 ojo
def ic8(x,k):
    if k=='ca': return f'<g class="i3"><rect x="{x-75}" y="1130" width="140" height="80" rx="14" fill="{R}" stroke="{D}" stroke-width="8"/><rect x="{x+65}" y="1154" width="16" height="32" rx="5" fill="{D}"/><rect x="{x-63}" y="1142" width="34" height="56" rx="6" fill="{L}"/></g>'
    if k=='tr': return f'<g class="i4"><circle cx="{x}" cy="1170" r="64" fill="{L}" stroke="{D}" stroke-width="8"/><circle cx="{x-22}" cy="1155" r="7" fill="{D}"/><circle cx="{x+22}" cy="1155" r="7" fill="{D}"/><path d="M{x-24} 1200q24-26 48 0" fill="none" stroke="{D}" stroke-width="7" stroke-linecap="round"/><path d="M{x+36} 1180q8 20 0 30q-8-10 0-30z" fill="{R}"/></g>'
    return f'<g class="i5"><circle cx="{x}" cy="1170" r="64" fill="{A}" stroke="{D}" stroke-width="8"/><path d="M{x-34} 1170l14-18 14 36 14-36 14 36 14-18" fill="none" stroke="{D}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>'
sc('s8',48.8,60.1, chip('Ojo')+'<div class="t" style="top:430px;font-size:84px">No toda <span class="st">procrastinación</span> es TDAH</div>'+
 av('dudosa','aD','left:300px;top:640px;width:440px;height:440px')+svg(ic8(210,'ca')+ic8(540,'tr')+ic8(870,'es'),T(210,1280,'cansancio',38,'#fff','lb3')+T(540,1280,'tristeza',38,'#fff','lb4')+T(870,1280,'estrés',38,'#fff','lb5'))+
 '<div class="q" style="top:1340px;font-size:62px">Valoración <span class="st">clínica</span></div>')
# 9 balanza
sc('s9',60.2,66.6, '<div class="t" style="top:430px;font-size:84px">Comprender no te quita <span class="st">responsabilidad</span></div>'+
 svg(f'<path d="M540 1000v200M440 1200h200" stroke="{L}" stroke-width="14" stroke-linecap="round"/><g id="beam"><path d="M180 900H900" stroke="{L}" stroke-width="14" stroke-linecap="round"/><circle cx="540" cy="900" r="22" fill="{A}" stroke="{D}" stroke-width="7"/>'
     f'<path d="M230 900v90M330 900v90M230 990h100" stroke="{D}" stroke-width="6" fill="none"/><g class="pl"><rect x="130" y="990" width="300" height="100" rx="34" fill="{A}" stroke="{D}" stroke-width="8"/></g>'
     f'<g class="pr"><rect x="650" y="990" width="300" height="100" rx="34" fill="{R}" stroke="{D}" stroke-width="8"/></g></g>',
 T(280,1052,'responsabilidad',30,D,'tl')+T(800,1052,'herramientas',32,D,'tr'))+
 '<div class="q" style="top:1290px;font-size:78px">Y menos <span class="st">culpa</span></div>')
# 10 cierre
sc('s10',66.7,DUR, '<div class="t" style="top:360px;text-align:center;font-size:80px">Este video <span class="st">orienta</span> y no diagnostica.</div>'+
 '<div class="q2" style="top:620px">Compártelo con alguien que necesite escucharlo</div>'+
 svg(f'<path class="sh" d="M540 930L300 1060M540 930L780 1060" stroke="{L}" stroke-width="10" stroke-linecap="round"/>'+''.join(f'<circle class="sn" cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="{D}" stroke-width="8"/>' for x,y,r,c in ((540,930,64,A),(300,1060,52,L),(780,1060,52,R))))+
 av('sonrisa','cz','left:405px;top:1110px;width:270px;height:270px')+
 '<div class="web" style="top:1395px">psicologakarentrujillo.com.mx</div>')
BOUND=[6.65,9.65,17.95,24.1,31.95,38.85,48.75,60.15,66.65]
css=f'''@font-face{{font-family:"Outfit";src:url("fonts/Outfit-700-latin.woff2") format("woff2");font-weight:500 700;font-display:block}}
@font-face{{font-family:"Maven Pro";src:url("fonts/MavenPro-700-latin.woff2") format("woff2");font-weight:400 700;font-display:block}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#000}}
#root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:{D};font-family:"Maven Pro",sans-serif;color:#fff}}
#cam{{position:absolute;inset:0}}.lay{{position:absolute;inset:0}}
#glow{{background:radial-gradient(660px 660px at 540px 920px,rgba(107,95,138,.55),rgba(46,37,69,0) 70%)}}
#vig{{background:radial-gradient(900px 1200px at 540px 900px,rgba(0,0,0,0) 45%,rgba(16,11,28,.5) 100%)}}
svg.full{{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible}}
.sc{{position:absolute;inset:0}}
.av{{position:absolute}}.av svg{{width:100%;height:100%}}
.tx{{font-family:"Outfit";font-weight:700;text-anchor:middle}}.tx.left{{text-anchor:start}}
.t{{position:absolute;left:60px;right:60px;font:700 96px/1.16 "Outfit",sans-serif;letter-spacing:-.02em}}
.st{{display:inline-block;background:{A};color:{D};padding:0 20px;border-radius:22px;box-shadow:7px 8px 0 {L};transform:rotate(-2.5deg)}}
.w{{display:inline-block}}
.chip{{position:absolute;left:60px;color:{D};font:700 32px/1 "Maven Pro";letter-spacing:.1em;text-transform:uppercase;padding:15px 26px;border-radius:40px;border:5px solid {D};box-shadow:5px 6px 0 rgba(198,188,226,.6)}}
.chip.ced{{font-size:26px;letter-spacing:.04em;text-transform:none;padding:12px 22px}}
.pill{{position:absolute;left:60px;top:340px;display:flex;align-items:center;gap:20px;font:700 66px/1 "Outfit"}}
.pill b{{display:grid;place-items:center;width:96px;height:96px;border-radius:50%;background:{L};color:{D};border:6px solid {D};box-shadow:5px 6px 0 {R};font:700 56px/1 "Outfit"}}
.q{{position:absolute;left:50px;right:50px;text-align:center;font:700 84px/1.18 "Outfit";letter-spacing:-.02em}}
.q2{{position:absolute;left:60px;right:60px;text-align:center;font:700 64px/1.2 "Outfit"}}
.cap2{{position:absolute;left:60px;right:60px;text-align:center;font:700 50px/1.2 "Outfit";color:{L}}}
.web{{position:absolute;left:0;right:0;top:1345px;text-align:center;font:700 40px "Maven Pro";color:{L}}}
#tr{{position:absolute;left:0;top:0;width:1080px;height:1920px;pointer-events:none}}
.cap{{position:absolute;left:60px;right:60px;top:1460px;text-align:center}}
.plate{{display:inline;background:rgba(46,37,69,.9);color:#fff;font:700 54px/1.42 "Maven Pro",sans-serif;padding:6px 22px;border-radius:18px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}'''
doodles=f'''<svg class="full" viewBox="0 0 1080 1920"><defs><filter id="rough" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence id="turb" type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="1" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="6" xChannelSelector="R" yChannelSelector="G"/></filter></defs>
<g filter="url(#rough)"><g fill="{L}"><path class="sp" d="M120 600l10 26 26 10-26 10-10 26-10-26-26-10 26-10z"/><path class="sp" d="M960 700l8 20 20 8-20 8-8 20-8-20-20-8 20-8z"/><path class="sp" d="M100 1260l7 17 17 7-17 7-7 17-7-17-17-7 17-7z"/><path class="sp" d="M985 1230l9 22 22 9-22 9-9 22-9-22-22-9 22-9z"/></g>
<path class="sq" d="M840 250q20-24 40 0t40 0t40 0" fill="none" stroke="{R}" stroke-width="7" stroke-linecap="round"/><path class="sq" d="M90 260q20-24 40 0t40 0" fill="none" stroke="{L}" stroke-width="7" stroke-linecap="round"/></g></svg>'''
trsvg=f'<svg id="tr" viewBox="0 0 1080 1920"><g filter="url(#rough)"><line id="trl" x1="-40" y1="1380" x2="-40" y2="1380" stroke="{L}" stroke-width="12" stroke-linecap="round" opacity="0"/><circle id="trn" cx="-40" cy="1380" r="26" fill="{A}" stroke="{D}" stroke-width="7" opacity="0"/></g></svg>'
body=''.join(f'<div class="sc clip" id="{i}" data-start="{a}" data-duration="{round(b-a,2)}" data-track-index="1">{h}</div>' for i,a,b,h in SC)
capsh=''.join(f'<div class="cap clip" id="cap{k}" data-start="{a}" data-duration="{d}" data-track-index="5"><span class="plate">{H.escape(t)}</span></div>' for k,(t,a,d) in enumerate(caps))
js=open('anim.js').read().replace('__KN__',json.dumps(KN)).replace('__DUR__',str(DUR)).replace('__BOUND__',json.dumps(BOUND)).replace('__NCAP__',str(len(caps))).replace('__CAPS__',json.dumps([[a] for _,a,_ in caps]))
doc=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=1080, height=1920"><style>{css}</style></head><body>
<div id="root" data-composition-id="kt21full" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920" data-fps="30">
<div id="cam"><div class="lay" id="glow"></div>{doodles}{body}<div class="lay" id="vig"></div></div>{trsvg}{capsh}
<script src="gsap.min.js"></script><script>(function(){{{js}}})();</script></div></body></html>'''
open('public/index.html','w').write(doc); print(len(SC),'escenas',len(caps),'subtítulos')
