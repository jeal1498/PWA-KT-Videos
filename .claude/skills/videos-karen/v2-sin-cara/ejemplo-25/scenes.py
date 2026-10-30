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

def TT(h,top=430,fs=92): return f'<div class="t" style="top:{top}px;font-size:{fs}px">{h}</div>'
def ST(t): return f'<span class="st">{t}</span>'
moon=lambda s: f'<g transform="scale({s}) translate(-12,-12)"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" fill="{A}" stroke="{D}" stroke-width="{round(8/s,2)}" stroke-linejoin="round"/></g>'
bolt=f'<path d="M25 -105L-55 25H-5L-25 105L60 -30H10Z" fill="{A}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/>'
weight=f'<path d="M-45 -45V-75a45 45 0 0 1 90 0V-45" fill="none" stroke="{D}" stroke-width="12" stroke-linecap="round"/><path d="M-95 85L-62 -50H62L95 85Z" fill="{L}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/><path d="M0 -10v60m-22 -22l22 22 22 -22" fill="none" stroke="{D}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
book=f'<rect x="-75" y="-95" width="150" height="190" rx="22" fill="{R}" stroke="{D}" stroke-width="8"/><path d="M-45 -45h90M-45 -10h90M-45 25h50" stroke="{D}" stroke-width="8" stroke-linecap="round"/><path d="M52 40l36 -36 22 22 -36 36 -28 6z" fill="{L}" stroke="{D}" stroke-width="7" stroke-linejoin="round"/>'
house=f'<path d="M-95 15L0 -75L95 15H72V85H-72V15Z" fill="{L}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/><rect x="-22" y="30" width="44" height="55" rx="8" fill="{A}" stroke="{D}" stroke-width="7"/>'
brief=f'<path d="M-36 -35v-34h72v34" fill="none" stroke="{D}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><rect x="-92" y="-38" width="184" height="124" rx="22" fill="{R}" stroke="{D}" stroke-width="8"/><path d="M-92 14h184" stroke="{D}" stroke-width="7"/><rect x="-14" y="2" width="28" height="26" rx="6" fill="{A}" stroke="{D}" stroke-width="6"/>'
friends=f'<circle cx="-42" cy="-35" r="36" fill="{L}" stroke="{D}" stroke-width="8"/><circle cx="42" cy="-35" r="36" fill="{R}" stroke="{D}" stroke-width="8"/><path d="M-100 80a58 52 0 0 1 116 0Z" fill="{L}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/><path d="M-16 80a58 52 0 0 1 116 0Z" fill="{R}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/>'
def pillt(x,y,w,h,fill,cls,dash=False): return f'<g class="{cls}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h//2}" fill="{fill}" stroke="{D}" stroke-width="7"/></g>'

# 1 gancho: la cocina
sc('s1',0,5.8, chip('Neuropsicóloga Karen Trujillo · Cédula 11009616',A,300).replace('class="chip"','class="chip ced"')+
 TT(f'<span class="w">¿Para</span> <span class="w">qué</span> {ST("entraste")}<span class="w">?</span>',390,86)+
 av('solemn','a1 d1','left:300px;top:830px;width:480px;height:480px')+av('duda','a1 d2','left:300px;top:830px;width:480px;height:480px;opacity:0')+
 svg(f'<g class="fr"><rect x="50" y="790" width="230" height="530" rx="26" fill="{L}" stroke="{D}" stroke-width="8"/><path d="M50 990H280" stroke="{D}" stroke-width="8"/><path d="M245 880v60M245 1050v90" stroke="{D}" stroke-width="10" stroke-linecap="round"/></g>'+
     f'<g class="sv"><rect x="800" y="1090" width="230" height="230" rx="16" fill="{R}" stroke="{D}" stroke-width="8"/><rect x="800" y="1090" width="230" height="34" rx="12" fill="{A}" stroke="{D}" stroke-width="8"/><rect x="832" y="1160" width="166" height="120" rx="14" fill="{D}"/><path d="M845 1146h140" stroke="{D}" stroke-width="10" stroke-linecap="round"/><path d="M835 1052h160l-14 38H849z" fill="{L}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/></g>'+
     f'<path d="M0 1320H1080" stroke="{D}" stroke-width="8"/>',
     T(690,900,'?',130,A,'qm1')+T(840,1010,'?',90,A,'qm2')+T(180,780,'?',100,A,'qm3'))+
 '<div class="q why" style="top:1350px;font-size:70px"><span class="st">¿Por qué pasa?</span></div>')
