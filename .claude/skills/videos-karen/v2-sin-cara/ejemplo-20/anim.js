var tl0=gsap.timeline({paused:true});
/* posiciones escritas con la voz anterior → tiempos de la voz nueva (interpolación por palabra) */
var KN=__KN__;function W(t){for(var i=1;i<KN.length;i++){if(t<=KN[i][0]){var a=KN[i-1],b=KN[i];return a[1]+(t-a[0])*(b[1]-a[1])/Math.max(b[0]-a[0],1e-6);}}return KN[KN.length-1][1]+(t-KN[KN.length-1][0]);}
function wrap(f){return function(){var a=[].slice.call(arguments);var i=a.length-1;if(typeof a[i]==='number')a[i]=W(a[i]);return tl0[f].apply(tl0,a);};}
var tl={to:wrap('to'),from:wrap('from'),fromTo:wrap('fromTo'),set:wrap('set')};
var $=function(s){return document.querySelectorAll(s);};
function draw(sel,t,dur){$(sel).forEach(function(p){var L=p.getTotalLength();gsap.set(p,{strokeDasharray:L,strokeDashoffset:L});tl.to(p,{strokeDashoffset:0,duration:dur||0.6,ease:'power2.inOut'},t);});}
function pop(sel,t,st){tl.fromTo(sel,{scale:0,transformOrigin:'50% 50%'},{scale:1,duration:0.7,ease:'elastic.out(1,0.55)',stagger:st||0},t);}
function up(sel,t,o){tl.fromTo(sel,{opacity:0,y:36},Object.assign({opacity:1,y:0,duration:0.5,ease:'back.out(1.6)'},o||{}),t);}
function stick(sel,t){tl.fromTo(sel,{scale:0,rotation:-14},{scale:1,rotation:-2.5,duration:0.8,ease:'elastic.out(1,0.5)'},t);}
function fade(sel,t){tl.fromTo(sel,{opacity:0},{opacity:1,duration:0.25},t);}
function enter(sel,t){tl.fromTo(sel,{y:140,scaleY:0.85,transformOrigin:'50% 100%'},{y:0,scaleY:1,duration:0.75,ease:'back.out(1.8)'},t);}
function breathe(sel,t,n){tl.to(sel,{scaleY:1.018,transformOrigin:'50% 100%',duration:0.9,repeat:n,yoyo:true,ease:'sine.inOut'},t);}
function swap(a,b,t){tl.to(a,{opacity:0,duration:0.25},t);tl.to(b,{opacity:1,duration:0.25},t);}
/* trazo vibrando 12 veces por segundo */
var turb=document.getElementById('turb');for(var k=0;k<Math.ceil(__DUR__*12);k++){tl0.set(turb,{attr:{seed:(k%6)+1}},k/12);}
/* garabatos de fondo */
gsap.utils.toArray('.sp').forEach(function(e,i){pop(e,0.4+i*0.15);tl.to(e,{rotation:(i%2?18:-18),transformOrigin:'50% 50%',duration:1.2,repeat:60,yoyo:true,ease:'sine.inOut'},1.1+i*0.2);});
draw('.sq',0.8,0.6);
/* escenas: entrada y salida suaves */
[['#s1',0,4.6],['#s2',4.7,8.2],['#s3',8.3,12.9],['#s4',13.0,18.9],['#s5',19.0,22.9],['#s6',23.0,24.9],['#s7',25.0,35.4],['#s8',35.5,43.3],['#s9',43.4,51.0],['#s10',51.1,61.2],['#s11',61.3,67.0],['#s12',67.1,71.1],['#s13',71.2,79.9]].forEach(function(s){
 tl.fromTo(s[0],{opacity:0},{opacity:1,duration:0.2},s[1]); if(s[2]<79) tl0.to(s[0],{opacity:0,duration:0.22},W(s[2])-0.22);});
