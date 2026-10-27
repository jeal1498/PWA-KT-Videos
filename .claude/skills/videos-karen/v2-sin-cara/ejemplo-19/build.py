import json, html as H
AV=json.load(open('avs.json')); W=json.load(open('words.json'))
DUR=75.6
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
def sc(i,a,b,body): SC.append((i,a,b,body))
def av(k,cls,style): return f'<div class="av {cls}" style="{style}">{AV[k]}</div>'
def svg(inner,txt=''): return f'<svg class="full" viewBox="0 0 1080 1920"><g filter="url(#rough)">{inner}</g>{txt}</svg>'
def chip(t,col=A,top=330): return f'<div class="chip" style="top:{top}px;background:{col}">{t}</div>'
def card(x,y,w=300,h=320,fill=A): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="34" fill="{fill}" stroke="{D}" stroke-width="8"/>'
def T(x,y,t,size=40,col=D,cls=''): return f'<text class="tx {cls}" x="{x}" y="{y}" font-size="{size}" fill="{col}">{t}</text>'

# 1 gancho
sc('s1',0,4.65, chip('Neuropsicóloga Karen Trujillo · Cédula 11009616',A,300).replace('class="chip"','class="chip ced"')+
 '<div class="t" style="top:390px;font-size:100px"><span class="w">Años</span> <span class="w">diciendo</span> <span class="st w">«tengo ansiedad»</span> <span class="w">y</span> <span class="w">algo</span> <span class="w">no</span> <span class="w">cuadra</span></div>'+
 svg(f'<circle class="qb" cx="800" cy="900" r="62" fill="{R}" stroke="{D}" stroke-width="8"/><path class="qb2" d="M760 1000q14-20 30-6" fill="none" stroke="{L}" stroke-width="8" stroke-linecap="round"/>',
     T(800,922,'?',76,D,'qbt'))+av('duda','a1','left:290px;top:800px;width:500px;height:500px'))
# 2 calmarte
sc('s2',4.7,12.45, svg(f'''<circle id="r1" cx="540" cy="960" r="300" fill="none" stroke="{L}" stroke-width="4" stroke-dasharray="26 18" opacity="0"/>
<circle id="r2" cx="540" cy="960" r="360" fill="none" stroke="{L}" stroke-width="3" stroke-dasharray="10 22" opacity="0"/>
<path id="fkL" d="M528 742C500 640 330 650 268 512" fill="none" stroke="{R}" stroke-width="13" stroke-linecap="round"/>
<path id="fkR" d="M552 742C580 640 750 650 812 512" fill="none" stroke="{L}" stroke-width="13" stroke-linecap="round"/>
<g id="cloud"><path d="M362 516c-56 4-80-62-30-88-8-62 66-96 112-62 24-58 118-62 144-4 52-26 116 14 104 70 48 10 52 80 2 86z" fill="{L}" stroke="{D}" stroke-width="8"/>
<circle class="cb" cx="468" cy="580" r="18" fill="{L}" stroke="{D}" stroke-width="6"/><circle class="cb" cx="496" cy="630" r="11" fill="{L}" stroke="{D}" stroke-width="5"/></g>
<g fill="{L}" stroke="{D}" stroke-width="5">'''+''.join(f'<circle class="bu" cx="540" cy="450" r="{r}"/>' for r in (16,12,14,10,13,9))+f'''</g>
<g id="nL"><circle cx="268" cy="510" r="78" fill="{R}" stroke="{D}" stroke-width="8"/><path id="icL" d="M268 510c0-10 14-10 14 0 0 19-29 19-29-2 0-30 44-30 44 4 0 40-60 40-60-10" fill="none" stroke="{D}" stroke-width="8" stroke-linecap="round"/></g>
<g id="nR"><circle cx="812" cy="510" r="78" fill="{A}" stroke="{D}" stroke-width="8"/><circle id="icR1" cx="812" cy="510" r="30" fill="none" stroke="{D}" stroke-width="8"/><circle id="icR2" cx="812" cy="510" r="11" fill="{D}"/></g>
<g id="lL"><rect x="168" y="350" width="200" height="56" rx="28" fill="{R}" stroke="{D}" stroke-width="6"/></g>
<g id="lR"><rect x="712" y="350" width="200" height="56" rx="28" fill="{A}" stroke="{D}" stroke-width="6"/></g>''',
 T(540,476,'tengo ansiedad',46,D,'clT')+T(268,390,'con miedo',34,D,'tL')+T(812,390,'sin miedo',34,D,'tR'))+
 av('preocupada','aT','left:240px;top:660px;width:600px;height:600px')+av('tranquila','aC','left:240px;top:660px;width:600px;height:600px;opacity:0')+
 '<div class="q" style="top:1300px">¿Y si es <span class="st">otra cosa</span>?</div>')
