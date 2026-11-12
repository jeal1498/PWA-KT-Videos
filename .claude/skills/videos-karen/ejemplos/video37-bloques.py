# Escenario animado del 37 (estilo del 36). Uso: python3 -I video37-bloques.py <trabajo>  (spec.json ya recortado; tiempos del video recortado)
import json, sys
W = sys.argv[1]
S = 'stroke="#2E2545" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"'
def pill(i, txt, cx, top, size=34, cls=''):
    return f'<div class="zw" style="left:{cx-330}px;top:{top}px"><div id="{i}" class="zp {cls}" style="position:static;display:inline-block;font-size:{size}px">{txt}</div></div>'
svg = f'''<svg width="960" height="450" viewBox="0 0 960 450"><defs><filter id="rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence id="rtb" type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="1"/><feDisplacementMap in="SourceGraphic" scale="5"/></filter></defs>
<g filter="url(#rough)">
[[amigas|zA1|170]][[amigas|zA2|170]][[amigas|zA3|170]][[globo|zGb|230]]
<g id="zK1" class="zo"><circle r="55" fill="#fff" {S}/></g><g id="zK2" class="zo"><rect x="-55" y="-55" width="110" height="110" rx="16" fill="#F9DEE3" {S}/></g><g id="zK3" class="zo"><path d="M0 -62L60 48H-60Z" fill="#fff" {S}/></g>
<g id="zFg" class="zo"><rect x="-36" y="-190" width="72" height="190" rx="36" fill="#fff" {S}/><circle cx="0" cy="-226" r="30" fill="#fff" {S}/></g>
[[mascara|zMk|96]][[globo|zB1|110]][[globo|zB2|110]][[globo|zB3|110]]
[[ojo|zOj|210]][[amigas|zAm|230]]
<g id="zBr" class="zo"><path d="M-40 -62V-84Q-40 -100 -24 -100H24Q40 -100 40 -84V-62" fill="none" {S}/><rect x="-100" y="-62" width="200" height="130" rx="20" fill="#fff" {S}/><path d="M-100 -2H100" fill="none" {S}/><rect x="-14" y="-16" width="28" height="30" rx="6" fill="#F9DEE3" {S}/></g>
[[x|zXm|130]]
<g id="zBt" class="zo"><rect x="-150" y="-62" width="300" height="124" rx="26" fill="#fff" {S}/><rect x="150" y="-24" width="24" height="48" rx="8" fill="#2E2545"/><rect id="zBf" x="-136" y="-48" width="272" height="96" rx="16" fill="#F9DEE3"/></g>
<path id="zWl" class="zl" d="M20 170H940" pathLength="1" fill="none" {S}/>
<g id="zIcT" class="zo"><path d="M410 170L472 84L508 122L546 170Z" fill="#fff" {S}/></g><g id="zIcB" class="zo"><path d="M346 170H612L648 250L572 360L452 396L362 300Z" fill="#F9DEE3" {S}/></g>
<g id="zNe" class="zo"><circle r="64" fill="#fff" {S}/><text y="26" text-anchor="middle" font-family="Outfit,sans-serif" font-weight="700" font-size="84" fill="#2E2545">≠</text></g>
[[informe|zIn|230]]<path id="zLk" class="zl" d="M510 215H395" pathLength="1" fill="none" {S}/>
[[globo|zS1|120]][[celular|zS2|120]][[amigas|zS3|120]]
</g></svg>'''
html = '''<style>#stg{position:absolute;left:54px;top:920px;width:960px;height:450px;background:#C6BCE2;border:6px solid #2E2545;border-radius:38px;box-shadow:8px 10px 0 rgba(46,37,69,.55);overflow:hidden;opacity:0}
#stg svg{position:absolute;left:0;top:0}.zo{opacity:0}.zl{stroke-dasharray:1;stroke-dashoffset:1;opacity:0}
.zw{position:absolute;width:660px;text-align:center}
.zp{white-space:nowrap;background:#F5E7D6;border:5px solid #2E2545;border-radius:24px;font:700 34px/1 Outfit,sans-serif;color:#2E2545;padding:10px 22px;box-shadow:5px 6px 0 #F9DEE3;opacity:0}</style>
''' + svg + ''.join([
 pill('zP1','Tiene amigas',480,330,38), pill('zP2','¿Te suena?',480,330,44),
 pill('zP3','No siempre igual',480,24,38), pill('zP4','Mujeres adultas',480,350,38),
 pill('zP5','Adaptarse',480,24,38), pill('zP6','Imitar',250,330,38), pill('zP7','Ensayar',710,330,38), pill('zP8','Pasar desapercibida',480,24,38),
 pill('zP9','Camuflaje social',480,24,50), pill('zP10','3 mitos, 3 realidades',480,190,50),
 pill('zMt','Mito',480,24,40), pill('zRe','Realidad',480,24,40),
 pill('zL1','Lo aprendió',250,330,36), pill('zR1','Agota',700,330,36),
 pill('zL2','Las mantiene',250,330,36), pill('zR2','Esfuerzo',700,330,36),
 pill('zL3','Rinde bien',250,330,36), pill('zR3','Se agota',700,330,36),
 pill('zF1','Facilidad',720,60,40), pill('zF2','Esfuerzo',730,250,44),
 pill('zI1','Me identifico',300,330,38), pill('zI2','Diagnóstico',660,330,38),
 pill('zE1','Evaluación integral',480,24,38), pill('zE2','Tu historia',700,120,36), pill('zE3','Tu presente',700,250,36),
 pill('zO1','ADOS-2',650,150,62), pill('zT1','Una tarea',480,24,40), pill('zT2','¿Cuáles te agotan?',480,24,40)])
