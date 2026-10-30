import math
def tr(x,y,inner): return f'<g transform="translate({x},{y})">{inner}</g>'
def ck(cx,cy,r=34,cls=''): return f'<g class="{cls}"><circle cx="{cx}" cy="{cy}" r="{r}" fill="{G}" stroke="{D}" stroke-width="6"/><path d="M{cx-r*.4:.0f} {cy}l{r*.3:.0f} {r*.3:.0f} {r*.6:.0f}-{r*.7:.0f}" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></g>'
def icard(x,y,w,h,icon,cls,fill=A): return f'<g class="{cls}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="38" fill="{fill}" stroke="{D}" stroke-width="8"/>{icon}</g>'
def clock(cx,cy,r,hc,mc,hang=-60):
    t=''.join(f'<path d="M{cx+r*.82*math.sin(i*math.pi/6):.1f} {cy-r*.82*math.cos(i*math.pi/6):.1f}L{cx+r*.93*math.sin(i*math.pi/6):.1f} {cy-r*.93*math.cos(i*math.pi/6):.1f}" stroke="{D}" stroke-width="8" stroke-linecap="round"/>' for i in range(12))
    hx=cx+r*.5*math.sin(math.radians(300)); hy=cy-r*.5*math.cos(math.radians(300))
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{A}" stroke="{D}" stroke-width="9"/>{t}'
      f'<g class="{hc}"><path d="M{cx} {cy}L{hx:.1f} {hy:.1f}" stroke="{D}" stroke-width="14" stroke-linecap="round"/></g>'
      f'<g class="{mc}"><path d="M{cx} {cy}L{cx} {cy-r*.72:.1f}" stroke="{D}" stroke-width="10" stroke-linecap="round"/></g><circle cx="{cx}" cy="{cy}" r="12" fill="{D}"/>')
def pillb(x,y,w,t,fill,cls): return f'<g class="{cls}"><rect x="{x}" y="{y}" width="{w}" height="84" rx="42" fill="{fill}" stroke="{D}" stroke-width="7"/></g>'
# 1 gancho
sc('s1',0,6.45, chip('Neuropsicóloga Karen Trujillo · Cédula 11009616',A,300).replace('class="chip"','class="chip ced"')+
 '<div class="t" style="top:390px;font-size:92px"><span class="w">Cita</span> <span class="w">a</span> <span class="w">las</span> <span class="st w">diez</span></div>'+
 av('duda','a1 d1','left:10px;top:860px;width:470px;height:470px')+av('cansada','a1 d2','left:10px;top:860px;width:470px;height:470px;opacity:0')+
 svg(pillb(60,700,300,'',L,'p1')+pillb(390,700,300,'',R,'p2')+pillb(720,700,300,'',A,'p3')+
     f'<g class="ck1">{clock(770,1090,150,"hh1","mm1")}</g>',
     T(210,755,'me baño',38,D,'pt1')+T(540,755,'me visto',38,D,'pt2')+T(870,755,'salgo',38,D,'pt3')))
# 2 lo que ves / lo que olvidas
def mini(x,y,t,cls,dash=False): return f'<g class="{cls}"><rect x="{x}" y="{y}" width="380" height="70" rx="30" fill="{"none" if dash else L}" stroke="{D if not dash else A}" stroke-width="7" {"stroke-dasharray=\"14 10\"" if dash else ""}/></g>'
v1=''.join(mini(100,790+i*100,'','m1'+str(i)) for i in range(3)); v2=''.join(mini(600,790+i*100,'','m2'+str(i),True) for i in range(3))
sc('s2',6.5,10.3,'<div class="t" style="top:430px;font-size:92px">Lo que <span class="st">ves</span></div>'+
 svg(icard(60,640,460,420,'','v1c')+icard(560,640,460,420,'','v2c',fill='#3d3260')+v1+v2+
     ck(470,700,0,'x'),
     T(290,710,'Lo que ves',44,D,'vl1')+T(790,710,'Lo que olvidas',44,'#fff','vl2')+''.join(T(290,835+i*100,t,36,D,f'vt1{i}') for i,t in enumerate(['baño','ropa','salir']))+''.join(T(790,835+i*100,'?',46,A,f'vt2{i}') for i in range(3))))