# 3 ansiedad
sc('s3',12.6,17.45, chip('Ansiedad',L)+'<div class="t" style="top:430px">Se mueve por el <span class="st">miedo</span></div>'+
 svg(f'''<path id="road" d="M150 1010C330 950 560 1080 800 980" fill="none" stroke="{L}" stroke-width="14" stroke-linecap="round" stroke-dasharray="4 26"/>
<path id="arr" d="M770 940l52 38-58 30" fill="none" stroke="{L}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
<circle id="hoy" cx="150" cy="1010" r="44" fill="{A}" stroke="{D}" stroke-width="8"/>
<g id="wc"><path d="M700 900c-50 2-70-54-26-76-6-54 58-84 98-54 22-50 104-54 126-4 46-22 100 12 90 60 42 8 46 70 2 74z" fill="{R}" stroke="{D}" stroke-width="8"/></g>''',
 T(150,1110,'hoy',46,'#fff','th')+T(840,840,'¿y si sale',38,D,'tw')+T(840,884,'mal?',38,D,'tw')))
# 4 TDAH
icA=f'<circle cx="210" cy="890" r="56" fill="{R}" stroke="{D}" stroke-width="8"/><circle cx="210" cy="890" r="28" fill="{A}" stroke="{D}" stroke-width="8"/><circle cx="210" cy="890" r="9" fill="{D}"/>'
icB=f'<path d="M512 830h56l40 40v56l-40 40h-56l-40-40v-56z" fill="{R}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/><path d="M505 898h70" stroke="{D}" stroke-width="10" stroke-linecap="round"/>'
icC=f'<rect x="818" y="836" width="46" height="46" rx="10" fill="{L}" stroke="{D}" stroke-width="7"/><rect x="876" y="836" width="46" height="46" rx="10" fill="{L}" stroke="{D}" stroke-width="7"/><rect x="818" y="894" width="46" height="46" rx="10" fill="{L}" stroke="{D}" stroke-width="7"/><path d="M880 918l14 14 26-30" fill="none" stroke="{G}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
sc('s4',17.6,24.95, chip('TDAH',R)+'<div class="t" style="top:430px">No hace falta ningún <span class="st">miedo</span></div>'+
 svg(f'<g class="k1">{card(60,760)}{icA}</g><g class="k2">{card(390,760)}{icB}</g><g class="k3">{card(720,760)}{icC}</g>',
     T(210,1030,'Atención',40,D,'l1')+T(540,1030,'Impulsos',40,D,'l2')+T(870,1030,'Organización',34,D,'l3'))+
 '<div class="cap2" style="top:1150px">Sin miedo de por medio</div>')
