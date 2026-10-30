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
var B=[0,5.8,9.3,14.6,20.4,25.1,29.8,35.4,45.0,52.4,59.3,63.5,99];
for(var n=0;n<12;n++){(function(n){var id='#s'+(n+1);tl.fromTo(id,{opacity:0},{opacity:1,duration:0.2},B[n]); if(B[n+1]<90) tl0.to(id,{opacity:0,duration:0.22},B[n+1]-0.22);})(n);}
function drop(sel,t){tl.fromTo(sel,{y:-300,opacity:0},{y:0,opacity:1,duration:0.7,ease:'bounce.out'},t);}
function spin(sel,t,deg,dur,o){tl.fromTo(sel,Object.assign({rotation:0},o||{}),Object.assign({rotation:deg,duration:dur,ease:'none'},o||{}),t);}
function dim(sel){tl0.set(sel,{opacity:0.3},0);}
function lite(sel,t){tl.to(sel,{opacity:1,duration:0.25},t);tl.fromTo(sel,{scale:1,transformOrigin:'50% 50%'},{scale:1.07,duration:0.2,yoyo:true,repeat:1,immediateRender:false},t);}
function gspin(sel,cx,cy,t,dur,dir){tl.fromTo(sel,{rotation:0,svgOrigin:cx+' '+cy},{rotation:360*dir,svgOrigin:cx+' '+cy,duration:dur,ease:'none',immediateRender:false},t);}
function shake(sel,t,n,a){tl.to(sel,{x:a||6,duration:0.07,repeat:n,yoyo:true,ease:'sine.inOut'},t);}

