import math
def gp(cx,cy,ro,ri,n=8):
    pts=[]
    for i in range(n):
        a=2*math.pi*i/n; w=math.pi/n
        for da,r in ((-0.5*w,ri),(-0.28*w,ro),(0.28*w,ro),(0.5*w,ri)):
            pts.append((cx+r*math.cos(a+da),cy+r*math.sin(a+da)))
    return 'M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'Z'
def gear(cx,cy,ro,ri,fill,cls=''): return f'<g class="{cls}"><path d="{gp(cx,cy,ro,ri)}" fill="{fill}" stroke="{D}" stroke-width="7" stroke-linejoin="round"/><circle cx="{cx}" cy="{cy}" r="{ri*.38:.0f}" fill="{A}" stroke="{D}" stroke-width="6"/></g>'
def tab(x,y,w,fill): return f'<rect x="{x}" y="{y}" width="{w}" height="62" rx="16" fill="{fill}" stroke="{D}" stroke-width="6"/><circle cx="{x+26}" cy="{y+31}" r="8" fill="{D}"/><rect x="{x+48}" y="{y+24}" width="{w-76}" height="14" rx="7" fill="{D}" opacity=".6"/>'
def ck(cx,cy,r=34,cls=''): return f'<g class="{cls}"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{G}" stroke="{D}" stroke-width="6"/><path d="M{cx-r*.4:.0f} {cy}l{r*.3:.0f} {r*.3:.0f} {r*.6:.0f}-{r*.7:.0f}" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>'
def tr(x,y,inner): return f'<g transform="translate({x},{y})">{inner}</g>'
def bubble(x,y,w,h,cls): return f'<g class="{cls}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{A}" stroke="{D}" stroke-width="8"/><circle cx="{x+30}" cy="{y+h+30}" r="16" fill="{A}" stroke="{D}" stroke-width="6"/></g>'
def icard(x,y,w,h,icon,cls,fill=A): return f'<g class="{cls}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="38" fill="{fill}" stroke="{D}" stroke-width="8"/>{icon}</g>'
def book(x,y,w,h,cls): return f'<g class="{cls}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="30" fill="{A}" stroke="{D}" stroke-width="8"/>'+''.join(f'<circle cx="{x}" cy="{y+50+i*60}" r="11" fill="{D}"/>' for i in range(int((h-60)//60)))+'</g>'
def lupa(cx,cy,cls): return f'<g class="{cls}"><circle cx="{cx}" cy="{cy}" r="44" fill="{L}" fill-opacity=".45" stroke="{A}" stroke-width="12"/><path d="M{cx+32} {cy+32}l42 42" stroke="{A}" stroke-width="16" stroke-linecap="round"/></g>'
AVBOX='left:290px;top:820px;width:500px;height:500px'
# 1 gancho
sil=''.join(f'<g class="si"><circle cx="{x}" cy="1010" r="42" fill="{c}" stroke="{D}" stroke-width="7"/><rect x="{x-62}" y="1065" width="124" height="260" rx="50" fill="{c}" stroke="{D}" stroke-width="7"/></g>' for x,c in ((120,L),(250,R),(830,R),(960,L)))
sc('s1',0,6.65, chip('Neuropsicóloga Karen Trujillo · Cédula 11009616',A,300).replace('class="chip"','class="chip ced"')+
 '<div class="t" style="top:390px;font-size:92px"><span class="w">Una</span> <span class="w">reunión,</span><br><span class="st w">en calma</span></div>'+
 svg(sil)+av('calma','a1 ac',AVBOX)+av('hectica','a1 ah',AVBOX+';opacity:0')+
 svg(f'<g class="tb"><rect x="30" y="1290" width="1020" height="110" rx="44" fill="{A}" stroke="{D}" stroke-width="8"/></g>'+gear(540,1290,150,112,L,'g1')+
     f'<g class="wv"><path d="M300 1150q-40 30 0 60t0 60" fill="none" stroke="{A}" stroke-width="9" stroke-linecap="round"/><path d="M780 1150q40 30 0 60t0 60" fill="none" stroke="{A}" stroke-width="9" stroke-linecap="round"/></g>'))
# 2 hiperactividad
runner=f'<circle cx="0" cy="0" r="170" fill="{A}" stroke="{D}" stroke-width="8"/><g fill="none" stroke="{D}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"><circle cx="10" cy="-92" r="24" fill="{D}"/><path d="M5 -62L-12 12M-6 -45L-52 -10M-6 -45L40 -70M-12 12L-60 52L-90 40M-12 12L34 42L24 90"/></g><path class="sl" d="M-120 -120L120 120" stroke="{A}" stroke-width="34" stroke-linecap="round"/><path class="sl" d="M-120 -120L120 120" stroke="{D}" stroke-width="16" stroke-linecap="round"/>'
sc('s2',6.7,11.2, chip('TDAH en adultos',A,330)+
 '<div class="t" style="top:430px;font-size:92px">Hiperactividad <span class="st">en adultos</span></div>'+
 svg(tr(330,1130,f'<g class="rn">{runner}</g>')+f'<g class="g2m">{gear(540,1130,190,142,L,"g2")}</g>'+
     f'<g class="wv2"><path d="M250 960q-40 30 0 60t0 60" fill="none" stroke="{R}" stroke-width="9" stroke-linecap="round"/><path d="M830 960q40 30 0 60t0 60" fill="none" stroke="{R}" stroke-width="9" stroke-linecap="round"/></g>'))
# 3 cuatro tarjetas
cw,ch_=440,340
chair=tr(0,0,f'<rect x="-60" y="10" width="120" height="24" rx="10" fill="{L}" stroke="{D}" stroke-width="7"/><rect x="-60" y="-90" width="24" height="110" rx="10" fill="{L}" stroke="{D}" stroke-width="7"/><path d="M-45 34L-55 90M50 34L60 90" stroke="{D}" stroke-width="9" stroke-linecap="round"/><path d="M98 -30q28 30 0 60M122 -50q40 50 0 100" fill="none" stroke="{D}" stroke-width="7" stroke-linecap="round"/>')
tabs=tab(-130,-110,260,A)+tab(-100,-40,260,L)+tab(-130,30,260,R)
glass=f'<path d="M-55 -85L55 -85L40 90L-40 90Z" fill="{R}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/><path d="M-46 -25L46 -25L38 82L-38 82Z" fill="{L}"/>'
bub=f'<circle cx="-75" cy="25" r="58" fill="{L}" stroke="{D}" stroke-width="7"/><circle cx="25" cy="-50" r="44" fill="{R}" stroke="{D}" stroke-width="7"/><circle cx="95" cy="35" r="36" fill="{L}" stroke="{D}" stroke-width="7"/><circle cx="-10" cy="75" r="9" fill="{D}"/><circle cx="-25" cy="95" r="6" fill="{D}"/>'
ics=[chair,tabs,glass,bub]; labs=['cambias de postura','abres pestañas','te levantas por agua','piensas en otras tres cosas']
pos=[(70,620),(570,620),(70,1000),(570,1000)]
s3=''.join(icard(x,y,cw,ch_,tr(x+220,y+150,ics[i]),f'c{i}') for i,(x,y) in enumerate(pos))
s3t=''.join(T(x+220,y+305,labs[i],34 if i==3 else 36,D,f'cl{i}') for i,(x,y) in enumerate(pos))
sc('s3',11.25,21.8,'<div class="t" style="top:430px;font-size:92px">Inquietud <span class="st">invisible</span></div>'+svg(s3,s3t))
# 4 años creyendo
sc('s4',21.9,27.4,'<div class="t" style="top:430px;font-size:88px">Creer que solo es <span class="st">ansiedad</span></div>'+
 av('cansada','a4 u1','left:20px;top:800px;width:520px;height:520px')+av('preocupada','a4 u2','left:20px;top:800px;width:520px;height:520px;opacity:0')+
 svg(bubble(560,780,460,150,'b1')+bubble(560,1060,460,150,'b2'),T(790,876,'¿Solo ansiedad?',42,D,'bt1')+T(790,1156,'¿No sé relajarme?',42,D,'bt2')))
# 5 conducta ≠ diagnóstico
sq=f'<path d="M-80 0q20-44 40 0t40 0t40 0t40 0" fill="none" stroke="{D}" stroke-width="10" stroke-linecap="round"/>'
clip=f'<rect x="-70" y="-90" width="140" height="190" rx="18" fill="{R}" stroke="{D}" stroke-width="8"/><rect x="-32" y="-108" width="64" height="34" rx="12" fill="{L}" stroke="{D}" stroke-width="7"/><path d="M-40 -30h80M-40 10h80M-40 50h50" stroke="{D}" stroke-width="8" stroke-linecap="round"/>'
neq=f'<g class="ne"><circle cx="540" cy="885" r="62" fill="{L}" stroke="{D}" stroke-width="8"/><path d="M510 868h60M510 902h60" stroke="{D}" stroke-width="12" stroke-linecap="round"/><path d="M522 935L558 835" stroke="{D}" stroke-width="12" stroke-linecap="round"/></g>'
sc('s5',27.45,32.5,'<div class="t" style="top:430px;font-size:92px">Ojo: no es un <span class="st">diagnóstico</span></div>'+
 svg(icard(60,720,400,330,tr(260,860,sq),'k1')+f'<rect class="dp" x="620" y="720" width="400" height="330" rx="38" fill="none" stroke="{A}" stroke-width="8" stroke-dasharray="18 14"/>'+icard(620,720,400,330,tr(820,850,clip),'k2')+neq,
     T(260,1010,'Una conducta',40,D,'kt1')+T(820,1010,'Un diagnóstico',40,D,'kt2'))+
 '<div class="cap2" style="top:1150px">De vez en cuando no basta</div>')
# 6 estrés, sueño, café
cloud=f'<g fill="{L}" stroke="{D}" stroke-width="8"><circle cx="-45" cy="-10" r="48"/><circle cx="10" cy="-40" r="58"/><circle cx="62" cy="-5" r="44"/><rect x="-80" y="-10" width="170" height="52" rx="26" stroke="none"/></g><path d="M0 20l-22 48h30l-18 50" fill="none" stroke="{D}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
moon=f'<path d="M25 -95A95 95 0 1 0 80 55A72 72 0 1 1 25 -95Z" fill="{L}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/>'
cup=f'<path d="M-70 -30H70V30Q70 90 0 90Q-70 90 -70 30Z" fill="{R}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/><path d="M70 -10h26a30 30 0 0 1 0 60h-30" fill="none" stroke="{D}" stroke-width="8"/><path d="M-30 -45q-20-25 0-50M20 -45q-20-25 0-50" fill="none" stroke="{D}" stroke-width="7" stroke-linecap="round"/>'
labs6=['estrés','poco sueño','mucho café']
s6=''.join(icard(x,700,300,340,tr(x+150,850,[cloud,moon,cup][i]),f'd{i}') for i,x in enumerate((60,390,720)))
s6t=''.join(T(x+150,1000,labs6[i],38,D,f'dl{i}') for i,x in enumerate((60,390,720)))
sc('s6',32.55,37.1,'<div class="t" style="top:430px;font-size:92px">También <span class="st">inquietan</span></div>'+svg(s6,s6t+T(625,790,'z',54,D,'zz')+T(665,745,'z',40,D,'zz')))
# 7 profesional explora
rows=['¿Son constantes?','¿Desde la infancia?','¿En casa y en el trabajo?','¿Dificultades reales?']
ys=[700,860,1020,1180]
s7=''.join(f'<g class="r{i}"><rect x="60" y="{y}" width="800" height="130" rx="44" fill="{A}" stroke="{D}" stroke-width="8"/><circle cx="800" cy="{y+65}" r="34" fill="none" stroke="{D}" stroke-width="6" stroke-dasharray="10 8"/></g>' for i,y in enumerate(ys))
s7+=''.join(ck(800,y+65,34,f'k{i}') for i,y in enumerate(ys))+lupa(960,765,'lp')
s7t=''.join(f'<text class="tx left" x="100" y="{y+78}" font-size="42" fill="{D}" id="" data-r="{i}">{rows[i]}</text>' for i,y in enumerate(ys))
sc('s7',37.15,47.8,'<div class="t" style="top:430px;font-size:92px">Un profesional <span class="st">explora</span></div>'+svg(s7,s7t))
# 8 no te etiquetes
tag=f'<g class="tg"><path d="M60 650h280l44 50-44 50H60z" fill="{R}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/><circle cx="96" cy="700" r="11" fill="{A}" stroke="{D}" stroke-width="5"/></g>'
nb=book(70,800,440,520,'nb')+''.join(f'<path class="nl" d="M120 {y}h340" stroke="{D}" stroke-width="9" stroke-linecap="round" fill="none"/>' for y in (960,1050,1140))
sc('s8',47.9,54.1,'<div class="t" style="top:430px;font-size:92px">No te <span class="st">etiquetes</span></div>'+
 av('anota','a8 n1','left:540px;top:830px;width:480px;height:480px')+av('sonrisa','a8 n2','left:540px;top:830px;width:480px;height:480px;opacity:0')+
 svg(tag+nb,T(535,640,'¿TDAH?',44,D,'tgt').replace('x="535"','x="205"').replace('y="640"','y="715"')+T(290,885,'¿Cuándo aparece?',38,D,'nt')))
# 9 información útil
cb=f'<g class="cb"><rect x="650" y="780" width="340" height="440" rx="34" fill="{R}" stroke="{D}" stroke-width="8"/><rect x="760" y="755" width="120" height="50" rx="18" fill="{L}" stroke="{D}" stroke-width="7"/></g>'
cl=''.join(f'<path class="cn" d="M700 {y}h240" stroke="{D}" stroke-width="9" stroke-linecap="round" fill="none"/>' for y in (900,980,1060))
sc('s9',54.15,60.4,'<div class="t" style="top:430px;font-size:92px">Sirve para tu <span class="st">evaluación</span></div>'+
 svg(book(80,800,300,400,'m9')+''.join(f'<path class="ml" d="M130 {y}h200" stroke="{D}" stroke-width="8" stroke-linecap="round" fill="none"/>' for y in (900,980,1060))+cb+cl+
     f'<path class="ar" d="M420 1000h190m-34-30l34 30-34 30" fill="none" stroke="{A}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>'+ck(960,780,38,'ok'),
     T(820,1300,'Para tu evaluación',44,'#fff','pe')))
# 10 cierre
sc('s10',60.45,DUR,'<div class="t t1" style="top:430px;text-align:center;font-size:92px">Sigue esta <span class="st">cuenta</span></div>'+
 '<div class="t t2" style="top:430px;text-align:center;font-size:80px">Este video <span class="st">orienta</span> y no diagnostica.</div>'+
 av('sonrisa2','cz','left:330px;top:720px;width:420px;height:420px')+'<div class="web" style="top:1180px">psicologakarentrujillo.com.mx</div>')
BOUND=[6.7,11.25,21.9,27.45,32.55,37.15,47.9,54.15,60.45]
