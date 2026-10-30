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
/* escenas */
[['#s1',0,6.6],['#s2',6.7,9.6],['#s3',9.7,17.9],['#s4',18.0,24.0],['#s5',24.2,31.9],['#s6',32.0,38.8],['#s7',38.9,48.7],['#s8',48.8,60.1],['#s9',60.2,66.6],['#s10',66.7,74.7]].forEach(function(s){
 tl.fromTo(s[0],{opacity:0},{opacity:1,duration:0.2},s[1]); if(s[2]<74) tl0.to(s[0],{opacity:0,duration:0.22},W(s[2])-0.22);});
/* 1 gancho */
up('#s1 .ced',0.05,{duration:0.4});up('#s1 .w',0.05,{stagger:0.12,y:50});stick('#s1 .st',1.9);
enter('#s1 .a1',0.4);fade('#s1 .a1',0.4);breathe('#s1 .a1',1.2,5);
up('#s1 .q',5.5);stick('#s1 .q .st',5.7);
tl.to('#s1 .a1',{rotation:-4,transformOrigin:'50% 100%',duration:0.5,yoyo:true,repeat:1,ease:'sine.inOut'},5.6);
/* 2 querer / arrancar */
pop('#s2 .c1',6.8);fade('#s2 .l1',7.1);pop('#s2 .c2',7.7);fade('#s2 .l2',8.0);
pop('#s2 .ne',8.6);up('#s2 .q',8.9);stick('#s2 .q .st',9.1);
/* 3 dificultad */
up('#s3 .chip',9.8);up('#s3 .t',10.2);stick('#s3 .st',12.2);
pop('#s3 .k1',10.6);pop('#s3 .k2',10.8);pop('#s3 .k3',11.0);tl.to('#s3 .k1,#s3 .k2,#s3 .k3',{opacity:0.4,duration:0.3},11.4);
tl.to('#s3 .k1',{opacity:1,duration:0.3},12.2);fade('#s3 .l1',12.4);tl.to('#s3 .k2',{opacity:1,duration:0.3},13.8);fade('#s3 .l2',14.0);tl.to('#s3 .k3',{opacity:1,duration:0.3},15.3);fade('#s3 .l3',15.5);
tl.fromTo('#gn',{attr:{width:0}},{attr:{width:840},duration:1.0,ease:'power2.out'},16.4);fade('#s3 .gl',16.5);
/* 4 esfuerzo */
up('#s4 .t',18.1);stick('#s4 .st',20.0);enter('#s4 .aT',18.4);fade('#s4 .aT',18.4);breathe('#s4 .aT',19.3,4);
fade('#s4 .e1',20.6);tl.fromTo('#ef',{attr:{width:0}},{attr:{width:900},duration:1.2,ease:'power2.out'},20.8);
fade('#s4 .e2',22.4);tl.fromTo('#rs',{attr:{width:0}},{attr:{width:420},duration:1.0,ease:'power2.out'},22.6);
tl.to('#s4 .aT',{rotation:3,transformOrigin:'50% 100%',duration:0.6,yoyo:true,repeat:1},22.8);
/* 5 pregunta */
up('#s5 .chip',24.3);pop('#s5 .b1',24.6);fade('#s5 .p1',24.9);draw('#stk',29.0,0.5);
draw('#dn',29.3,0.4);pop('#s5 .b2',29.7);tl.fromTo('#s5 .p2',{opacity:0},{opacity:1,duration:0.3,stagger:0.5},30.0);
/* 6 diminuto */
up('#s6 .t',32.1);stick('#s6 .st',33.4);
pop('#s6 .sml',33.6);pop('#s6 .big',35.3);fade('#s6 .bg',35.6);
tl.fromTo('#s6 .bg',{opacity:1},{opacity:0.55,duration:0.3,immediateRender:false},36.4);
draw('#sta',36.9,0.4);tl.to('#s6 .sml',{scale:1.08,transformOrigin:'810px 1100px',duration:0.3,yoyo:true,repeat:1},37.2);fade('#s6 .sm',37.4);
/* 7 convives */
up('#s7 .chip',39.0);up('#s7 .t',39.4);stick('#s7 .st',41.3);
pop('#s7 .ex',39.9);fade('#s7 .et',40.2);tl.to('#s7 .ex,#s7 .et',{x:6,duration:0.06,repeat:7,yoyo:true},41.4);
tl.to('#s7 .ex,#s7 .et',{opacity:0,duration:0.2},42.5);pop('#s7 .bub',42.6);fade('#s7 .bt',42.9);
pop('#s7 .co',44.8);fade('#s7 .x1',45.2);pop('#s7 .re',46.5);fade('#s7 .x2',46.9);
tl.to('#s7 .re',{rotation:12,transformOrigin:'810px 1130px',duration:0.12,repeat:7,yoyo:true},47.6);
/* 8 ojo */
up('#s8 .chip',48.9);up('#s8 .t',49.2);stick('#s8 .st',50.4);
enter('#s8 .aD',49.6);fade('#s8 .aD',49.6);breathe('#s8 .aD',50.4,4);
pop('#s8 .i3',53.6);fade('#s8 .lb3',53.9);pop('#s8 .i4',54.6);fade('#s8 .lb4',54.9);pop('#s8 .i5',55.5);fade('#s8 .lb5',55.8);
up('#s8 .q',58.0);stick('#s8 .q .st',58.4);
/* 9 balanza */
up('#s9 .t',60.3);stick('#s9 .st',62.2);
pop('#s9 .pl',61.0);fade('#s9 .tl',61.3);
tl.fromTo('#beam',{rotation:0,transformOrigin:'540px 900px'},{rotation:-6,duration:0.8,ease:'sine.inOut'},61.6);
pop('#s9 .pr',64.1);fade('#s9 .tr',64.4);
tl.to('#beam',{rotation:0,duration:0.8,ease:'elastic.out(1,0.5)',transformOrigin:'540px 900px'},64.6);
up('#s9 .q',65.2);stick('#s9 .q .st',65.5);
/* 10 cierre */
up('#s10 .t',66.8);stick('#s10 .t .st',67.3);tl.to('#s10 .t',{opacity:0,y:-20,duration:0.3},69.7);
up('#s10 .q2',70.0);draw('#s10 .sh',71.0,0.6);pop('#s10 .sn',71.3,0.2);
enter('#s10 .cz',73.0);fade('#s10 .cz',73.0);up('#s10 .web',73.6,{y:20});
/* transición: línea con nodo hecha a mano */
__BOUND__.forEach(function(b0){var b=W(b0);tl0.set('#trl,#trn',{opacity:1},b-0.4);
 tl0.fromTo('#trl',{attr:{x2:-40}},{attr:{x2:1120},duration:0.36,ease:'power2.inOut'},b-0.4);
 tl0.fromTo('#trn',{attr:{cx:-40}},{attr:{cx:1120},duration:0.36,ease:'power2.inOut'},b-0.4);
 tl0.to('#trl,#trn',{opacity:0,duration:0.15},b-0.03);});
/* cámara lenta */
tl0.fromTo('#cam',{scale:1,transformOrigin:'50% 46%'},{scale:1.04,duration:__DUR__,ease:'none'},0);
/* subtítulos */
for(var c=0;c<__NCAP__;c++){tl0.fromTo('#cap'+c+' .plate',{opacity:0,y:14},{opacity:1,y:0,duration:0.18},__CAPS__[c][0]);}
window.__timelines=window.__timelines||{};window.__timelines['kt21full']=tl0;
