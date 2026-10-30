var tl0=gsap.timeline({paused:true});var tl=tl0;
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
var SCN=[['#s1',0,6.65],['#s2',6.7,11.25],['#s3',11.25,21.9],['#s4',21.9,27.45],['#s5',27.45,32.55],['#s6',32.55,37.15],['#s7',37.15,47.9],['#s8',47.9,54.15],['#s9',54.15,60.45],['#s10',60.45,99]];
SCN.forEach(function(s){tl.fromTo(s[0],{opacity:0},{opacity:1,duration:0.2},s[1]); if(s[2]<90) tl0.to(s[0],{opacity:0,duration:0.22},s[2]-0.22);});
function drop(sel,t){tl.fromTo(sel,{y:-300,opacity:0},{y:0,opacity:1,duration:0.7,ease:'bounce.out'},t);}
function spin(sel,t,deg,dur,o){tl.fromTo(sel,Object.assign({rotation:0},o||{}),Object.assign({rotation:deg,duration:dur,ease:'none'},o||{}),t);}
function dim(sel){tl0.set(sel,{opacity:0.3},0);}
function lite(sel,t){tl.to(sel,{opacity:1,duration:0.25},t);tl.fromTo(sel,{scale:1,transformOrigin:'50% 50%'},{scale:1.07,duration:0.2,yoyo:true,repeat:1,immediateRender:false},t);}
function gspin(sel,cx,cy,t,dur,dir){tl.fromTo(sel,{rotation:0,svgOrigin:cx+' '+cy},{rotation:360*dir,svgOrigin:cx+' '+cy,duration:dur,ease:'none',immediateRender:false},t);}
function shake(sel,t,n,a){tl.to(sel,{x:a||6,duration:0.07,repeat:n,yoyo:true,ease:'sine.inOut'},t);}
/* 1 gancho: reunión en calma, motor por dentro */
up('#s1 .ced',0.05,{duration:0.4});up('#s1 .w',0.05,{stagger:0.15,y:50});stick('#s1 .st',0.8);
pop('#s1 .si',0.25,0.18);enter('#s1 .a1',0.3);fade('#s1 .ac',0.3);breathe('#s1 .ac',1.1,3);up('#s1 .tb',0.5);
pop('#s1 .g1',3.8);tl.to('#s1 .g1',{rotation:'+=1080',svgOrigin:'540 1290',duration:2.4,ease:'none'},4.2);
draw('#s1 .wv path',4.0,0.5);
swap('#s1 .ac','#s1 .ah',4.0);shake('#s1 .ah',4.3,9,7);
/* 2 hiperactividad en adultos */
up('#s2 .chip',6.75);up('#s2 .t',6.8);stick('#s2 .st',7.6);
pop('#s2 .g2m',6.9);tl.to('#s2 .g2',{rotation:720,svgOrigin:'540 1130',duration:4.5,ease:'none'},7.0);
draw('#s2 .wv2 path',7.3,0.5);
tl.to('#s2 .g2m',{x:210,scale:0.8,transformOrigin:'540px 1130px',duration:0.6,ease:'power2.inOut'},9.35);
pop('#s2 .rn',9.5);draw('#s2 .sl',10.2,0.4);
/* 3 cuatro tarjetas */
up('#s3 .t',11.3);stick('#s3 .st',12.2);
dim('#s3 .c0,#s3 .c1,#s3 .c2,#s3 .c3');
[0,1,2,3].forEach(function(i){pop('#s3 .c'+i,11.4+i*0.15);fade('#s3 .cl'+i,11.6+i*0.15);});
lite('#s3 .c0',12.2);lite('#s3 .c1',13.6);lite('#s3 .c2',15.5);lite('#s3 .c3',18.1);
tl.to('#s3 .c3',{rotation:2,duration:0.12,repeat:9,yoyo:true,transformOrigin:'50% 50%'},19.0);
/* 4 años creyendo */
up('#s4 .t',21.95);stick('#s4 .st',22.8);enter('#s4 .u1',22.0);fade('#s4 .u1',22.0);breathe('#s4 .u1',22.8,3);
pop('#s4 .b1',22.5);fade('#s4 .bt1',22.7);
swap('#s4 .u1','#s4 .u2',25.8);tl.to('#s4 .b1,#s4 .bt1',{opacity:0.4,duration:0.3},25.7);pop('#s4 .b2',25.9);fade('#s4 .bt2',26.1);
/* 5 conducta ≠ diagnóstico */
up('#s5 .t',27.5);stick('#s5 .st',28.5);
pop('#s5 .k1',27.6);fade('#s5 .kt1',27.9);shake('#s5 .k1',28.2,12,5);
fade('#s5 .dp',28.0);up('#s5 .cap2',29.1);
pop('#s5 .ne',30.9);pop('#s5 .k2',31.3);fade('#s5 .kt2',31.6);tl.to('#s5 .dp',{opacity:0,duration:0.2},31.3);
/* 6 estrés, sueño, café */
up('#s6 .t',32.6);stick('#s6 .st',33.4);
dim('#s6 .d0,#s6 .d1,#s6 .d2');
[0,1,2].forEach(function(i){pop('#s6 .d'+i,32.7+i*0.15);fade('#s6 .dl'+i,32.9+i*0.15);});
lite('#s6 .d0',33.45);lite('#s6 .d1',34.3);lite('#s6 .d2',35.7);
tl.fromTo('#s6 .zz',{opacity:0,y:20},{opacity:1,y:-10,duration:0.5,stagger:0.3},34.5);
/* 7 un profesional explora */
up('#s7 .t',37.2);stick('#s7 .st',38.0);
dim('#s7 .r0,#s7 .r1,#s7 .r2,#s7 .r3');
[0,1,2,3].forEach(function(i){pop('#s7 .r'+i,37.3+i*0.15);fade('#s7 [data-r="'+i+'"]',37.5+i*0.15);});
pop('#s7 .lp',37.6);
lite('#s7 .r0',38.6);lite('#s7 .r1',41.2);lite('#s7 .r2',42.9);lite('#s7 .r3',45.3);
tl.to('#s7 .lp',{y:0,duration:0.01},38.0);tl.to('#s7 .lp',{y:160,duration:0.5,ease:'power2.inOut'},41.0);tl.to('#s7 .lp',{y:320,duration:0.5,ease:'power2.inOut'},42.7);tl.to('#s7 .lp',{y:480,duration:0.5,ease:'power2.inOut'},45.1);
pop('#s7 .k0',40.7);pop('#s7 .k1',42.4);pop('#s7 .k2',44.9);pop('#s7 .k3',47.0);
/* 8 no te etiquetes */
up('#s8 .t',47.95);stick('#s8 .st',48.7);
enter('#s8 .n1',48.0);fade('#s8 .n1',48.0);breathe('#s8 .n1',48.8,3);
pop('#s8 .tg',48.1);fade('#s8 .tgt',48.3);
tl.to('#s8 .tg,#s8 .tgt',{x:700,y:-260,rotation:40,opacity:0,duration:0.7,ease:'power2.in'},50.0);
pop('#s8 .nb',48.4);fade('#s8 .nt',48.9);
draw('#s8 .nl',50.7,0.5);
swap('#s8 .n1','#s8 .n2',53.0);
/* 9 información útil */
up('#s9 .t',54.2);stick('#s9 .st',55.0);
pop('#s9 .m9',54.3);fade('#s9 .ml',54.8);pop('#s9 .cb',55.0);
draw('#s9 .ar',56.0,0.5);draw('#s9 .cn',56.6,0.4);fade('#s9 .pe',56.0);pop('#s9 .ok',58.3);
/* 10 cierre */
up('#s10 .t1',60.5);stick('#s10 .t1 .st',61.0);enter('#s10 .cz',60.5);fade('#s10 .cz',60.5);breathe('#s10 .cz',61.2,4);up('#s10 .web',61.0,{y:20});
tl.to('#s10 .t1',{opacity:0,y:-20,duration:0.25},61.45);up('#s10 .t2',61.55);stick('#s10 .t2 .st',62.2);
/* transición */
__BOUND__.forEach(function(b){tl0.set('#trl,#trn',{opacity:1},b-0.4);
 tl0.fromTo('#trl',{attr:{x2:-40}},{attr:{x2:1120},duration:0.36,ease:'power2.inOut'},b-0.4);
 tl0.fromTo('#trn',{attr:{cx:-40}},{attr:{cx:1120},duration:0.36,ease:'power2.inOut'},b-0.4);
 tl0.to('#trl,#trn',{opacity:0,duration:0.15},b-0.03);});
tl0.fromTo('#cam',{scale:1,transformOrigin:'50% 46%'},{scale:1.04,duration:__DUR__,ease:'none'},0);
for(var c=0;c<__NCAP__;c++){tl0.fromTo('#cap'+c+' .plate',{opacity:0,y:14},{opacity:1,y:0,duration:0.18},__CAPS__[c][0]);}
window.__timelines=window.__timelines||{};window.__timelines['kt23full']=tl0;