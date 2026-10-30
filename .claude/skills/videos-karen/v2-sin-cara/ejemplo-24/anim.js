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
var SCN=[['#s1',0,6.5],['#s2',6.5,10.35],['#s3',10.35,18.2],['#s4',18.2,29.5],['#s5',29.5,40.4],['#s6',40.4,46.4],['#s7',46.4,55.3],['#s8',55.3,99]];
SCN.forEach(function(s){tl.fromTo(s[0],{opacity:0},{opacity:1,duration:0.2},s[1]); if(s[2]<90) tl0.to(s[0],{opacity:0,duration:0.22},s[2]-0.22);});
function drop(sel,t){tl.fromTo(sel,{y:-300,opacity:0},{y:0,opacity:1,duration:0.7,ease:'bounce.out'},t);}
function spin(sel,t,deg,dur,o){tl.fromTo(sel,Object.assign({rotation:0},o||{}),Object.assign({rotation:deg,duration:dur,ease:'none'},o||{}),t);}
function dim(sel){tl0.set(sel,{opacity:0.3},0);}
function lite(sel,t){tl.to(sel,{opacity:1,duration:0.25},t);tl.fromTo(sel,{scale:1,transformOrigin:'50% 50%'},{scale:1.07,duration:0.2,yoyo:true,repeat:1,immediateRender:false},t);}
function gspin(sel,cx,cy,t,dur,dir){tl.fromTo(sel,{rotation:0,svgOrigin:cx+' '+cy},{rotation:360*dir,svgOrigin:cx+' '+cy,duration:dur,ease:'none',immediateRender:false},t);}
function shake(sel,t,n,a){tl.to(sel,{x:a||6,duration:0.07,repeat:n,yoyo:true,ease:'sine.inOut'},t);}
/* 1 gancho: cita a las diez */
up('#s1 .ced',0.05,{duration:0.4});up('#s1 .w',0.05,{stagger:0.15,y:50});stick('#s1 .st',0.7);
enter('#s1 .a1',0.3);fade('#s1 .d1',0.3);breathe('#s1 .d1',1.0,2);pop('#s1 .ck1',0.4);
drop('#s1 .p1',2.5);fade('#s1 .pt1',2.9);drop('#s1 .p2',3.2);fade('#s1 .pt2',3.6);drop('#s1 .p3',3.8);fade('#s1 .pt3',4.2);
tl.to('#s1 .mm1',{rotation:150,svgOrigin:'770 1090',duration:1.2,ease:'power2.in'},4.6);tl.to('#s1 .hh1',{rotation:12,svgOrigin:'770 1090',duration:1.2,ease:'power2.in'},4.6);
swap('#s1 .d1','#s1 .d2',5.0);shake('#s1 .d2',5.3,7,6);
/* 2 lo que ves / olvidas */
up('#s2 .t',6.55);stick('#s2 .st',7.2);
pop('#s2 .v1c',6.6);fade('#s2 .vl1',6.8);[0,1,2].forEach(function(i){pop('#s2 .m1'+i,7.0+i*0.25);fade('#s2 .vt1'+i,7.2+i*0.25);});
pop('#s2 .v2c',8.2);fade('#s2 .vl2',8.4);[0,1,2].forEach(function(i){pop('#s2 .m2'+i,8.6+i*0.25);fade('#s2 .vt2'+i,8.8+i*0.25);});
/* 3 tareas invisibles */
up('#s3 .t',10.4);stick('#s3 .st',11.0);
dim('#s3 .c0,#s3 .c1,#s3 .c2,#s3 .c3');
[0,1,2,3].forEach(function(i){pop('#s3 .c'+i,10.5+i*0.15);fade('#s3 .cl'+i,10.7+i*0.15);});
lite('#s3 .c0',12.2);lite('#s3 .c1',13.3);lite('#s3 .c2',14.7);lite('#s3 .c3',17.0);
tl.to('#s3 .c3',{rotation:2,duration:0.12,repeat:5,yoyo:true,transformOrigin:'50% 50%'},17.4);
/* 4 planea al revés */
up('#s4 .t',18.25);stick('#s4 .st',19.0);
pop('#s4 .ck4',18.3);tl.to('#s4 .mm4',{rotation:-1440,svgOrigin:'540 1180',duration:10,ease:'none'},18.6);tl.to('#s4 .hh4',{rotation:-120,svgOrigin:'540 1180',duration:10,ease:'none'},18.6);
draw('#s4 .ar4',18.5,0.9);
pop('#s4 .bk0',19.9);fade('#s4 .bl0',20.1);pop('#s4 .bk1',22.8);fade('#s4 .bl1',23.0);pop('#s4 .bk2',24.5);fade('#s4 .bl2',24.7);pop('#s4 .bk3',27.2);fade('#s4 .bl3',27.4);
/* 5 mide tu tiempo */
up('#s5 .t',29.55);stick('#s5 .st',30.2);
[0,1,2,3,4,5,6].forEach(function(i){pop('#s5 .dy'+i,29.7+i*0.1);fade('#s5 .dl'+i,29.9+i*0.1);});
[0,1,2,3,4,5,6].forEach(function(i){draw('#s5 .dc'+i,30.5+i*0.3,0.25);});
pop('#s5 .bc',31.8);fade('#s5 .bt1',32.0);
tl.fromTo('#s5 .br',{scaleX:0,transformOrigin:'60px 50%',opacity:1},{scaleX:1,duration:1.0,ease:'power2.out'},35.3);fade('#s5 .bt2',35.8);
pop('#s5 .ok5',38.7);
/* 6 alarma */
up('#s6 .t',40.45);stick('#s6 .st',41.2);
enter('#s6 .a6',40.5);fade('#s6 .a6',40.5);breathe('#s6 .a6',41.3,3);
pop('#s6 .q1',40.6);fade('#s6 .qt1',40.8);draw('#s6 .qa',41.4,0.4);pop('#s6 .q2',41.9);fade('#s6 .qt2',42.1);
pop('#s6 .ph',43.0);pop('#s6 .bn',44.5);fade('#s6 .bt',44.7);shake('#s6 .ph,#s6 .bn,#s6 .bt',44.7,9,6);
/* 7 sirve a cualquiera */
up('#s7 .t',46.45);stick('#s7 .st',47.2);pop('#s7 .v1',46.6);pop('#s7 .v2',46.9);
tl.fromTo('#s7 .vt',{opacity:0},{opacity:1,duration:0.3,stagger:0.4},48.6);
tl.to('#s7 .v1',{x:25,duration:0.8,ease:'sine.inOut'},48.6);tl.to('#s7 .v2',{x:-25,duration:0.8,ease:'sine.inOut'},48.6);
pop('#s7 .c1',50.4);fade('#s7 .ct1',50.7);draw('#s7 .ar7',52.0,0.4);pop('#s7 .c2',53.3);fade('#s7 .ct2',53.6);pop('#s7 .k7',54.1);
/* 8 cierre */
up('#s8 .t1',55.35);stick('#s8 .t1 .st',56.0);enter('#s8 .cz',55.4);fade('#s8 .cz',55.4);breathe('#s8 .cz',56.2,4);
pop('#s8 .eb',56.2);fade('#s8 .ebt',56.5);up('#s8 .web',56.5,{y:20});
tl.to('#s8 .t1,#s8 .eb,#s8 .ebt',{opacity:0,duration:0.25},58.3);up('#s8 .t2',58.4);stick('#s8 .t2 .st',59.0);
/* transición */
__BOUND__.forEach(function(b){tl0.set('#trl,#trn',{opacity:1},b-0.4);
 tl0.fromTo('#trl',{attr:{x2:-40}},{attr:{x2:1120},duration:0.36,ease:'power2.inOut'},b-0.4);
 tl0.fromTo('#trn',{attr:{cx:-40}},{attr:{cx:1120},duration:0.36,ease:'power2.inOut'},b-0.4);
 tl0.to('#trl,#trn',{opacity:0,duration:0.15},b-0.03);});
tl0.fromTo('#cam',{scale:1,transformOrigin:'50% 46%'},{scale:1.04,duration:__DUR__,ease:'none'},0);
for(var c=0;c<__NCAP__;c++){tl0.fromTo('#cap'+c+' .plate',{opacity:0,y:14},{opacity:1,y:0,duration:0.18},__CAPS__[c][0]);}
window.__timelines=window.__timelines||{};window.__timelines['kt24full']=tl0;