# 3 tareas invisibles
cw,ch_=440,340
keys=f'<circle cx="-60" cy="-20" r="46" fill="{L}" stroke="{D}" stroke-width="8"/><circle cx="-60" cy="-20" r="14" fill="{D}"/><rect x="-14" y="-34" width="130" height="28" rx="10" fill="{L}" stroke="{D}" stroke-width="8"/><rect x="70" y="-6" width="20" height="38" rx="6" fill="{L}" stroke="{D}" stroke-width="7"/><rect x="100" y="-6" width="20" height="28" rx="6" fill="{L}" stroke="{D}" stroke-width="7"/>'
msg=f'<rect x="-90" y="-80" width="180" height="120" rx="34" fill="{L}" stroke="{D}" stroke-width="8"/><path d="M-40 40L-60 90L0 40Z" fill="{L}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/><path d="M-55 -40h110M-55 -5h70" stroke="{D}" stroke-width="9" stroke-linecap="round"/><circle cx="85" cy="-80" r="26" fill="{R}" stroke="{D}" stroke-width="7"/>'
blouse=f'<path d="M0 -50V-72q0 -26 26 -26" fill="none" stroke="{D}" stroke-width="8" stroke-linecap="round"/><path d="M-90 -5L0 -55L90 -5" fill="none" stroke="{D}" stroke-width="8" stroke-linecap="round"/><path d="M-72 -8L-38 -52Q0 -30 38 -52L72 -8L48 14L38 4V80H-38V4L-48 14Z" fill="{R}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/>'
light=f'<rect x="-44" y="-95" width="88" height="190" rx="36" fill="{L}" stroke="{D}" stroke-width="8"/><circle cx="0" cy="-52" r="24" fill="{R}" stroke="{D}" stroke-width="6"/><circle cx="0" cy="0" r="24" fill="{A}" stroke="{D}" stroke-width="6"/><circle cx="0" cy="52" r="24" fill="{G}" stroke="{D}" stroke-width="6"/>'
ics=[keys,msg,blouse,light]; labs=['las llaves','un mensaje','cambiarte de blusa','el tráfico']
pos=[(70,620),(570,620),(70,1000),(570,1000)]
s3=''.join(icard(x,y,cw,ch_,tr(x+220,y+150,ics[i]),f'c{i}') for i,(x,y) in enumerate(pos))
s3t=''.join(T(x+220,y+305,labs[i],36,D,f'cl{i}') for i,(x,y) in enumerate(pos))
sc('s3',10.35,18.15,'<div class="t" style="top:430px;font-size:92px">Tareas <span class="st">invisibles</span></div>'+svg(s3,s3t))
# 4 planea al revés
blk=[(770,'Llegada',A,'10:00'),(530,'Camino',R,''),(290,'Arreglarte',L,''),(70,'Margen',None,'+10')]
b4=''.join(f'<g class="bk{i}"><rect x="{x}" y="800" width="{220 if i<3 else 190}" height="120" rx="40" fill="{c or "none"}" stroke="{D if c else A}" stroke-width="8" {"" if c else "stroke-dasharray=\"16 12\""}/></g>' for i,(x,t,c,s) in enumerate(blk))
sc('s4',18.2,29.45,'<div class="t" style="top:430px;font-size:92px">Planea al <span class="st">revés</span></div>'+
 svg(f'<path class="ar4" d="M1000 730H140m40-34l-40 34 40 34" fill="none" stroke="{A}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>'+b4+f'<g class="ck4">{clock(540,1180,150,"hh4","mm4")}</g>',
     ''.join(T(x+(110 if i<3 else 95),872,t,34 if i!=3 else 36,D if c else A,f'bl{i}') for i,(x,t,c,s) in enumerate(blk))+T(880,775,'',1)))
