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
def sc(i,a,b,body): SC.append((i,wp(a),wp(b) if b<79 else DUR,body))
def av(k,cls,style): return f'<div class="av {cls}" style="{style}">{AV[k]}</div>'
def svg(inner,txt=''): return f'<svg class="full" viewBox="0 0 1080 1920"><g filter="url(#rough)">{inner}</g>{txt}</svg>'
def chip(t,col=A,top=330): return f'<div class="chip" style="top:{top}px;background:{col}">{t}</div>'
def card(x,y,w=300,h=320,fill=A): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="34" fill="{fill}" stroke="{D}" stroke-width="8"/>'
def T(x,y,t,size=40,col=D,cls=''): return f'<text class="tx {cls}" x="{x}" y="{y}" font-size="{size}" fill="{col}">{t}</text>'

def pill(n,t): return f'<div class="pill"><b>{n}</b>{t}</div>'
def clock(cx,cy,r,cls='',hands=True):
    h=f'<line class="hm" x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy-r*0.65}" stroke="{D}" stroke-width="{max(r//14,5)}" stroke-linecap="round"/><line class="hh" x1="{cx}" y1="{cy}" x2="{cx+r*0.4}" y2="{cy+r*0.25}" stroke="{D}" stroke-width="{max(r//11,6)}" stroke-linecap="round"/>' if hands else ''
    return f'<g class="{cls}"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{A}" stroke="{D}" stroke-width="8"/>'+''.join(f'<line x1="{cx+dx*r*.78}" y1="{cy+dy*r*.78}" x2="{cx+dx*r*.9}" y2="{cy+dy*r*.9}" stroke="{D}" stroke-width="7" stroke-linecap="round"/>' for dx,dy in ((0,-1),(0,1),(-1,0),(1,0)))+h+f'<circle cx="{cx}" cy="{cy}" r="{max(r//10,8)}" fill="{D}"/></g>'
# 1 gancho
sc('s1',0,4.6, chip('Neuropsicóloga Karen Trujillo · Cédula 11009616',A,300).replace('class="chip"','class="chip ced"')+
 '<div class="t" style="top:390px;font-size:104px"><span class="w">«Solo</span> <span class="w">voy</span> <span class="w">a</span> <span class="w">revisar</span> <span class="w">un</span> <span class="st w">mensaje»</span></div>'+
 svg(f'<g class="ph"><rect x="620" y="840" width="230" height="380" rx="40" fill="{L}" stroke="{D}" stroke-width="8"/><rect x="642" y="880" width="186" height="280" rx="22" fill="{R}"/><rect x="665" y="915" width="140" height="44" rx="22" fill="{D}"/><rect x="665" y="980" width="100" height="44" rx="22" fill="{L}"/></g>'
     f'<g class="bd"><circle cx="845" cy="850" r="34" fill="{G}" stroke="{D}" stroke-width="6"/></g>'+clock(750,1330,96,'ck1')+
     f'<rect class="p10" x="470" y="1280" width="150" height="56" rx="28" fill="{L}" stroke="{D}" stroke-width="6"/><rect class="p1h" x="470" y="1280" width="150" height="56" rx="28" fill="{A}" stroke="{D}" stroke-width="6"/>',
     T(845,864,'1',40,'#fff','bdt')+T(545,1320,'10 min',34,D,'t10')+T(545,1320,'1 hora',34,D,'t1h'))+
 av('sorprendida','a1','left:40px;top:830px;width:500px;height:500px'))
# 2 escurrió
sc('s2',4.7,8.2, '<div class="t" style="top:430px">No fue falta de <span class="st">ganas</span></div>'+
 svg(clock(800,980,170,'ck2')+''.join(f'<path class="dr" d="M{x} {y}q-16 34 0 50q16-16 0-50z" fill="{c}" stroke="{D}" stroke-width="5"/>' for x,y,c in ((700,1150,L),(810,1160,R),(900,1140,L)))+
     f'<path class="sand" d="M620 1330q180-60 360 0z" fill="{R}" stroke="{D}" stroke-width="7"/>')+
 av('cansada','aT','left:20px;top:760px;width:500px;height:500px')+
 '<div class="q" style="top:1310px;font-size:76px">El tiempo se <span class="st">escurrió</span></div>')
