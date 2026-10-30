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
def pl(inner,cx,cy,s,ox,oy): return f'<g transform="translate({cx-ox*s:.1f},{cy-oy*s:.1f}) scale({s})">{inner}</g>'
def key(fill,rot): return f'<g transform="rotate({rot} 300 1075)"><circle cx="300" cy="1150" r="34" fill="{fill}" stroke="{D}" stroke-width="8"/><circle cx="300" cy="1150" r="11" fill="{D}"/><rect x="289" y="1182" width="22" height="120" rx="8" fill="{fill}" stroke="{D}" stroke-width="8"/><rect x="311" y="1252" width="30" height="16" rx="4" fill="{fill}" stroke="{D}" stroke-width="7"/><rect x="311" y="1278" width="22" height="16" rx="4" fill="{fill}" stroke="{D}" stroke-width="7"/></g>'
KEYS=key(L,-16)+key(A,12)+f'<circle cx="300" cy="1068" r="30" fill="none" stroke="{D}" stroke-width="9"/>'
RAIL=f'<rect x="225" y="985" width="150" height="24" rx="12" fill="{A}" stroke="{D}" stroke-width="7"/><circle cx="300" cy="1030" r="12" fill="{D}"/>'
PHONE=f'<g transform="rotate(-9 560 1250)"><rect x="505" y="1130" width="120" height="205" rx="26" fill="{A}" stroke="{D}" stroke-width="8"/><rect x="520" y="1160" width="90" height="145" rx="10" fill="{L}"/><rect x="545" y="1143" width="40" height="8" rx="4" fill="{D}"/></g>'
WALLET=f'<rect x="615" y="1250" width="95" height="75" rx="14" fill="{L}" stroke="{D}" stroke-width="8"/><path d="M615 1280h95" stroke="{D}" stroke-width="7"/><circle cx="690" cy="1280" r="9" fill="{A}" stroke="{D}" stroke-width="5"/>'
TRAY=f'<path d="M440 1300h270l-26 85H466z" fill="{R}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/>'
HEAD=f'<path d="M790 1285C785 1150 925 1150 920 1285" fill="none" stroke="{D}" stroke-width="16" stroke-linecap="round"/><rect x="765" y="1240" width="52" height="95" rx="24" fill="{R}" stroke="{D}" stroke-width="8"/><rect x="893" y="1240" width="52" height="95" rx="24" fill="{R}" stroke="{D}" stroke-width="8"/>'
BOX=f'<rect x="762" y="1335" width="186" height="50" rx="18" fill="{A}" stroke="{D}" stroke-width="8"/>'
K=lambda cx,cy,s: pl(KEYS,cx,cy,s,300,1170)
P=lambda cx,cy,s: pl(PHONE,cx,cy,s,560,1232)
HD=lambda cx,cy,s: pl(HEAD,cx,cy,s,855,1255)
# 1 gancho
sc('s1',0,4.85, chip('Neuropsicóloga Karen Trujillo · Cédula 11009616',A,300).replace('class="chip"','class="chip ced"')+
 '<div class="t" style="top:390px;font-size:96px"><span class="w">Llegas</span> <span class="w">a</span> <span class="w">casa</span> <span class="w">con</span> <span class="w">las</span> <span class="st w">manos llenas</span></div>'+
 av('cansada','a1','left:20px;top:800px;width:440px;height:440px')+
 svg(f'<g class="dk1">{K(700,1010,.85)}</g><g class="dk2">{P(850,1200,.9)}</g><g class="dk3">{HD(690,1350,.85)}</g>'))