# 5 mide tu tiempo
cal=''.join(f'<circle class="dy{i}" cx="{130+i*137}" cy="760" r="46" fill="{A}" stroke="{D}" stroke-width="7"/>' for i in range(7))
cks=''.join(f'<path class="dc{i}" d="M{130+i*137-18} 764l12 12 24-28" fill="none" stroke="{G}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>' for i in range(7))
sc('s5',29.5,40.35,'<div class="t" style="top:430px;font-size:92px">Mide tu <span class="st">tiempo</span></div>'+
 svg(cal+cks+f'<g class="bc"><rect x="60" y="960" width="340" height="110" rx="40" fill="{L}" stroke="{D}" stroke-width="8"/></g><g class="br"><rect x="60" y="1130" width="720" height="110" rx="40" fill="{R}" stroke="{D}" stroke-width="8"/></g>'+ck(880,1185,50,'ok5'),
     ''.join(T(130+i*137,774,d,40,D,f'dl{i}') for i,d in enumerate('LMXJVSD'))+T(230,1030,'Creo: 20 min',42,D,'bt1')+T(420,1200,'Real: 35 min',46,D,'bt2')))
# 6 alarma
sc('s6',40.4,46.35,'<div class="t" style="top:430px;font-size:92px">Una <span class="st">alarma</span></div>'+
 av('calma','a6 u6','left:570px;top:830px;width:450px;height:450px')+
 svg(pillb(60,640,240,'',L,'q1')+f'<path class="qa" d="M320 682h120m-30-26l30 26-30 26" fill="none" stroke="{A}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'+pillb(460,640,240,'',R,'q2')+
     f'<g class="ph"><rect x="70" y="800" width="400" height="560" rx="56" fill="{A}" stroke="{D}" stroke-width="9"/><rect x="100" y="860" width="340" height="440" rx="30" fill="{L}"/></g>'+
     f'<g class="bn"><rect x="115" y="930" width="310" height="170" rx="30" fill="{A}" stroke="{D}" stroke-width="7"/><circle cx="170" cy="985" r="26" fill="{R}" stroke="{D}" stroke-width="6"/></g>',
     T(180,696,'Ducha',38,D,'qt1')+T(580,696,'Salir',38,D,'qt2')+T(285,1010,'Ya toca',40,D,'bt')+T(285,1062,'salir',40,D,'bt')))
# 7 sirve a cualquiera
sc('s7',46.4,55.25,'<div class="t" style="top:430px;font-size:92px">Sirve a <span class="st">cualquiera</span></div>'+
 svg(f'<circle class="v1" cx="390" cy="950" r="190" fill="{L}" fill-opacity=".9" stroke="{D}" stroke-width="8"/><circle class="v2" cx="690" cy="950" r="190" fill="{R}" fill-opacity=".85" stroke="{D}" stroke-width="8"/>'+
     f'<g class="c1"><rect x="60" y="1240" width="450" height="130" rx="50" fill="{A}" stroke="{D}" stroke-width="8"/></g><path class="ar7" d="M520 1305h70m-24-22l24 22-24 22" fill="none" stroke="{A}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/><g class="c2"><rect x="610" y="1240" width="410" height="130" rx="50" fill="{A}" stroke="{D}" stroke-width="8"/></g>'+ck(970,1240,34,'k7'),
     T(335,962,'con TDAH',38,D,'vt')+T(745,962,'sin TDAH',38,D,'vt')+T(285,1318,'Si es constante',40,D,'ct1')+T(815,1318,'Consúltalo',44,D,'ct2')))
# 8 cierre
sc('s8',55.3,DUR,'<div class="t t1" style="top:430px;text-align:center;font-size:88px">¿Cuántos minutos <span class="st">extra</span>?</div>'+
 '<div class="t t2" style="top:430px;text-align:center;font-size:80px">Este video <span class="st">orienta</span> y no diagnostica.</div>'+
 av('sonrisa','cz','left:330px;top:720px;width:420px;height:420px')+
 svg(f'<g class="eb"><rect x="720" y="760" width="260" height="110" rx="55" fill="{A}" stroke="{D}" stroke-width="8"/></g>',T(850,832,'+ ? min',44,D,'ebt'))+
 '<div class="web" style="top:1180px">psicologakarentrujillo.com.mx</div>')
BOUND=[6.5,10.35,18.2,29.5,40.4,46.4,55.3]