# 3 ahora / no ahora
sc('s3',8.3,12.9, chip('Con TDAH',R)+'<div class="t" style="top:430px">El tiempo suele sentirse <span class="st">así</span></div>'+
 svg(f'<g class="n1"><rect x="70" y="800" width="430" height="360" rx="40" fill="{A}" stroke="{D}" stroke-width="8"/><circle cx="285" cy="940" r="62" fill="{R}" stroke="{D}" stroke-width="8"/><g stroke="{D}" stroke-width="8" stroke-linecap="round"><path d="M285 840v-24M285 1040v24M185 940h-24M385 940h24M215 870l-16-16M355 1010l16 16M355 870l16-16M215 1010l-16 16"/></g></g>'
     f'<g class="n2"><rect x="580" y="800" width="430" height="360" rx="40" fill="{L}" fill-opacity=".45" stroke="{D}" stroke-width="8" stroke-dasharray="22 16"/><path d="M810 880a70 70 0 1 0 60 100a56 56 0 0 1-60-100z" fill="{L}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/></g>',
     T(285,1110,'ahora',58,D,'l1')+T(795,1110,'no ahora',58,D,'l2')))
# 4 calcular / cambiar
sc('s4',13.0,18.9, chip('Cuesta más')+
 svg(f'<g class="c1"><rect x="60" y="720" width="450" height="400" rx="40" fill="{A}" stroke="{D}" stroke-width="8"/>'+clock(285,880,80,'',False).replace(f'<circle cx="285" cy="880" r="10" fill="{D}"/>','')+f'<line x1="285" y1="880" x2="285" y2="830" stroke="{D}" stroke-width="9" stroke-linecap="round"/><line x1="285" y1="880" x2="325" y2="900" stroke="{D}" stroke-width="9" stroke-linecap="round"/><circle cx="285" cy="880" r="9" fill="{D}"/><circle cx="410" cy="780" r="38" fill="{R}" stroke="{D}" stroke-width="7"/></g>'
     f'<g class="c2"><rect x="570" y="720" width="450" height="400" rx="40" fill="{A}" stroke="{D}" stroke-width="8"/><rect x="610" y="840" width="120" height="120" rx="24" fill="{L}" stroke="{D}" stroke-width="7"/><rect x="860" y="840" width="120" height="120" rx="24" fill="{R}" stroke="{D}" stroke-width="7"/><path id="jmp" d="M735 880q60-80 120 0" fill="none" stroke="{D}" stroke-width="9" stroke-linecap="round" stroke-dasharray="2 18"/><path d="M835 852l22 28-34 8" fill="none" stroke="{D}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></g>',
     T(410,794,'?',46,D,'qm')+T(285,1070,'Calcular cuánto tarda',32,D,'l1')+T(795,1070,'Pasar a otra actividad',32,D,'l2'))+
 '<div class="q" style="top:1200px">Cuesta <span class="st">más</span></div>')
# 5 impuntual
sc('s5',19.0,22.9, '<div class="t" style="top:430px">Llegas <span class="st">corriendo</span></div>'+
 svg(clock(880,830,86,'ck5'))+
 av('agobiada','aG','left:240px;top:660px;width:600px;height:600px')+
 '<div class="q" style="top:1330px;font-size:76px">Y te dices <span class="st">impuntual</span></div>')
# 6 tres ideas
sc('s6',23.0,24.9, '<div class="t" style="top:560px;text-align:center;font-size:160px">3 <span class="st">ideas</span></div>'+
 svg(f'<path id="p3l" d="M240 1020C390 980 690 1060 840 1020" fill="none" stroke="{L}" stroke-width="10" stroke-linecap="round" stroke-dasharray="4 22"/>'+
     ''.join(f'<circle class="pn" cx="{x}" cy="1020" r="66" fill="{c}" stroke="{D}" stroke-width="8"/>' for x,c in ((240,L),(540,R),(840,A))),
     ''.join(T(x,1044,n,64,D,'pnt') for x,n in ((240,'1'),(540,'2'),(840,'3')))))