# 5 perfeccionismo
rows=''.join(f'<g class="rw{i}"><circle cx="230" cy="{y}" r="34" fill="{A}" stroke="{D}" stroke-width="7"/><path class="ck{i}" d="M214 {y+2}l12 12 22-26" fill="none" stroke="{G}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></g>' for i,y in enumerate((860,980,1100)))
sc('s5',25.1,32.25, chip('Perfeccionismo')+'<div class="t" style="top:430px">A veces es una <span class="st">estrategia</span></div>'+
 svg(f'<g id="board"><rect x="150" y="760" width="780" height="430" rx="36" fill="{L}" stroke="{D}" stroke-width="8"/><rect x="430" y="730" width="220" height="60" rx="20" fill="{R}" stroke="{D}" stroke-width="7"/></g>{rows}',
     T(300,876,'Revisar',54,D,'rt0').replace('class="tx','class="tx left')+T(300,996,'Anotar',54,D,'rt1').replace('class="tx','class="tx left')+T(300,1116,'Controlar',54,D,'rt2').replace('class="tx','class="tx left'))+
 '<div class="q" style="top:1260px;font-size:62px"><span class="st">Controlar para no perderte</span></div>')
# 6 3 pistas
sc('s6',32.3,34.25, '<div class="t" style="top:560px;text-align:center;font-size:160px">3 <span class="st">pistas</span></div>'+
 svg(f'<path id="p3l" d="M240 1020C390 980 690 1060 840 1020" fill="none" stroke="{L}" stroke-width="10" stroke-linecap="round" stroke-dasharray="4 22"/>'+
     ''.join(f'<circle class="pn" cx="{x}" cy="1020" r="66" fill="{c}" stroke="{D}" stroke-width="8"/>' for x,c in ((240,L),(540,R),(840,A))),
     ''.join(T(x,1044,n,64,D,'pnt') for x,n in ((240,'1'),(540,'2'),(840,'3')))))
# 7 pista 1
def pill(n,t): return f'<div class="pill"><b>{n}</b>{t}</div>'
sc('s7',34.3,41.45, pill(1,'¿Desde cuándo?')+
 svg(f'<path d="M150 960C350 900 700 1020 930 950" fill="none" stroke="#6B5F8A" stroke-width="16" stroke-linecap="round"/><path id="tlp" d="M150 960C350 900 700 1020 930 950" fill="none" stroke="{L}" stroke-width="16" stroke-linecap="round"/>'+
     f'<circle id="inf" cx="150" cy="960" r="48" fill="{R}" stroke="{D}" stroke-width="8"/>'+''.join(f'<circle class="ms" cx="{x}" cy="{y}" r="22" fill="{L}" stroke="{D}" stroke-width="6"/>' for x,y in ((360,935),(560,962),(760,975)))+
     f'<circle id="hoy7" cx="930" cy="950" r="48" fill="{A}" stroke="{D}" stroke-width="8"/>',
     T(150,1068,'Infancia',44,'#fff','l7')+T(930,1058,'Hoy',44,'#fff','l7'))+
 '<div class="q" style="top:1180px;font-size:60px">No aparecen de un <span class="st">día para otro</span></div>')
# 8 pista 2
icH=f'<path d="M150 900l60-56 60 56z" fill="{R}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/><rect x="160" y="898" width="100" height="78" fill="{L}" stroke="{D}" stroke-width="8"/><rect x="196" y="926" width="28" height="50" fill="{A}" stroke="{D}" stroke-width="6"/>'
icS=f'<path d="M470 890l70-32 70 32-70 32z" fill="{L}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/><path d="M494 902v40c24 20 68 20 92 0v-40" fill="{R}" stroke="{D}" stroke-width="8"/><path d="M610 890v44" stroke="{D}" stroke-width="7" stroke-linecap="round"/>'
icW=f'<rect x="812" y="870" width="116" height="90" rx="14" fill="{R}" stroke="{D}" stroke-width="8"/><path d="M846 870v-22h48v22" fill="none" stroke="{D}" stroke-width="8"/><path d="M812 906h116" stroke="{D}" stroke-width="6"/>'
sc('s8',41.6,47.55, pill(2,'¿Dónde pasa?')+
 svg(f'<g class="c1">{card(60,760)}{icH}</g><g class="c2">{card(390,760)}{icS}</g><g class="c3">{card(720,760)}{icW}</g>'+
     ''.join(f'<g class="ok{i}"><circle cx="{x}" cy="770" r="30" fill="{G}" stroke="{D}" stroke-width="6"/><path d="M{x-13} 770l9 9 17-19" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>' for i,x in enumerate((330,660,990))),
     T(210,1030,'Casa',42,D,'x1')+T(540,1030,'Escuela',42,D,'x2')+T(870,1030,'Trabajo',42,D,'x3'))+
 '<div class="q" style="top:1180px;font-size:62px">No solo <span class="st">bajo estrés</span></div>')