function spin(sel,t,deg,dur,o){tl.fromTo(sel,Object.assign({rotation:0},o||{}),Object.assign({rotation:deg,duration:dur,ease:'none'},o||{}),t);}
/* 1 gancho */
up('#s1 .ced',0.1,{duration:0.4});up('#s1 .w',0.25,{stagger:0.14,y:50});stick('#s1 .st',1.1);
enter('#s1 .a1',0.5);fade('#s1 .a1',0.5);breathe('#s1 .a1',1.3,3);
pop('#s1 .ph',0.8);pop('#s1 .bd',1.5);fade('#s1 .bdt',1.6);
tl.to('#s1 .ph,#s1 .bd,#s1 .bdt',{x:5,duration:0.06,repeat:5,yoyo:true},1.9);
pop('#s1 .ck1',3.5);
tl.fromTo('#s1 .hm',{rotation:0,transformOrigin:'750px 1330px'},{rotation:1080,duration:1.0,ease:'power1.in',transformOrigin:'750px 1330px'},3.6);
tl.fromTo('#s1 .hh',{rotation:0,transformOrigin:'750px 1330px'},{rotation:90,duration:1.0,ease:'power1.in',transformOrigin:'750px 1330px'},3.6);
fade('#s1 .p10',3.7);fade('#s1 .t10',3.75);tl.to('#s1 .p10,#s1 .t10',{opacity:0,duration:0.2},4.2);fade('#s1 .p1h',4.25);fade('#s1 .t1h',4.3);
tl.to('#s1 .a1',{rotation:-4,transformOrigin:'50% 100%',duration:0.4,yoyo:true,repeat:1,ease:'sine.inOut'},3.6);
/* 2 escurrió */
up('#s2 .t',4.8);stick('#s2 .st',5.5);enter('#s2 .aT',5.0);fade('#s2 .aT',5.0);breathe('#s2 .aT',5.8,2);
pop('#s2 .ck2',6.3);
gsap.utils.toArray('#s2 .dr').forEach(function(e,i){tl.fromTo(e,{opacity:0,y:0},{opacity:1,y:150,duration:0.9,ease:'power1.in'},6.7+i*0.25);tl.to(e,{opacity:0,duration:0.15},7.5+i*0.25);});
tl.fromTo('#s2 .sand',{scaleY:0,transformOrigin:'800px 1330px'},{scaleY:1,duration:1.0,ease:'power2.out'},7.0);
tl.to('#s2 .ck2',{rotation:-6,transformOrigin:'800px 980px',duration:0.9,ease:'sine.inOut'},6.8);
up('#s2 .q',6.6);stick('#s2 .q .st',7.2);
/* 3 ahora / no ahora */
up('#s3 .chip',8.4);up('#s3 .t',8.8);stick('#s3 .st',9.9);
pop('#s3 .n1',11.2);fade('#s3 .l1',11.5);pop('#s3 .n2',12.2);fade('#s3 .l2',12.6);
tl.to('#s3 .n1',{scale:1.05,transformOrigin:'285px 980px',duration:0.4,yoyo:true,repeat:1},11.7);
/* 4 calcular / cambiar */
up('#s4 .chip',13.1);pop('#s4 .c1',13.3);fade('#s4 .l1',14.1);pop('#s4 .qm',14.4);
tl.fromTo('#s4 .c1 line',{rotation:0,transformOrigin:'285px 880px'},{rotation:360,duration:2,ease:'none',transformOrigin:'285px 880px'},14.2);
pop('#s4 .c2',15.3);fade('#s4 .l2',16.4);draw('#jmp',16.0,0.7);
up('#s4 .q',17.5);stick('#s4 .q .st',17.7);
/* 5 impuntual */
up('#s5 .t',19.1);stick('#s5 .st',19.9);enter('#s5 .aG',19.3);fade('#s5 .aG',19.3);
tl.to('#s5 .aG',{x:6,duration:0.07,repeat:25,yoyo:true},20.0);
pop('#s5 .ck5',19.8);tl.fromTo('#s5 .hm',{rotation:0,transformOrigin:'880px 830px'},{rotation:1440,duration:3,ease:'none',transformOrigin:'880px 830px'},19.8);
up('#s5 .q',21.1);stick('#s5 .q .st',21.9);
/* 6 tres ideas */
up('#s6 .t',23.1);stick('#s6 .st',23.5);draw('#p3l',23.4,0.8);pop('#s6 .pn',23.8,0.25);tl.fromTo('#s6 .pnt',{opacity:0},{opacity:1,duration:0.2,stagger:0.25},24.0);
/* 7 mide */
up('#s7 .pill',25.1);pop('#s7 .sw',26.0);spin('#s7 .swh',27.0,720,3.0,{transformOrigin:'900px 440px'});
gsap.utils.toArray('#s7 [class^=rw]').forEach(function(e,i){pop(e,[29.0,29.6,30.2][i]);});
tl.fromTo('#s7 .hd',{opacity:0},{opacity:1,duration:0.3,stagger:0.2},28.9);
[[30.9,0],[31.7,1],[32.5,2]].forEach(function(a){fade('#s7 .rt'+a[1],a[0]);fade('#s7 .rc'+a[1],a[0]+0.2);tl.fromTo('#s7 .rr'+a[1],{opacity:0,scale:0.4,transformOrigin:'50% 50%'},{opacity:1,scale:1,duration:0.5,ease:'elastic.out(1,0.5)'},a[0]+0.9);});
up('#s7 .q',33.3);stick('#s7 .q .st',33.8);
/* 8 hacia atrás */
up('#s8 .pill',35.6);draw('#tll',37.0,1.4);draw('#tla',38.3,0.3);pop('#s8 .g0',38.4);fade('#s8 .tp',38.6);
pop('#s8 .g1',40.0);fade('#s8 .tq1',40.2);pop('#s8 .g2',40.5);fade('#s8 .tq2',40.7);pop('#s8 .g3',40.9);fade('#s8 .tq3',41.1);
pop('#s8 .mg',41.8);fade('#s8 .tm',42.1);up('#s8 .q',37.4);stick('#s8 .q .st',37.9);
/* 9 sonido */
up('#s9 .pill',43.5);
function ring(c,t){tl.fromTo(c+' .bl',{rotation:0},{rotation:14,duration:0.08,repeat:11,yoyo:true,ease:'sine.inOut'},t);}
pop('#s9 .b1',46.2);fade('#s9 .x1',46.7);ring('#s9 .b1',46.9);tl.fromTo('#s9 .rg0,#s9 .rg1',{opacity:0},{opacity:1,duration:0.2,repeat:5,yoyo:true},46.9);
draw('#bl3',47.6,0.8);pop('#s9 .b2',48.0);fade('#s9 .x2',48.6);ring('#s9 .b2',49.3);tl.fromTo('#s9 .rg2,#s9 .rg3',{opacity:0},{opacity:1,duration:0.2,repeat:5,yoyo:true},49.3);
up('#s9 .q',46.5);stick('#s9 .q .st',46.9);
/* 10 ojo */
up('#s10 .chip',51.2);up('#s10 .t',51.6);stick('#s10 .st',55.8);
enter('#s10 .aD',52.0);fade('#s10 .aD',52.0);breathe('#s10 .aD',52.8,3);
tl.to('#s10 .aD',{rotation:4,transformOrigin:'50% 100%',duration:0.5,yoyo:true,repeat:1},54.0);
pop('#s10 .i3',58.1);fade('#s10 .lb3',58.5);pop('#s10 .i4',59.2);fade('#s10 .lb4',59.5);pop('#s10 .i5',60.0);fade('#s10 .lb5',60.3);
/* 11 sistema */
up('#s11 .t',61.4);stick('#s11 .st',62.3);enter('#s11 .aQ',61.5);fade('#s11 .aQ',61.5);breathe('#s11 .aQ',62.3,4);
up('#s11 .q',64.1);stick('#s11 .q .st',64.7);
/* 12 evaluación */
up('#s12 .tt',67.2);stick('#s12 .tt .st',67.6);tl.to('#s12 .tt',{opacity:0,y:-30,duration:0.4},68.5);
tl.fromTo('#s12 .ev',{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.6,ease:'elastic.out(1,0.6)'},68.7);
pop('#clip',68.9);draw('#s12 .er',69.5,0.5);pop('#s12 .ec0',69.7);pop('#s12 .ec1',70.1);pop('#s12 .ec2',70.5);up('#s12 .cap2',70.4);
/* 13 cierre */
up('#s13 .t',71.3);stick('#s13 .t .st',71.9);tl.to('#s13 .t',{opacity:0.0,y:-20,duration:0.3},74.1);
up('#s13 .q2',74.3);pop('#s13 .o1',75.3);tl.fromTo('#s13 .ot1',{opacity:0},{opacity:1,duration:0.3,stagger:0.2},75.5);
pop('#s13 .o2',77.0);tl.fromTo('#s13 .ot2',{opacity:0},{opacity:1,duration:0.3,stagger:0.2},77.2);
enter('#s13 .cz',78.2);fade('#s13 .cz',78.2);breathe('#s13 .cz',79.0,1);up('#s13 .web',78.9,{y:20});
/* transición: línea con nodo hecha a mano */
__BOUND__.forEach(function(b0){var b=W(b0);tl0.set('#trl,#trn',{opacity:1},b-0.4);
 tl0.fromTo('#trl',{attr:{x2:-40}},{attr:{x2:1120},duration:0.36,ease:'power2.inOut'},b-0.4);
 tl0.fromTo('#trn',{attr:{cx:-40}},{attr:{cx:1120},duration:0.36,ease:'power2.inOut'},b-0.4);
 tl0.to('#trl,#trn',{opacity:0,duration:0.15},b-0.03);});
/* cámara lenta */
tl0.fromTo('#cam',{scale:1,transformOrigin:'50% 46%'},{scale:1.04,duration:__DUR__,ease:'none'},0);
/* subtítulos */
for(var c=0;c<__NCAP__;c++){tl0.fromTo('#cap'+c+' .plate',{opacity:0,y:14},{opacity:1,y:0,duration:0.18},__CAPS__[c][0]);}
window.__timelines=window.__timelines||{};window.__timelines['kt18full']=tl0;