# 7 mide
rowsy=(900,1020,1140); nm=('Bañarte','Vestirte','Salir')
tab=''.join(f'<g class="rw{i}"><rect x="60" y="{y-46}" width="960" height="92" rx="46" fill="{A}" stroke="{D}" stroke-width="6"/><rect x="560" y="{y-34}" width="170" height="68" rx="34" fill="{L}" stroke="{D}" stroke-width="5"/><rect x="780" y="{y-34}" width="210" height="68" rx="34" fill="{R}" stroke="{D}" stroke-width="5"/></g>' for i,y in enumerate(rowsy))
tt=''.join(T(100,y+16,n,46,D,f'rt{i}').replace('class="tx','class="tx left')+T(645,y+14,c,38,D,f'rc{i}')+T(885,y+14,r,40,D,f'rr{i}') for i,(y,n,c,r) in enumerate(zip(rowsy,nm,('10 min','10 min','5 min'),('25 min','20 min','15 min'))))
sc('s7',25.0,35.4, pill(1,'Mide, no adivines')+
 svg(f'<g class="sw"><circle cx="900" cy="440" r="72" fill="{A}" stroke="{D}" stroke-width="8"/><rect x="880" y="352" width="40" height="22" rx="8" fill="{L}" stroke="{D}" stroke-width="6"/><line class="swh" x1="900" y1="440" x2="900" y2="392" stroke="{D}" stroke-width="9" stroke-linecap="round"/><circle cx="900" cy="440" r="9" fill="{D}"/></g>{tab}',
     T(645,812,'creo',36,'#fff','hd')+T(885,812,'real',36,'#fff','hd')+tt)+
 '<div class="q" style="top:1260px;font-size:64px">Casi siempre es <span class="st">más</span></div>')
# 8 hacia atrás
nx=[(880,A,'8:00'),(680,L,''),(520,L,''),(360,L,'')]
sc('s8',35.5,43.3, pill(2,'Planifica hacia atrás')+
 svg(f'<path id="tll" d="M880 960H190" fill="none" stroke="{L}" stroke-width="12" stroke-linecap="round" stroke-dasharray="4 24"/>'
     f'<path id="tla" d="M215 925l-36 35 36 35" fill="none" stroke="{L}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
     f'<circle class="g0" cx="880" cy="960" r="70" fill="{A}" stroke="{D}" stroke-width="8"/>'+''.join(f'<circle class="g{i}" cx="{x}" cy="960" r="44" fill="{L}" stroke="{D}" stroke-width="7"/>' for i,x in ((1,680),(2,520),(3,360)))+
     f'<g class="mg"><rect x="60" y="900" width="240" height="120" rx="40" fill="{R}" stroke="{D}" stroke-width="8" stroke-dasharray="20 12"/></g>',
     T(880,978,'8:00',44,D,'tp')+''.join(T(x,1090,'paso',34,D,f'tq{i}') for i,x in ((1,680),(2,520),(3,360)))+T(180,1090,'margen',36,D,'tm'))+
 '<div class="q" style="top:1230px">Calcula <span class="st">hacia atrás</span></div>')
# 9 sonido
def bell(x,cls): return f'<g class="{cls}"><g class="bl" style="transform-origin:{x}px 820px"><path d="M{x-80} 960q0-120 80-140q80 20 80 140z" fill="{A}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/><rect x="{x-96}" y="958" width="192" height="26" rx="13" fill="{L}" stroke="{D}" stroke-width="7"/><circle cx="{x}" cy="1008" r="20" fill="{D}"/><circle cx="{x}" cy="812" r="14" fill="{D}"/></g></g>'
sc('s9',43.4,51.0, pill(3,'Ponle sonido al tiempo')+
 svg(bell(290,'b1')+bell(790,'b2')+f'<path id="bl3" d="M420 900C500 860 580 860 660 900" fill="none" stroke="{L}" stroke-width="10" stroke-linecap="round" stroke-dasharray="4 20"/>'+
     ''.join(f'<path class="rg{k}" d="M{x+sx*110} {y}q{sx*26} 34 0 68" fill="none" stroke="{R}" stroke-width="8" stroke-linecap="round"/>' for k,(x,sx,y) in enumerate(((290,-1,880),(290,1,880),(790,-1,880),(790,1,880)))),
     T(290,1130,'al empezar',44,D,'x1')+T(790,1118,'10 min antes',42,D,'x2')+T(790,1166,'de cambiar',42,D,'x2'))+
 '<div class="q" style="top:1260px;font-size:70px">Una alarma <span class="st">al empezar</span></div>')