function ttl(id,a){up(id+' .t',a+0.05);stick(id+' .st',a+0.7);}
/* 1 cocina */
up('#s1 .ced',0.05,{duration:0.4});up('#s1 .w',0.05,{stagger:0.15,y:50});stick('#s1 .st',0.7);
pop('#s1 .fr',0.35);pop('#s1 .sv',0.6);enter('#s1 .a1',0.3);fade('#s1 .d1',0.3);breathe('#s1 .d1',1.0,2);
pop('#s1 .qm1',1.9);pop('#s1 .qm2',2.5);pop('#s1 .qm3',3.0);
swap('#s1 .d1','#s1 .d2',3.7);tl.to('#s1 .qm1,#s1 .qm2,#s1 .qm3',{y:-14,duration:0.5,repeat:3,yoyo:true,ease:'sine.inOut'},3.7);
up('#s1 .why',4.3);stick('#s1 .why .st',4.5);
/* 2 un olvido, cuatro causas */
ttl('#s2',5.8);pop('#s2 .hub',5.9);fade('#s2 .hubt',6.1);
[0,1,2,3].forEach(function(i){draw('#s2 .br'+i,6.5+i*0.3,0.5);pop('#s2 .nd'+i,7.0+i*0.3);fade('#s2 .ndt'+i,7.2+i*0.3);});
tl.to('#s2 .hub',{scale:1.08,transformOrigin:'50% 50%',duration:0.4,yoyo:true,repeat:3,ease:'sine.inOut'},7.9);
/* 3 mala noche */
ttl('#s3',9.3);pop('#s3 .mo',9.4);gsap.utils.toArray('#s3 .stz').forEach(function(e,i){pop(e,9.6+i*0.2);});fade('#s3 .zz',10.1);
tl.to('#s3 .zz',{y:-18,duration:0.8,repeat:3,yoyo:true,ease:'sine.inOut'},10.3);
pop('#s3 .bfr',10.2,0.15);tl.fromTo('#s3 .bf1,#s3 .bf2',{opacity:0},{opacity:1,duration:0.3},10.6);fade('#s3 .bl1',10.6);fade('#s3 .bl2',10.7);
tl.to('#s3 .bf1',{scaleY:0.22,svgOrigin:'625 1272',duration:1.4,ease:'power2.inOut'},12.3);tl.to('#s3 .bf2',{scaleY:0.18,svgOrigin:'865 1272',duration:1.4,ease:'power2.inOut'},12.9);
/* 4 estrés */
ttl('#s4',14.6);pop('#s4 .hd',14.7);fade('#s4 .hdt',14.9);
[0,1,2,3].forEach(function(i){pop('#s4 .nt'+i,15.3+i*0.6);fade('#s4 .ntt'+i,15.5+i*0.6);});
pop('#s4 .dt',17.9);fade('#s4 .dtt',18.0);
tl.to('#s4 .dt,#s4 .dtt',{x:-230,duration:0.45,ease:'power2.in'},18.4);tl.to('#s4 .dt,#s4 .dtt',{x:0,rotation:14,duration:0.6,ease:'back.out(2)'},18.9);
/* 5 ansiedad */
ttl('#s5',20.4);pop('#s5 .rc',20.5);fade('#s5 .rct',20.7);
[0,1,2,3].forEach(function(i){pop('#s5 .bb'+i,21.2+i*0.4);fade('#s5 .bt'+i,21.4+i*0.4);});
tl.to('#s5 .bb0,#s5 .bt0',{x:60,y:140,duration:0.8,ease:'sine.inOut'},22.8);tl.to('#s5 .bb1,#s5 .bt1',{x:-60,y:130,duration:0.8,ease:'sine.inOut'},22.9);
tl.to('#s5 .bb2,#s5 .bt2',{x:60,y:-130,duration:0.8,ease:'sine.inOut'},23.0);tl.to('#s5 .bb3,#s5 .bt3',{x:-60,y:-130,duration:0.8,ease:'sine.inOut'},23.1);
tl.to('#s5 .rc,#s5 .rct',{scale:0.78,transformOrigin:'50% 50%',duration:0.5},23.7);shake('#s5 .rc,#s5 .rct',23.9,7,5);
/* 6 sobrecarga */
ttl('#s6',25.1);enter('#s6 .a6',25.2);fade('#s6 .a6',25.2);breathe('#s6 .a6',26,3);
[0,1,2,3,4].forEach(function(i){drop('#s6 .tc'+i,25.7+i*0.5);fade('#s6 .tt'+i,26.1+i*0.5);});
tl.to('#s6 .tw',{rotation:7,svgOrigin:'660 1330',duration:0.6,ease:'sine.in'},28.3);
tl.to('#s6 .tc4,#s6 .tt4,#s6 .tc3,#s6 .tt3',{x:160,y:120,rotation:18,duration:0.7,ease:'power2.in'},28.7);
/* 7 qué me pasa */
ttl('#s7',29.8);[0,1,2,3].forEach(function(i){pop('#s7 .pp'+i,29.9+i*0.25);fade('#s7 .ppt'+i,30.1+i*0.25);});
draw('#s7 .ar7',31.0,0.4);pop('#s7 .bgq',31.3);fade('#s7 .bq1',31.5);fade('#s7 .bq2',31.6);
enter('#s7 .a7',31.2);fade('#s7 .a7',31.2);breathe('#s7 .a7',32,3);up('#s7 .ao',33.0,{y:20});
/* 8 años, tres lugares */
ttl('#s8',35.4);draw('#s8 .tl8',35.6,1.0);fade('#s8 .tt0',35.9);fade('#s8 .tt2',37.9);
[0,1,2,3].forEach(function(i){pop('#s8 .tn'+i,36.2+i*0.7);});
dim('#s8 .k0,#s8 .k1,#s8 .k2');[0,1,2].forEach(function(i){pop('#s8 .k'+i,38.7+i*0.2);fade('#s8 .kl'+i,38.9+i*0.2);});
lite('#s8 .k0',40.4);lite('#s8 .k1',41.2);lite('#s8 .k2',42.0);
[0,1,2].forEach(function(i){pop('#s8 .kc'+i,[40.6,41.4,42.2][i]);});
pop('#s8 .vd',43.7);fade('#s8 .vdt',43.9);
/* 9 profesional */
ttl('#s9',45.0);pop('#s9 .fo',45.1);fade('#s9 .fot',45.5);
pop('#s9 .lp',46.4);tl.to('#s9 .lp',{x:-60,y:70,rotation:-8,duration:1.2,repeat:3,yoyo:true,ease:'sine.inOut',svgOrigin:'800 930'},47.6);
fade('#s9 .ecl',49.8);[0,1,2].forEach(function(i){pop('#s9 .ec'+i,50.0+i*0.4);fade('#s9 .ect'+i,50.2+i*0.4);});
/* 10 mientras tanto */
ttl('#s10',52.4);dim('#s10 .z0,#s10 .z1,#s10 .z2');[0,1,2].forEach(function(i){pop('#s10 .z'+i,52.6+i*0.2);fade('#s10 .zl'+i,52.8+i*0.2);});
lite('#s10 .z0',54.0);lite('#s10 .z1',55.4);lite('#s10 .z2',56.7);
/* 11 no todo olvido */
up('#s11 .t',59.35);stick('#s11 .st',60.0);enter('#s11 .a11',59.4);fade('#s11 .a11',59.4);breathe('#s11 .a11',60.2,3);
/* 12 cierre */
up('#s12 .t1',63.55);stick('#s12 .t1 .st',64.2);enter('#s12 .cz',63.6);fade('#s12 .cz',63.6);breathe('#s12 .cz',64.4,6);
dim('#s12 .g0,#s12 .g1');pop('#s12 .g0',63.8);fade('#s12 .gt0',64.0);pop('#s12 .g1',64.1);fade('#s12 .gt1',64.3);
lite('#s12 .g0',66.0);lite('#s12 .g1',67.5);
tl.to('#s12 .t1,#s12 .g0,#s12 .g1,#s12 .gt0,#s12 .gt1',{opacity:0,duration:0.25},68.4);up('#s12 .t2',68.6);stick('#s12 .t2 .st',69.2);up('#s12 .web',68.9,{y:20});
/* transición */
__BOUND__.forEach(function(b){tl0.set('#trl,#trn',{opacity:1},b-0.4);
 tl0.fromTo('#trl',{attr:{x2:-40}},{attr:{x2:1120},duration:0.36,ease:'power2.inOut'},b-0.4);
 tl0.fromTo('#trn',{attr:{cx:-40}},{attr:{cx:1120},duration:0.36,ease:'power2.inOut'},b-0.4);
 tl0.to('#trl,#trn',{opacity:0,duration:0.15},b-0.03);});
tl0.fromTo('#cam',{scale:1,transformOrigin:'50% 46%'},{scale:1.04,duration:__DUR__,ease:'none'},0);
for(var c=0;c<__NCAP__;c++){tl0.fromTo('#cap'+c+' .plate',{opacity:0,y:14},{opacity:1,y:0,duration:0.18},__CAPS__[c][0]);}
window.__timelines=window.__timelines||{};window.__timelines['kt25full']=tl0;