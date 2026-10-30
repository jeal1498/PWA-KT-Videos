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
[['#s1',0,4.65],['#s2',4.7,12.45],['#s3',12.6,17.45],['#s4',17.6,24.95],['#s5',25.1,32.25],['#s6',32.3,34.25],['#s7',34.3,41.45],['#s8',41.6,47.55],['#s9',47.6,52.25],['#s10',52.3,57.05],['#s11',57.1,60.15],['#s12',60.3,67.65],['#s13',67.9,75.6]].forEach(function(s){
 tl.fromTo(s[0],{opacity:0},{opacity:1,duration:0.2},s[1]); if(s[2]<75.5) tl0.to(s[0],{opacity:0,duration:0.22},W(s[2])-0.22);});

/* 1 gancho */
up('#s1 .ced',0.1,{duration:0.4});
up('#s1 .w',0.3,{stagger:0.16,y:50});
stick('#s1 .st',0.65);
enter('#s1 .a1',0.5);fade('#s1 .a1',0.5);breathe('#s1 .a1',1.3,3);
pop('#s1 .qb',2.4);fade('#s1 .qbt',2.55);draw('#s1 .qb2',2.6,0.3);
tl.to('#s1 .qb,#s1 .qbt',{rotation:12,transformOrigin:'800px 900px',duration:0.3,repeat:5,yoyo:true,ease:'sine.inOut'},3.0);
tl.to('#s1 .a1',{rotation:-4,transformOrigin:'50% 100%',duration:0.4,yoyo:true,repeat:1,ease:'sine.inOut'},2.8);

/* 2 intentas calmarte (prototipo aprobado, +4.7 s) */
var o=4.7;
enter('#s2 .aT,#s2 .aC',o+0.05);fade('#s2 .aT',o+0.05);breathe('#s2 .aT,#s2 .aC',o+0.85,7);
tl.to('#r1',{opacity:0.45,duration:0.5},o+0.4);tl.to('#r2',{opacity:0.25,duration:0.5},o+0.6);
tl.fromTo('#r1',{rotation:0,transformOrigin:'540px 960px'},{rotation:36,duration:7.7,ease:'none'},o);
tl.fromTo('#r2',{rotation:0,transformOrigin:'540px 960px'},{rotation:-26,duration:7.7,ease:'none'},o);
pop('#cloud path',o+1.0);fade('#s2 .clT',o+1.35);pop('#s2 .cb',o+1.25,0.12);
tl.to('#cloud,#s2 .clT',{y:-12,duration:0.7,repeat:1,yoyo:true,ease:'sine.inOut'},o+1.6);
tl.to('#cloud',{scale:0,rotation:10,transformOrigin:'540px 470px',duration:0.4,ease:'back.in(2)'},o+2.9);
tl.to('#s2 .clT',{opacity:0,duration:0.25},o+2.9);
var BU=[[-210,-90],[-120,-170],[30,-200],[160,-150],[230,-40],[-60,80]];
gsap.utils.toArray('#s2 .bu').forEach(function(e,i){tl.fromTo(e,{x:0,y:0,scale:0,opacity:1},{x:BU[i][0],y:BU[i][1],scale:1,duration:0.5,ease:'power3.out'},o+3.22);tl.to(e,{opacity:0,duration:0.3},o+3.6);});
swap('#s2 .aT','#s2 .aC',o+3.4);
tl.to('#s2 .aT,#s2 .aC',{rotation:-3,transformOrigin:'50% 100%',duration:0.25,yoyo:true,repeat:1},o+3.4);
draw('#fkR',o+3.35,0.6);draw('#fkL',o+3.5,0.6);
pop('#nR',o+3.9);pop('#nL',o+4.05);draw('#icR1',o+4.3,0.35);pop('#icR2',o+4.6);draw('#icL',o+4.45,0.5);
pop('#lR',o+4.55);pop('#lL',o+4.7);fade('#s2 .tR',o+4.65);fade('#s2 .tL',o+4.8);
up('#s2 .q',o+3.45);stick('#s2 .q .st',o+3.75);

/* 3 ansiedad */
up('#s3 .chip',12.7);up('#s3 .t',13.0);stick('#s3 .st',13.5);
draw('#road',14.0,1.2);draw('#arr',15.0,0.35);pop('#hoy',13.9);fade('#s3 .th',14.1);
tl.to('#hoy',{x:600,y:-20,duration:1.8,ease:'power1.inOut'},14.7);tl.to('#s3 .th',{opacity:0,duration:0.3},14.7);
pop('#wc',15.0);fade('#s3 .tw',15.3);tl.to('#wc,#s3 .tw',{x:4,duration:0.06,repeat:15,yoyo:true},15.9);