# 2 un olvido, cuatro causas
nodes=[(190,830,'sueño',L),(890,830,'estrés',R),(190,1250,'ansiedad',A),(890,1250,'carga',L)]
br=''.join(f'<path class="br{i}" d="M540 1040L{x} {y}" stroke="{A}" stroke-width="9" stroke-linecap="round" fill="none"/>' for i,(x,y,t,c) in enumerate(nodes))
nd=''.join(f'<g class="nd{i}"><circle cx="{x}" cy="{y}" r="88" fill="{c}" stroke="{D}" stroke-width="8"/></g>' for i,(x,y,t,c) in enumerate(nodes))
sc('s2',5.8,9.3,TT(f'Un olvido,<br>{ST("cuatro causas")}',420,88)+
 svg(br+f'<g class="hub"><circle cx="540" cy="1040" r="115" fill="{A}" stroke="{D}" stroke-width="9"/></g>'+nd,
     T(540,1055,'olvido',44,D,'hubt')+''.join(T(x,y+12,t,32,D,f'ndt{i}') for i,(x,y,t,c) in enumerate(nodes))))
# 3 mala noche
stars=''.join(f'<path class="stz" d="M{x} {y-26}l7 19 19 7-19 7-7 19-7-19-19-7 19-7z" fill="{A}"/>' for x,y in [(150,780),(430,830),(460,1100),(120,1160)])
sc('s3',9.3,14.6,TT(f'Mala {ST("noche")}')+
 svg(f'<g class="mo"><g transform="translate(290,960)">{moon(14)}</g></g>'+stars+
     f'<rect class="bfr" x="560" y="760" width="130" height="520" rx="40" fill="none" stroke="{A}" stroke-width="8"/><rect class="bfr" x="800" y="760" width="130" height="520" rx="40" fill="none" stroke="{A}" stroke-width="8"/>'+
     f'<rect class="bf1" x="568" y="768" width="114" height="504" rx="34" fill="{G}"/><rect class="bf2" x="808" y="768" width="114" height="504" rx="34" fill="{G}"/>',
     T(625,1340,'Atención',36,A,'bl1')+T(865,1340,'Memoria',36,A,'bl2')+T(330,1200,'z z z',70,A,'zz')))
# 4 estrés
notes=[(400,930,'correo',L),(570,970,'pagos',A),(420,1090,'junta',R),(590,1130,'cuentas',L)]
nts=''.join(f'<g class="nt{i}"><rect x="{x-20}" y="{y}" width="190" height="110" rx="26" fill="{c}" stroke="{D}" stroke-width="7"/></g>' for i,(x,y,t,c) in enumerate(notes))
sc('s4',14.6,20.4,TT(f'Semana de {ST("estrés")}',430,88)+
 svg(f'<g class="hd"><circle cx="540" cy="1060" r="270" fill="{R}" stroke="{D}" stroke-width="9"/></g>'+nts+
     f'<g class="dt"><rect x="830" y="1000" width="180" height="90" rx="40" fill="{A}" stroke="{D}" stroke-width="7"/></g>',
     T(540,850,'mente',40,D,'hdt')+''.join(T(x+75,y+66,t,34,D,f'ntt{i}') for i,(x,y,t,c) in enumerate(notes))+T(920,1058,'dato',34,D,'dtt')))