# 9 pista 3
tr=f'<path id="tree" d="M540 760V840M540 840H300M540 840H780M300 840V920M780 840V920M300 920H190M300 920H410M780 920H670M780 920H890M190 920V1000M410 920V1000M670 920V1000M890 920V1000" fill="none" stroke="{L}" stroke-width="10" stroke-linecap="round"/>'
nodes=[(540,740,42,A,'g0')]+[(x,920,38,L,'g1') for x in (300,780)]+[(x,1040,36,R,'g2') for x in (190,410,670,890)]
sc('s9',47.6,52.25, pill(3,'¿A quién se parece?')+svg(tr+''.join(f'<circle class="{c}" cx="{x}" cy="{y}" r="{r}" fill="{f}" stroke="{D}" stroke-width="7"/>' for x,y,r,f,c in nodes))+
 '<div class="q" style="top:1180px;font-size:62px">Son rasgos <span class="st">hereditarios</span></div>')
# 10a disimular
sc('s10',52.3,57.05, chip('Sesgo en mujeres')+'<div class="t" style="top:430px">Aprenden a <span class="st">disimular</span></div>'+
 av('sonrisa','m1','left:290px;top:660px;width:500px;height:500px')+av('preocupada2','m2','left:290px;top:660px;width:500px;height:500px;opacity:0')+
 '<div class="q" style="top:1210px;font-size:60px">Por fuera, solo se ve a alguien <span class="st">nerviosa</span></div>')
# 10b convivir
sc('s11',57.1,60.15, svg(f'<circle class="v1" cx="420" cy="900" r="240" fill="{L}" fill-opacity=".9" stroke="{D}" stroke-width="8"/><circle class="v2" cx="660" cy="900" r="240" fill="{R}" fill-opacity=".85" stroke="{D}" stroke-width="8"/>',
 T(320,914,'Ansiedad',48,D,'vt')+T(770,894,'TDAH /',42,D,'vt')+T(770,944,'autismo',42,D,'vt'))+'<div class="q" style="top:1220px;font-size:70px">Pueden <span class="st">convivir</span></div>')
# 11 evaluación
rws=''.join(f'<path class="er" d="M440 {y}h200" stroke="{D}" stroke-width="9" stroke-linecap="round" opacity=".55"/><g class="ec{i}"><circle cx="390" cy="{y}" r="26" fill="{G}" stroke="{D}" stroke-width="6"/><path d="M378 {y}l8 8 16-18" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>' for i,y in enumerate((900,1010,1120)))
sc('s12',60.3,67.65, '<div class="t tt" style="top:430px;text-align:center">Las pistas <span class="st">no son</span> un diagnóstico</div>'+
 '<div class="chip ev" style="top:640px;left:50%;transform:translateX(-50%);background:'+L+'">Evaluación</div>'+
 svg(f'<g id="clip"><rect x="320" y="770" width="440" height="430" rx="34" fill="{A}" stroke="{D}" stroke-width="8"/><rect x="450" y="740" width="180" height="56" rx="18" fill="{R}" stroke="{D}" stroke-width="7"/></g>{rws}')+
 '<div class="cap2 ec" style="top:1250px;font-size:44px">Pruebas estandarizadas que ordenan tu historia</div>')