# 2 los sueltas
sfc=f'<rect x="60" y="950" width="300" height="26" rx="13" fill="{L}" stroke="{D}" stroke-width="7"/><path d="M100 976v90M320 976v90" stroke="{D}" stroke-width="10" stroke-linecap="round"/>'+f'<rect x="400" y="930" width="300" height="80" rx="34" fill="{R}" stroke="{D}" stroke-width="7"/><rect x="400" y="880" width="300" height="60" rx="30" fill="{R}" stroke="{D}" stroke-width="7"/>'+f'<rect x="740" y="950" width="280" height="22" rx="11" fill="{L}" stroke="{D}" stroke-width="7"/><path d="M780 972v40M980 972v40" stroke="{D}" stroke-width="9" stroke-linecap="round"/>'
sc('s2',4.9,12.0, '<div class="t" style="top:430px;font-size:88px">Los sueltas <span class="st">«un momento»</span></div>'+
 svg(f'<g class="su">{sfc}</g><g class="o1">{K(210,900,.4)}</g><g class="o2">{P(550,880,.6)}</g><g class="o3">{HD(880,900,.6)}</g>'+''.join(f'<g class="qm{i}"><circle cx="{x}" cy="760" r="38" fill="{R}" stroke="{D}" stroke-width="7"/></g>' for i,x in enumerate((210,550,880))),
     ''.join(T(x,774,'?',50,D,f'qt{i}') for i,x in enumerate((210,550,880))))+
 av('dudosa','aD','left:300px;top:1040px;width:400px;height:400px'))
# 3 memoria / lugar distinto
sp=lambda x,lab,i: f'<g class="sp{i}"><rect x="{x}" y="1020" width="190" height="190" rx="34" fill="{A}" stroke="{D}" stroke-width="8"/></g>'
sc('s3',12.1,22.5, '<div class="t" style="top:430px">No es tu <span class="st">memoria</span></div>'+
 svg(f'<g class="mc"><rect x="80" y="740" width="400" height="170" rx="46" fill="{A}" stroke="{D}" stroke-width="8"/></g><g class="ck"><circle cx="520" cy="826" r="52" fill="{G}" stroke="{D}" stroke-width="8"/><path d="M496 826l18 18 32-36" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>'
     f'<g class="kk">{K(170,1130,.75)}</g>'+
     sp(400,'mesa',0)+sp(610,'sofá',1)+sp(820,'bolsa',2)+
     f'<g class="dq"><circle cx="170" cy="1000" r="44" fill="{R}" stroke="{D}" stroke-width="7"/></g>',
     T(280,848,'memoria',58,D,'mt')+T(495,1130,'mesa',44,D,'sl0')+T(705,1130,'sofá',44,D,'sl1')+T(915,1130,'bolsa',44,D,'sl2')+T(170,1018,'?',54,D,'dqt'))+
 '<div class="q" style="top:1300px;font-size:64px">Si cambia, hay que <span class="st">recordar</span></div>')
# 4 zona de aterrizaje
sc('s4',22.6,33.0, '<div class="t" style="top:430px">Una zona de <span class="st">aterrizaje</span></div>'+
 svg(f'<g transform="translate(0,-150)"><rect class="zp" x="120" y="930" width="840" height="470" rx="48" fill="{L}" fill-opacity=".25" stroke="{D}" stroke-width="8"/>'
     f'<g class="zs"><rect x="215" y="975" width="170" height="340" rx="30" fill="none" stroke="{A}" stroke-width="7" stroke-dasharray="16 12"/><rect x="430" y="1120" width="290" height="275" rx="30" fill="none" stroke="{A}" stroke-width="7" stroke-dasharray="16 12"/><rect x="750" y="1160" width="210" height="235" rx="30" fill="none" stroke="{A}" stroke-width="7" stroke-dasharray="16 12"/></g><g class="zk">{RAIL}{KEYS}</g><g class="zt">{PHONE}{WALLET}{TRAY}</g><g class="zb">{HEAD}{BOX}</g></g>',
     T(300,1290,'gancho',40,'#fff','zl1')+T(575,1290,'bandeja',40,'#fff','zl2')+T(855,1290,'cajita',40,'#fff','zl3')))