# 10 ojo
def ico(x,k):
    if k=='ca': return f'<g class="i3"><rect x="{x-70}" y="1210" width="130" height="76" rx="14" fill="{R}" stroke="{D}" stroke-width="8"/><rect x="{x+60}" y="1232" width="16" height="32" rx="5" fill="{D}"/><rect x="{x-58}" y="1222" width="34" height="52" rx="6" fill="{L}"/></g>'
    if k=='es': return f'<g class="i4"><path d="M{x-80} 1290c-46 2-64-46-22-64-4-44 52-70 86-44 20-40 90-40 108 4 40-12 78 24 56 62-8 12-20 20-34 20z" fill="{L}" stroke="{D}" stroke-width="8"/></g>'
    return f'<g class="i5"><path d="M{x+10} 1210a70 70 0 1 0 56 108a56 56 0 0 1-56-108z" fill="{A}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/></g>'
sc('s10',51.1,61.2, chip('Ojo')+'<div class="t" style="top:430px">No siempre es <span class="st">TDAH</span></div>'+
 av('dudosa','aD','left:290px;top:600px;width:500px;height:500px')+
 svg(ico(210,'ca')+ico(540,'es')+ico(870,'su'),T(210,1360,'cansancio',38,D,'lb3')+T(540,1360,'estrés',38,D,'lb4')+T(870,1360,'sueño',38,D,'lb5')))
# 11 sistema
sc('s11',61.3,67.0, '<div class="t" style="top:430px">No se trata de ser <span class="st">perfecto</span></div>'+
 av('tranquila','aQ','left:240px;top:640px;width:600px;height:600px')+
 '<div class="q" style="top:1320px;font-size:70px">Un <span class="st">sistema</span> que te ayude</div>')
# 12 evaluación
rws=''.join(f'<path class="er" d="M440 {y}h200" stroke="{D}" stroke-width="9" stroke-linecap="round" opacity=".55"/><g class="ec{i}"><circle cx="390" cy="{y}" r="26" fill="{G}" stroke="{D}" stroke-width="6"/><path d="M378 {y}l8 8 16-18" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>' for i,y in enumerate((900,1010,1120)))
sc('s12',67.1,71.1, '<div class="t tt" style="top:430px;text-align:center">Si te sigue <span class="st">costando</span></div>'+
 '<div class="chip ev" style="top:640px;left:50%;transform:translateX(-50%);background:'+L+'">Evaluación</div>'+
 svg(f'<g id="clip"><rect x="320" y="770" width="440" height="430" rx="34" fill="{A}" stroke="{D}" stroke-width="8"/><rect x="450" y="740" width="180" height="56" rx="18" fill="{R}" stroke="{D}" stroke-width="7"/></g>{rws}')+
 '<div class="cap2 ec" style="top:1250px;font-size:44px">Ordena tu historia</div>')
# 13 cierre
def opt(x,t1,t2,c,cl): return f'<g class="{cl}"><rect x="{x}" y="740" width="440" height="250" rx="40" fill="{c}" stroke="{D}" stroke-width="8"/></g>'
sc('s13',71.2,DUR, '<div class="t" style="top:360px;text-align:center;font-size:80px">Este video <span class="st">orienta</span> y no diagnostica.</div>'+
 '<div class="q2" style="top:600px">¿Qué te cuesta más?</div>'+
 svg(opt(60,'','',L,'o1')+opt(580,'','',R,'o2'),T(280,850,'Calcular',46,D,'ot1')+T(280,910,'cuánto tardas',46,D,'ot1')+T(800,850,'Soltar una',46,D,'ot2')+T(800,910,'actividad',46,D,'ot2'))+
 av('sonrisa','cz','left:390px;top:1030px;width:300px;height:300px')+
 '<div class="web">psicologakarentrujillo.com.mx</div>')
BOUND=[4.65,8.25,12.95,18.95,22.95,24.95,35.45,43.35,51.05,61.25,67.05,71.15]
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
<div id="root" data-composition-id="kt18full" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920" data-fps="30">
<div id="cam"><div class="lay" id="glow"></div>{doodles}{body}<div class="lay" id="vig"></div></div>{trsvg}{capsh}
<script src="gsap.min.js"></script><script>(function(){{{js}}})();</script></div></body></html>'''
open('public/index.html','w').write(doc); print(len(SC),'escenas',len(caps),'subtítulos')