/* 4 TDAH */
up('#s4 .chip',17.7);up('#s4 .t',18.0);stick('#s4 .st',18.5);up('#s4 .cap2',19.2);
pop('#s4 .k1',20.3);fade('#s4 .l1',20.6);pop('#s4 .k2',22.6);fade('#s4 .l2',22.9);pop('#s4 .k3',23.8);fade('#s4 .l3',24.1);

/* 5 perfeccionismo */
up('#s5 .chip',25.2);up('#s5 .t',25.5);stick('#s5 .t .st',26.0);pop('#board',26.6);
[28.7,29.4,30.3].forEach(function(t,i){pop('#s5 .rw'+i+' circle',t);tl.fromTo('#s5 .rt'+i,{opacity:0,x:-30},{opacity:1,x:0,duration:0.4,ease:'back.out(2)'},t);draw('#s5 .ck'+i,t+0.3,0.35);});
up('#s5 .q',30.9);stick('#s5 .q .st',31.0);

/* 6 tres pistas */
up('#s6 .t',32.4);stick('#s6 .st',32.6);draw('#p3l',32.5,0.8);pop('#s6 .pn',32.9,0.25);tl.fromTo('#s6 .pnt',{opacity:0},{opacity:1,duration:0.2,stagger:0.25},33.1);

/* 7 pista 1 */
up('#s7 .pill',34.4);pop('#inf',35.3);fade('#s7 .l7',35.5);draw('#tlp',36.7,3.3);pop('#s7 .ms',37.5,0.65);pop('#hoy7',40.0);
up('#s7 .q',37.2);stick('#s7 .q .st',37.6);

/* 8 pista 2 */
up('#s8 .pill',41.7);pop('#s8 .c1',43.2);fade('#s8 .x1',43.5);pop('#s8 .c2',43.9);fade('#s8 .x2',44.2);pop('#s8 .c3',44.7);fade('#s8 .x3',45.0);
pop('#s8 .ok0',44.0);pop('#s8 .ok1',44.6);pop('#s8 .ok2',45.3);up('#s8 .q',45.6);stick('#s8 .q .st',45.9);

/* 9 pista 3 */
up('#s9 .pill',47.7);pop('#s9 .g0',48.1);draw('#tree',48.3,1.4);pop('#s9 .g1',48.9,0.2);pop('#s9 .g2',49.5,0.18);up('#s9 .q',50.5);stick('#s9 .q .st',50.8);

/* 10 disimular: sonríe y por fuera se ve nerviosa */
up('#s10 .chip',52.4);up('#s10 .t',52.6);stick('#s10 .t .st',53.0);
enter('#s10 .m1,#s10 .m2',52.8);fade('#s10 .m1',52.8);breathe('#s10 .m1,#s10 .m2',53.6,3);
swap('#s10 .m1','#s10 .m2',55.2);tl.to('#s10 .m2',{x:5,duration:0.06,repeat:13,yoyo:true},55.5);
up('#s10 .q',55.1);stick('#s10 .q .st',55.9);

/* 11 conviven */
pop('#s11 .v1',57.2);pop('#s11 .v2',57.45);tl.fromTo('#s11 .vt',{opacity:0},{opacity:1,duration:0.3,stagger:0.15},57.7);
tl.to('#s11 .v1',{x:20,duration:0.8,ease:'sine.inOut'},58.3);tl.to('#s11 .v2',{x:-20,duration:0.8,ease:'sine.inOut'},58.3);
up('#s11 .q',57.8);stick('#s11 .q .st',58.2);

/* 12 evaluación */
up('#s12 .tt',60.4);stick('#s12 .tt .st',60.9);tl.to('#s12 .tt',{opacity:0,y:-30,duration:0.4},63.0);
tl.fromTo('#s12 .ev',{opacity:0,scale:0.5},{opacity:1,scale:1,duration:0.6,ease:'elastic.out(1,0.6)'},63.2);
pop('#clip',63.5);draw('#s12 .er',64.3,0.5);pop('#s12 .ec0',64.8);pop('#s12 .ec1',65.3);pop('#s12 .ec2',65.8);up('#s12 .cap2',65.2);

/* 13 cierre */
up('#s13 .t',68.0);stick('#s13 .t .st',68.5);up('#s13 .q2',71.6);
enter('#s13 .cz',71.8);fade('#s13 .cz',71.8);breathe('#s13 .cz',72.6,3);
pop('#s13 .mn',72.3,0.3);tl.fromTo('#s13 .mnt',{opacity:0},{opacity:1,duration:0.2,stagger:0.3},72.5);
tl.to('#s13 .cz',{y:-18,duration:0.25,yoyo:true,repeat:3,ease:'power2.out'},74.0);up('#s13 .web',74.2,{y:20});

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