# 5 a la vista, a la mano
sc('s5',33.1,39.2, '<div class="t" style="top:430px">A la vista y <span class="st">a la mano</span></div>'+
 svg(f'<g class="ey"><rect x="70" y="740" width="450" height="230" rx="40" fill="{A}" stroke="{D}" stroke-width="8"/><path d="M200 855q95-100 190 0q-95 100-190 0z" fill="{R}" stroke="{D}" stroke-width="8"/><circle cx="295" cy="855" r="30" fill="{L}" stroke="{D}" stroke-width="7"/><circle cx="295" cy="855" r="11" fill="{D}"/></g>'
     f'<g class="ma"><rect x="560" y="740" width="450" height="230" rx="40" fill="{A}" stroke="{D}" stroke-width="8"/><path d="M640 930V790M640 790h40M640 830h26M640 870h40M640 910h26" stroke="{D}" stroke-width="8" stroke-linecap="round" fill="none"/><rect x="720" y="820" width="220" height="70" rx="20" fill="{L}" stroke="{D}" stroke-width="7" stroke-dasharray="14 10"/></g>'
     f'<g class="p3"><rect x="70" y="1080" width="450" height="130" rx="65" fill="{R}" stroke="{D}" stroke-width="8"/></g><path id="x3" d="M110 1100L480 1190" stroke="{D}" stroke-width="12" stroke-linecap="round"/>'
     f'<g class="p1"><rect x="560" y="1080" width="450" height="130" rx="65" fill="{A}" stroke="{D}" stroke-width="8"/><circle cx="950" cy="1075" r="34" fill="{G}" stroke="{D}" stroke-width="6"/><path d="M936 1075l10 10 18-22" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>',
     T(295,945,'a la vista',40,D,'e1')+T(830,945,'altura de la mano',34,D,'e2').replace('x="830"','x="800"')+T(295,1165,'3 pasos',54,D,'n3')+T(785,1165,'1 gesto',54,D,'n1')))
# 6 gesto
sc('s6',39.3,48.4, '<div class="t" style="top:430px">Lo vuelve <span class="st">hábito</span></div>'+
 svg(f'<g class="dr"><rect x="60" y="720" width="190" height="330" rx="26" fill="{R}" stroke="{D}" stroke-width="8"/><circle cx="216" cy="890" r="14" fill="{D}"/></g>'+
     ''.join(f'<g class="cd{i}"><rect x="{x}" y="1110" width="300" height="200" rx="36" fill="{A}" stroke="{D}" stroke-width="8"/></g>' for i,x in enumerate((60,390,720)))+
     f'<g class="ik0">{K(210,1210,.55)}</g><g class="ik1">{P(540,1215,.7)}</g><g class="ik2">{HD(870,1215,.6)}</g>'+
     ''.join(f'<g class="nb{i}"><circle cx="{x}" cy="1110" r="36" fill="{G}" stroke="{D}" stroke-width="7"/></g>' for i,x in enumerate((90,420,750))),
     ''.join(T(x,1124,str(i+1),42,'#fff',f'nt{i}') for i,x in enumerate((90,420,750))))+
 av('tranquila','aQ','left:330px;top:700px;width:380px;height:380px')+
 '<div class="q" style="top:1350px;font-size:60px">Al entrar, <span class="st">soltar todo ahí</span></div>')
# 7 semana / revisar
days='LMXJVSD'
cal=''.join(f'<circle class="dy{i}" cx="{130+i*137}" cy="900" r="46" fill="{A}" stroke="{D}" stroke-width="7"/>' for i in range(7))
cks=''.join(f'<path class="dc{i}" d="M{130+i*137-18} 982l12 12 24-28" fill="none" stroke="{G}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>' for i in range(7))
sc('s7',48.5,57.3, '<div class="t" style="top:430px">Una <span class="st">semana</span></div>'+
 svg(cal+cks+f'<g class="eye"><circle cx="150" cy="1190" r="62" fill="{A}" stroke="{D}" stroke-width="8"/><path d="M95 1190q55-62 110 0q-55 62-110 0z" fill="{R}" stroke="{D}" stroke-width="6"/><circle cx="150" cy="1190" r="18" fill="{L}" stroke="{D}" stroke-width="5"/><circle cx="150" cy="1190" r="7" fill="{D}"/></g>'
     f'<g class="mz"><rect x="270" y="1090" width="470" height="220" rx="36" fill="{L}" fill-opacity=".3" stroke="{D}" stroke-width="8"/><g transform="translate(40,-10)">{P(420,1215,.7)}</g>{pl(TRAY,520,1255,.6,575,1340)}<rect x="320" y="1120" width="90" height="150" rx="14" fill="none" stroke="{R}" stroke-width="8" stroke-dasharray="14 10"/></g>'
     f'<g class="mf"><circle cx="365" cy="1130" r="30" fill="{R}" stroke="{D}" stroke-width="6"/></g>'
     f'<g class="sw"><circle cx="900" cy="1200" r="76" fill="{A}" stroke="{D}" stroke-width="8"/><rect x="880" y="1108" width="40" height="22" rx="8" fill="{L}" stroke="{D}" stroke-width="6"/><line class="swh" x1="900" y1="1200" x2="900" y2="1150" stroke="{D}" stroke-width="9" stroke-linecap="round"/><circle cx="900" cy="1200" r="9" fill="{D}"/></g>',
     ''.join(T(130+i*137,914,d,40,D,f'dl{i}') for i,d in enumerate(days))+T(365,1144,'!',44,D,'mft')+T(900,1330,'2 s',46,'#fff','s2')))