# 12 cierre
sc('s13',67.9,DUR, '<div class="t" style="top:360px;text-align:center;font-size:80px">Este video <span class="st">orienta</span> y no diagnostica.</div>'+
 '<div class="q2" style="top:600px">¿Cuál de las 3 pistas te hizo pensar?</div>'+
 av('sonrisa2','cz','left:370px;top:780px;width:340px;height:340px')+
 svg(''.join(f'<circle class="mn" cx="{x}" cy="1200" r="56" fill="{c}" stroke="{D}" stroke-width="8"/>' for x,c in ((300,L),(540,R),(780,A))),
     ''.join(T(x,1222,n,58,D,'mnt') for x,n in ((300,'1'),(540,'2'),(780,'3'))))+
 '<div class="web">psicologakarentrujillo.com.mx</div>')

BOUND=[4.65,12.45,17.5,24.95,32.25,34.25,41.45,47.55,52.25,57.05,60.2,67.65]
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
.web{{position:absolute;left:0;right:0;top:1300px;text-align:center;font:700 40px "Maven Pro";color:{L}}}
#tr{{position:absolute;left:0;top:0;width:1080px;height:1920px;pointer-events:none}}
.cap{{position:absolute;left:60px;right:60px;top:1460px;text-align:center}}
.plate{{display:inline;background:rgba(46,37,69,.9);color:#fff;font:700 54px/1.42 "Maven Pro",sans-serif;padding:6px 22px;border-radius:18px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}'''
doodles=f'''<svg class="full" viewBox="0 0 1080 1920"><defs><filter id="rough" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence id="turb" type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="1" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="6" xChannelSelector="R" yChannelSelector="G"/></filter></defs>
<g filter="url(#rough)"><g fill="{L}"><path class="sp" d="M120 600l10 26 26 10-26 10-10 26-10-26-26-10 26-10z"/><path class="sp" d="M960 700l8 20 20 8-20 8-8 20-8-20-20-8 20-8z"/><path class="sp" d="M100 1260l7 17 17 7-17 7-7 17-7-17-17-7 17-7z"/><path class="sp" d="M985 1230l9 22 22 9-22 9-9 22-9-22-22-9 22-9z"/></g>
<path class="sq" d="M840 250q20-24 40 0t40 0t40 0" fill="none" stroke="{R}" stroke-width="7" stroke-linecap="round"/><path class="sq" d="M90 260q20-24 40 0t40 0" fill="none" stroke="{L}" stroke-width="7" stroke-linecap="round"/></g></svg>'''
trsvg=f'<svg id="tr" viewBox="0 0 1080 1920"><g filter="url(#rough)"><line id="trl" x1="-40" y1="1380" x2="-40" y2="1380" stroke="{L}" stroke-width="12" stroke-linecap="round" opacity="0"/><circle id="trn" cx="-40" cy="1380" r="26" fill="{A}" stroke="{D}" stroke-width="7" opacity="0"/></g></svg>'
body=''.join(f'<div class="sc clip" id="{i}" data-start="{a}" data-duration="{round(b-a,2)}" data-track-index="1">{h}</div>' for i,a,b,h in SC)
capsh=''.join(f'<div class="cap clip" id="cap{k}" data-start="{a}" data-duration="{d}" data-track-index="5"><span class="plate">{H.escape(t)}</span></div>' for k,(t,a,d) in enumerate(caps))
js=open('anim.js').read().replace('__BOUND__',json.dumps(BOUND)).replace('__NCAP__',str(len(caps))).replace('__CAPS__',json.dumps([[a] for _,a,_ in caps]))
doc=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=1080, height=1920"><style>{css}</style></head><body>
<div id="root" data-composition-id="kt18full" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920" data-fps="30">
<div id="cam"><div class="lay" id="glow"></div>{doodles}{body}<div class="lay" id="vig"></div></div>{trsvg}{capsh}
<script src="gsap.min.js"></script><script>(function(){{{js}}})();</script></div></body></html>'''
open('public/index.html','w').write(doc); print(len(SC),'escenas',len(caps),'subtítulos')