# 5 ansiedad
bub=[(60,780,400,'¿y si sale mal?',L),(600,800,420,'ya es tarde',R),(70,1250,420,'qué pendiente',A),(560,1260,440,'no puedo parar',L)]
bb=''.join(f'<g class="bb{i}"><rect x="{x}" y="{y}" width="{w}" height="100" rx="50" fill="{c}" stroke="{D}" stroke-width="7"/></g>' for i,(x,y,w,t,c) in enumerate(bub))
sc('s5',20.4,25.1,TT(f'Con {ST("ansiedad")}')+
 svg(f'<g class="rc"><rect x="370" y="1020" width="340" height="140" rx="44" fill="{A}" stroke="{D}" stroke-width="8"/></g>'+bb,
     T(540,1105,'tu recuerdo',42,D,'rct')+''.join(T(x+w//2,y+64,t,34,D,f'bt{i}') for i,(x,y,w,t,c) in enumerate(bub))))
# 6 sobrecarga
tw=''.join(f'<g class="tc{i}"><rect x="{430+(i%2)*20}" y="{1230-i*105}" width="470" height="92" rx="34" fill="{[L,R,A,L,R][i]}" stroke="{D}" stroke-width="7"/></g>' for i in range(5))
sc('s6',25.1,29.8,TT(f'Con {ST("sobrecarga")}',430,88)+
 av('cansada','a6 u6','left:10px;top:1000px;width:400px;height:400px')+
 svg(f'<g class="tw">{tw}</g>',''.join(T(665+(i%2)*20,1290-i*105,'tarea',36,D,f'tt{i}') for i in range(5))))
# 7 qué me pasa
pl4=[(60,740,'sueño',L),(60,830,'estrés',R),(60,920,'ansiedad',A),(60,1010,'carga',L)]
p4=''.join(pillt(x,y,360,76,c,f'pp{i}') for i,(x,y,t,c) in enumerate(pl4))
sc('s7',29.8,35.4,TT(f'¿Qué me {ST("pasa")}?')+
 av('preocupada','a7 u7','left:40px;top:1110px;width:330px;height:330px')+
 svg(p4+f'<path class="ar7" d="M440 880H520m-26 -24l26 24-26 24" fill="none" stroke="{A}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'+
     f'<g class="bgq"><rect x="540" y="760" width="480" height="260" rx="60" fill="{A}" stroke="{D}" stroke-width="8"/></g>',
     ''.join(T(x+180,y+50,t,36,D,f'ppt{i}') for i,(x,y,t,c) in enumerate(pl4))+T(780,865,'¿Qué me',60,D,'bq1')+T(780,945,'pasa?',60,D,'bq2'))+
 '<div class="cap2 ao" style="left:400px;right:50px;top:1180px;font-size:46px">Un olvido aislado no dice mucho</div>')
# 8 años, tres lugares
cds=[(60,'casa',house),(395,'trabajo',brief),(730,'amigos',friends)]
c8=''.join(icard(x,1000,290,290,tr(x+145,1125,ic),f'k{i}') for i,(x,n,ic) in enumerate(cds))
c8t=''.join(T(x+145,1260,n,34,D,f'kl{i}') for i,(x,n,ic) in enumerate(cds))
c8c=''.join(ck(x+250,1030,30,f'kc{i}') for i,(x,n,ic) in enumerate(cds))
tk=''.join(f'<circle class="tn{i}" cx="{150+i*260}" cy="860" r="24" fill="{A}" stroke="{D}" stroke-width="7"/>' for i in range(4))
sc('s8',35.4,45.0,TT(f'Llevan {ST("años")}')+
 svg(f'<path class="tl8" d="M100 860H980" stroke="{A}" stroke-width="10" stroke-linecap="round" fill="none"/>'+tk+c8+c8c+
     f'<g class="vd"><rect x="150" y="1330" width="780" height="100" rx="50" fill="{G}" stroke="{D}" stroke-width="8"/></g>',
     T(150,800,'hoy',34,A,'tt0')+T(670,800,'años',34,A,'tt2')+c8t+T(540,1397,'Afecta tu vida diaria',44,'#fff','vdt')))
# 9 profesional
sc('s9',45.0,52.4,TT(f'Con un<br>{ST("profesional")}',420,88)+
 svg(f'<g class="fo"><path d="M60 845q0 -45 45 -45h125l40 55H520q40 0 40 40V1120q0 40 -40 40H105q-45 0 -45 -40Z" fill="{R}" stroke="{D}" stroke-width="8" stroke-linejoin="round"/></g>'+
     f'<g class="lp"><circle cx="800" cy="930" r="120" fill="rgba(245,231,214,.14)" stroke="{A}" stroke-width="14"/><path d="M888 1018L985 1115" stroke="{A}" stroke-width="24" stroke-linecap="round"/></g>'+
     ''.join(pillt(60+i*315,1260,290,84,c,f'ec{i}') for i,c in enumerate([L,R,A])),
     T(310,1010,'Tu historia',54,D,'fot')+''.join(T(205+i*315,1315,t,32,D,f'ect{i}') for i,t in enumerate(['sueño','estrés','ansiedad']))+T(540,1240,'otras explicaciones',36,A,'ecl')))
# 10 mientras tanto
ics10=[moon(9.5).replace('<g ','<g ',1),weight,book]; lab10=['Duerme','Baja una carga','Anota']
c10=''.join(icard(60+i*330,780,300,400,tr(60+i*330+150,950,ics10[i]),f'z{i}') for i in range(3))
sc('s10',52.4,59.3,TT(f'Mientras {ST("tanto")}')+svg(c10,''.join(T(210+i*330,1120,lab10[i],34,D,f'zl{i}') for i in range(3))))
# 11 no todo olvido es TDAH
sc('s11',59.3,63.5,TT(f'No todo olvido<br>{ST("es TDAH")}',420,104)+
 av('sonrisa','a11 s11','left:300px;top:880px;width:480px;height:480px')+
 '<div class="cap2 ao2" style="top:1370px;font-size:50px;color:#fff">Sin asustarte</div>')
# 12 cierre
cd12=''.join(icard(60+i*500,760,460,330,tr(60+i*500+230,925,[moon(8),bolt][i]),f'g{i}') for i in range(2))
sc('s12',63.5,DUR,'<div class="t t1" style="top:430px;text-align:center;font-size:84px">¿Cuándo olvidas <span class="st">más</span>?</div>'+
 '<div class="t t2" style="top:430px;text-align:center;font-size:80px">Este video <span class="st">orienta</span> y no diagnostica.</div>'+
 av('sonrisa2','cz','left:330px;top:1100px;width:340px;height:340px')+
 svg(cd12,T(290,1060,'Poco sueño',40,D,'gt0')+T(790,1060,'Estrés',40,D,'gt1'))+
 '<div class="web" style="top:1010px">psicologakarentrujillo.com.mx</div>')
BOUND=[5.8,9.3,14.6,20.4,25.1,29.8,35.4,45.0,52.4,59.3,63.5]