def myth(n, obj, size, ts):
    # ts: mito, x, real, mover, bat, d0, d1, izq, der, fuera
    mito, xx, real, mover, bat, d0, d1, izq, der, out = ts
    return f'''
P('#zBf',{{scaleX:1,fill:'#F9DEE3'}},{mito-.1});
POP('#{obj}',{mito+.1});POP('#zMt',{mito});
POP('#zXm',{xx});
OUT('#zMt',{real-.1},.2);OUT('#zXm',{real},.25);POP('#zRe',{real+.1});
TO('#{obj}',{{x:270,y:215,scale:{size[1]}}},{mover},.6,'power2.inOut');
FR('#zBt',{{scale:0,opacity:0,x:690,y:215}},{{scale:.8,opacity:1,x:690,y:215}},{bat},.55,'back.out(1.7)');
POP('#zL{n}',{izq});
TO('#zBf',{{scaleX:.1}},{d0},{d1-d0},'power1.inOut');TO('#zBf',{{fill:'#E8707C'}},{d1-.6},.5);
POP('#zR{n}',{der});
OUT('#zL{n}',{out});OUT('#zR{n}',{out});OUT('#zRe',{out});OUT('#zBt',{out});OUT('#{obj}',{out});
'''
js = r'''
const P=(s,v,t)=>tl.set(s,v,t);
const TO=(s,v,t,d,e)=>tl.to(s,Object.assign({duration:d,ease:e||'power2.out'},v),t);
const FR=(s,a,v,t,d,e)=>tl.fromTo(s,a,Object.assign({duration:d,ease:e||'power2.out',immediateRender:false},v),t);
const POP=(s,t,k)=>FR(s,{scale:0,opacity:0},{scale:k||1,opacity:1,duration:.55,ease:'elastic.out(1,.5)'},t,.55,'elastic.out(1,.5)');
const OUT=(s,t,d)=>TO(s,{opacity:0},t,d||.3,'power2.in');
const DRAW=(s,t,d)=>{P(s,{opacity:1},t);FR(s,{strokeDashoffset:1},{strokeDashoffset:0},t,d||.5,'power2.inOut');};
const SHOW=t=>FR('#stg',{opacity:0,y:60},{opacity:1,y:0},t,.5,'back.out(1.5)');
const HIDE=t=>TO('#stg',{opacity:0,y:60},t,.4,'power2.in');
P('.zo',{transformOrigin:'50% 50%'},0);P('#zin',{scale:1.3,x:517-1.3*480,y:283-1.3*273,transformOrigin:'0 0'},0);
P('#zBf',{transformOrigin:'0% 50%'},0);
P('#zA1',{x:260,y:215},0);P('#zA2',{x:480,y:215},0);P('#zA3',{x:700,y:215},0);P('#zGb',{x:480,y:200},0);
P('#zK1',{x:300,y:215},0);P('#zK2',{x:480,y:215},0);P('#zK3',{x:660,y:215},0);
P('#zFg',{x:480,y:403},0);P('#zMk',{x:480,y:157},0);P('#zB1',{x:330,y:200},0);P('#zB2',{x:640,y:200},0);P('#zB3',{x:330,y:285},0);
P('#zOj',{x:480,y:215},0);P('#zAm',{x:480,y:215},0);P('#zBr',{x:480,y:215},0);P('#zXm',{x:480,y:215},0);
P('#zNe',{x:480,y:215},0);P('#zIn',{x:480,y:215},0);P('#zS1',{x:190,y:215},0);P('#zS2',{x:340,y:215},0);P('#zS3',{x:490,y:215},0);
SHOW(1.85);
// A: amigas (1.85 a 3.6)
POP('#zA1',2.45);POP('#zA2',2.75);POP('#zA3',3.05);POP('#zP1',3.0);
OUT('#zA1',3.6);OUT('#zA2',3.6);OUT('#zA3',3.6);OUT('#zP1',3.6);
// B: ¿has escuchado algo así?
POP('#zGb',3.8);POP('#zP2',4.9);OUT('#zGb',5.5);OUT('#zP2',5.5);
// C: no siempre igual, en mujeres adultas
POP('#zK1',6.6);POP('#zK2',7.1);POP('#zK3',7.6);POP('#zP3',6.6);
TO('#zK1',{opacity:.3},9.7,.3);TO('#zK3',{opacity:.3},9.7,.3);TO('#zK2',{scale:1.5},9.7,.5,'back.out(2)');POP('#zP4',9.8);
OUT('#zK1',11.1);OUT('#zK2',11.1);OUT('#zK3',11.1);OUT('#zP3',11.1);OUT('#zP4',11.1);
// D: la figura se adapta
FR('#zFg',{scale:.2,opacity:0},{scale:1.2,opacity:1},11.5,.7,'back.out(1.6)');POP('#zP5',13.0);
FR('#zMk',{y:-60,scale:.3,opacity:0},{y:157,scale:1.1,opacity:1},14.7,.5,'bounce.out');POP('#zP6',14.8);
POP('#zB1',16.8);POP('#zB2',17.4);POP('#zB3',17.9);POP('#zP7',16.9);
OUT('#zP5',18.9);OUT('#zP6',18.9);OUT('#zP7',18.9);OUT('#zB1',18.9);OUT('#zB2',18.9);OUT('#zB3',18.9);
POP('#zP8',19.0);TO('#zFg',{opacity:.25},19.2,.8);TO('#zMk',{opacity:.25},19.2,.8);
OUT('#zP8',20.2);
// E: camuflaje social
POP('#zP9',21.4);OUT('#zP9',23.1);OUT('#zFg',23.1);OUT('#zMk',23.1);
// F: tres mitos
POP('#zP10',23.5);OUT('#zP10',25.3);
''' + myth(1,'zOj',(210,.85),(26.1,27.7,29.0,29.3,30.3,31.7,35.1,30.6,34.4,35.9)) \
    + myth(2,'zAm',(230,.8),(36.8,38.6,39.5,39.8,40.9,41.9,44.9,41.3,44.3,45.5)) \
    + myth(3,'zBr',(1,.85),(46.4,48.5,49.4,49.7,50.5,53.7,57.3,51.3,54.4,57.9)) + r'''
// G: iceberg
DRAW('#zWl',58.2,.6);POP('#zIcT',59.3);POP('#zF1',60.3);
FR('#zIcB',{scale:.2,opacity:0,y:-40},{scale:1,opacity:1,y:0},62.1,.7,'back.out(1.4)');POP('#zF2',63.1);
OUT('#zWl',65.3);OUT('#zIcT',65.3);OUT('#zIcB',65.3);OUT('#zF1',65.3);OUT('#zF2',65.3);
// H: identificarte no es diagnóstico
POP('#zI1',66.0);P('#zOj',{x:300,y:215,scale:1},66.5);P('#zAm',{x:480,y:215,scale:1},66.5);P('#zBr',{x:660,y:215,scale:1},66.5);POP('#zOj',66.8,.6);POP('#zAm',67.2,.55);POP('#zBr',67.6,.7);OUT('#zOj',70.5);OUT('#zAm',70.5);OUT('#zBr',70.5);POP('#zNe',70.6);POP('#zI2',72.8);
OUT('#zI1',73.8);OUT('#zNe',73.8);OUT('#zI2',73.8);
// I: evaluación clínica integral
POP('#zIn',74.1);POP('#zE1',75.1);
TO('#zIn',{x:270},75.9,.5,'power2.inOut');POP('#zE2',76.6);POP('#zE3',78.4);
OUT('#zE1',81.5);OUT('#zE2',81.5);OUT('#zE3',81.5);
// J: ADOS-2 es una parte
POP('#zO1',83.3);DRAW('#zLk',84.7,.5);
OUT('#zO1',86.4);OUT('#zIn',86.4);OUT('#zLk',86.4);
// K: situaciones que agotan
POP('#zT1',86.9);OUT('#zT1',88.8);
POP('#zS1',89.4);POP('#zS2',89.9);POP('#zS3',90.3);
P('#zBf',{scaleX:1,fill:'#F9DEE3'},87.1);
FR('#zBt',{scale:0,opacity:0,x:715,y:215},{scale:.8,opacity:1,x:715,y:215},87.2,.55,'back.out(1.7)');
TO('#zBf',{scaleX:.1},90.9,1.6,'power1.inOut');TO('#zBf',{fill:'#E8707C'},91.8,.5);POP('#zT2',91.0);
HIDE(92.9);
'''
sp = json.load(open(W + '/spec.json'))
sp.update({'layout': 'split', 'escenas': [], 'pastillas': [], 'destacados': [], 'referencias': [], 'zooms': []})
sp['custom'] = {'ini': 1.85, 'fin': 92.95, 'html': html, 'js': js}
json.dump(sp, open(W + '/spec.json', 'w'), ensure_ascii=False, indent=1)
print('ok')
