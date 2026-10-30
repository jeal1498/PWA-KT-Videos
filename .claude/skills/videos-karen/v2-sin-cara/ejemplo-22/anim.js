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
[['#s1',0,4.85],['#s2',4.9,12.0],['#s3',12.1,22.5],['#s4',22.6,33.0],['#s5',33.1,39.2],['#s6',39.3,48.4],['#s7',48.5,57.3],['#s8',57.4,65.0],['#s9',65.1,99]].forEach(function(s){
 tl.fromTo(s[0],{opacity:0},{opacity:1,duration:0.2},s[1]); if(s[2]<74) tl0.to(s[0],{opacity:0,duration:0.22},W(s[2])-0.22);});
function drop(sel,t){tl.fromTo(sel,{y:-300,opacity:0},{y:0,opacity:1,duration:0.7,ease:'bounce.out'},t);}
function spin(sel,t,deg,dur,o){tl.fromTo(sel,Object.assign({rotation:0},o||{}),Object.assign({rotation:deg,duration:dur,ease:'none'},o||{}),t);}
/* 1 gancho */
up('#s1 .ced',0.05,{duration:0.4});up('#s1 .w',0.05,{stagger:0.12,y:50});stick('#s1 .st',1.0);
enter('#s1 .a1',0.3);fade('#s1 .a1',0.3);breathe('#s1 .a1',1.1,3);
drop('#s1 .dk1',2.2);drop('#s1 .dk2',3.0);drop('#s1 .dk3',3.9);
/* 2 los sueltas */
up('#s2 .t',5.0);stick('#s2 .st',6.0);pop('#s2 .su',5.1);
drop('#s2 .o1',6.2);drop('#s2 .o2',7.0);drop('#s2 .o3',7.8);
enter('#s2 .aD',9.4);fade('#s2 .aD',9.4);breathe('#s2 .aD',10.1,2);
[9.6,10.2,10.8].forEach(function(t,i){pop('#s2 .qm'+i,t);fade('#s2 .qt'+i,t+0.1);});
tl.to('#s2 .o1,#s2 .o2,#s2 .o3',{opacity:0.45,duration:0.4},9.6);
/* 3 memoria / lugar distinto */
up('#s3 .t',12.2);stick('#s3 .st',13.2);pop('#s3 .mc',12.3);fade('#s3 .mt',12.6);pop('#s3 .ck',13.6);
pop('#s3 .kk',14.0);
pop('#s3 .sp0',14.9);fade('#s3 .sl0',15.2);
pop('#s3 .sp1',15.4);fade('#s3 .sl1',15.7);
pop('#s3 .sp2',15.9);fade('#s3 .sl2',16.2);
up('#s3 .q',17.4);stick('#s3 .q .st',18.5);
pop('#s3 .dq',19.2);fade('#s3 .dqt',19.4);tl.to('#s3 .dq,#s3 .dqt',{x:4,duration:0.06,repeat:19,yoyo:true},20.2);
/* 4 zona de aterrizaje */
up('#s4 .t',22.7);stick('#s4 .st',23.4);pop('#s4 .zp',23.6);
fade('#s4 .zs',24.6);pop('#s4 .zk',26.7);tl.to('#s4 .zs',{opacity:0,duration:0.5},32.2);fade('#s4 .zl1',27.0);pop('#s4 .zt',28.4);fade('#s4 .zl2',28.8);pop('#s4 .zb',31.0);fade('#s4 .zl3',31.4);
/* 5 a la vista / a la mano */
up('#s5 .t',33.2);stick('#s5 .st',34.3);pop('#s5 .ey',33.5);fade('#s5 .e1',33.8);pop('#s5 .ma',34.1);fade('#s5 .e2',34.4);
pop('#s5 .p3',35.4);fade('#s5 .n3',35.7);draw('#x3',36.6,0.4);pop('#s5 .p1',37.9);fade('#s5 .n1',38.2);
/* 6 gesto */
up('#s6 .t',39.4);stick('#s6 .st',40.1);enter('#s6 .aQ',39.5);fade('#s6 .aQ',39.5);breathe('#s6 .aQ',40.3,4);
pop('#s6 .dr',40.4);
pop('#s6 .cd0',43.0);pop('#s6 .cd1',43.3);pop('#s6 .cd2',43.6);
pop('#s6 .ik0',44.0);pop('#s6 .ik1',44.4);pop('#s6 .ik2',44.8);
pop('#s6 .nb0',45.6);fade('#s6 .nt0',45.7);pop('#s6 .nb1',46.1);fade('#s6 .nt1',46.2);pop('#s6 .nb2',46.6);fade('#s6 .nt2',46.7);
up('#s6 .q',47.2);stick('#s6 .q .st',47.5);
tl.to('#s6 .aQ',{x:8,duration:0.1,repeat:7,yoyo:true},47.2);
/* 7 semana / revisar */
up('#s7 .t',48.6);stick('#s7 .st',49.7);
[0,1,2,3,4,5,6].forEach(function(i){pop('#s7 .dy'+i,48.8+i*0.1);fade('#s7 .dl'+i,49.0+i*0.1);});
[0,1,2,3,4,5,6].forEach(function(i){draw('#s7 .dc'+i,49.6+i*0.28,0.25);});
pop('#s7 .eye',52.0);pop('#s7 .mz',53.2);pop('#s7 .mf',54.8);fade('#s7 .mft',55.0);tl.to('#s7 .mf,#s7 .mft',{scale:1.15,transformOrigin:'365px 1130px',duration:0.25,repeat:3,yoyo:true},55.2);
pop('#s7 .sw',55.9);fade('#s7 .s2',56.2);spin('#s7 .swh',56.0,720,1.2,{transformOrigin:'900px 1200px'});
/* 8 cualquier persona */
up('#s8 .t',57.5);stick('#s8 .st',59.1);pop('#s8 .v1',57.7);pop('#s8 .v2',57.95);
tl.fromTo('#s8 .vt',{opacity:0},{opacity:1,duration:0.3,stagger:0.5},60.2);
tl.to('#s8 .v1',{x:25,duration:0.8,ease:'sine.inOut'},59.0);tl.to('#s8 .v2',{x:-25,duration:0.8,ease:'sine.inOut'},59.0);
pop('#s8 .cs',62.5);fade('#s8 .cst',62.8);
/* 9 cierre */
up('#s9 .t',65.2);stick('#s9 .t .st',65.8);
pop('#s9 .sg',66.0);tl.fromTo('#s9 .sgt',{opacity:0},{opacity:1,duration:0.3,stagger:0.4},66.5);
tl.to('#s9 .sg,#s9 .sgt',{opacity:0,duration:0.25},69.2);tl.to('#s9 .t',{opacity:0,y:-20,duration:0.3},68.5);
up('#s9 .q2',68.8);
pop('#s9 .oc0',69.4);pop('#s9 .oi0',69.6);fade('#s9 .ol0',69.8);
pop('#s9 .oc1',70.0);pop('#s9 .oi1',70.2);fade('#s9 .ol1',70.4);
pop('#s9 .oc2',70.6);pop('#s9 .oi2',70.8);fade('#s9 .ol2',71.0);
enter('#s9 .cz',71.2);fade('#s9 .cz',71.2);up('#s9 .web',71.5,{y:20});
/* transición: línea con nodo hecha a mano */
__BOUND__.forEach(function(b0){var b=W(b0);tl0.set('#trl,#trn',{opacity:1},b-0.4);
 tl0.fromTo('#trl',{attr:{x2:-40}},{attr:{x2:1120},duration:0.36,ease:'power2.inOut'},b-0.4);
 tl0.fromTo('#trn',{attr:{cx:-40}},{attr:{cx:1120},duration:0.36,ease:'power2.inOut'},b-0.4);
 tl0.to('#trl,#trn',{opacity:0,duration:0.15},b-0.03);});
/* cámara lenta */
tl0.fromTo('#cam',{scale:1,transformOrigin:'50% 46%'},{scale:1.04,duration:__DUR__,ease:'none'},0);
/* subtítulos */
for(var c=0;c<__NCAP__;c++){tl0.fromTo('#cap'+c+' .plate',{opacity:0,y:14},{opacity:1,y:0,duration:0.18},__CAPS__[c][0]);}
window.__timelines=window.__timelines||{};window.__timelines['kt22full']=tl0;