# 8 cualquier persona
sc('s8',57.4,65.0, '<div class="t" style="top:430px">Sirve a <span class="st">cualquier persona</span></div>'+
 svg(f'<circle class="v1" cx="390" cy="1000" r="190" fill="{L}" fill-opacity=".9" stroke="{D}" stroke-width="8"/><circle class="v2" cx="690" cy="1000" r="190" fill="{R}" fill-opacity=".85" stroke="{D}" stroke-width="8"/>'
     f'<g class="cs"><rect x="120" y="1290" width="840" height="130" rx="50" fill="{A}" stroke="{D}" stroke-width="8"/><circle cx="900" cy="1290" r="34" fill="{G}" stroke="{D}" stroke-width="6"/><path d="M886 1290l10 10 18-22" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>',
     T(335,1012,'con TDAH',38,D,'vt')+T(745,1012,'sin TDAH',38,D,'vt')+T(540,1370,'Si te pasa mucho: consúltalo',44,D,'cst')))
# 9 cierre
sc('s9',65.1,DUR, '<div class="t" style="top:360px;text-align:center;font-size:80px">Este video <span class="st">orienta</span> y no diagnostica.</div>'+
 svg(f'<g class="sg"><path d="M540 760V1200" stroke="{L}" stroke-width="16" stroke-linecap="round"/><path d="M540 800h300l50 50-50 50H540z" fill="{A}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/><path d="M540 930H240l-50 50 50 50h300z" fill="{R}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/></g>',
     T(690,865,'orienta',44,D,'sgt')+T(390,995,'no diagnostica',38,D,'sgt'))+
 '<div class="q2" style="top:620px">¿Qué objeto pierdes más?</div>'+
 svg(''.join(f'<g class="oc{i}"><rect x="{x}" y="780" width="300" height="270" rx="40" fill="{A}" stroke="{D}" stroke-width="8"/></g>' for i,x in enumerate((60,390,720)))+
     f'<g class="oi0">{K(210,915,.6)}</g><g class="oi1">{P(540,915,.8)}</g><g class="oi2">{HD(870,920,.75)}</g>',
     T(210,1100,'llaves',40,'#fff','ol0')+T(540,1100,'celular',40,'#fff','ol1')+T(870,1100,'audífonos',40,'#fff','ol2'))+
 av('sonrisa','cz','left:405px;top:1130px;width:270px;height:270px')+
 '<div class="web" style="top:1405px">psicologakarentrujillo.com.mx</div>')
BOUND=[4.85,12.05,22.55,32.95,39.25,48.45,57.35,65.05]
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
<div id="root" data-composition-id="kt22full" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920" data-fps="30">
<div id="cam"><div class="lay" id="glow"></div>{doodles}{body}<div class="lay" id="vig"></div></div>{trsvg}{capsh}
<script src="gsap.min.js"></script><script>(function(){{{js}}})();</script></div></body></html>'''
open('public/index.html','w').write(doc); print(len(SC),'escenas',len(caps),'subtítulos')
