// Avatar de Karen en el estilo del personaje (opcional, NO se usa por ahora: Eduardo pidió quedarse con el personaje genérico el 27 oct 2026).
// Cabello medium3 con puntas caramelo, lentes rosas, labios rojos (boca dibujada encima: «cerrada» o «dientes») y blusa floreada.
// Genera karen3.html de muestra; las referencias eran dos fotos suyas que no están en el repo.
const {createAvatar}=require('@dicebear/core');const C=require('@dicebear/collection');const fs=require('fs');
let n=0;
function mk(skin,face,head,mouth){head=head||'medium3';mouth=mouth||'cerrada';const p='z'+(++n)+'-';let s=createAvatar(C.openPeeps,{seed:'Karen',size:600,backgroundColor:['transparent'],face:[face],head:[head],accessories:['glasses2'],accessoriesProbability:100,facialHairProbability:0,maskProbability:0,skinColor:[skin],clothingColor:['FFFFFF'],headContrastColor:['724133']}).toString();
 s=s.replace(/<metadata[\s\S]*?<\/metadata>/,'').replace(/id="([^"]+)"/g,(m,v)=>'id="'+p+v+'"').replace(/url\(#([^)]+)\)/g,(m,v)=>'url(#'+p+v+')');
 // pelo con puntas claras: el negro del grupo de la cabeza pasa a degradado
 s=s.replace(/(<\/g><g transform="[^"]+">[\s\S]*?)fill="#000"/,'$1fill="url(#'+p+'om)"');
 // lentes rosas
 s=s.replace(/(<g transform="translate\(203 303\)">[\s\S]*?)fill="#000"/,'$1fill="#D9849C"');
 s=s.replace(/#000000|#000\b/g,'#2E2545');
 s=s.replace('<mask','<defs><linearGradient id="'+p+'om" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2E2545"/><stop offset=".55" stop-color="#3a2a33"/><stop offset=".85" stop-color="#8a5a3c"/><stop offset="1" stop-color="#b07d52"/></linearGradient></defs><mask');
 s=s.replace(/<g transform="translate\(315 248\)">/,'<g class="face" data-mouth="'+mouth+'" data-skin="#'+skin+'" transform="translate(315 248)">');
 return s;}
const fl=(x,y,r)=>`<g transform="translate(${x} ${y})"><ellipse cx="${-r*1.3}" cy="${r*0.5}" rx="${r*0.7}" ry="${r*0.32}" transform="rotate(-25)" fill="#9C7458" stroke="#2E2545" stroke-width="2.5"/><ellipse cx="${r*1.25}" cy="${-r*0.6}" rx="${r*0.65}" ry="${r*0.3}" transform="rotate(30)" fill="#9C7458" stroke="#2E2545" stroke-width="2.5"/>${[0,72,144,216,288].map(a=>`<circle cx="${(r*0.62*Math.cos(a*Math.PI/180)).toFixed(1)}" cy="${(r*0.62*Math.sin(a*Math.PI/180)).toFixed(1)}" r="${(r*0.55).toFixed(1)}" fill="#F2A7B8" stroke="#2E2545" stroke-width="3"/>`).join('')}<circle r="${(r*0.42).toFixed(1)}" fill="#E07A93" stroke="#2E2545" stroke-width="3"/><circle r="${(r*0.14).toFixed(1)}" fill="#E8C35A"/></g>`;
const flores=`<svg viewBox="0 0 600 600" style="position:absolute;inset:0;width:100%;height:100%;clip-path:inset(86% 0 0 0)">${fl(150,575,22)+fl(232,550,15)+fl(392,560,20)+fl(465,588,18)+fl(305,596,14)+fl(82,598,15)+fl(522,556,12)}</svg>`;
const flores2=`<svg viewBox="0 0 600 600" style="position:absolute;inset:0;width:100%;height:100%;clip-path:inset(88% 0 0 0)">${fl(330,590,17)+fl(400,565,14)+fl(455,592,15)+fl(270,600,12)}</svg>`;
const lab=['Foto','Sonrisa cerrada','Sonrisa con dientes'];
const cards=[`<img src="karen-foto2.jpg" style="height:560px;width:560px;object-fit:cover;border-radius:18px">`,`<div class="av">${mk('EDB98A','smile','medium3','cerrada')}${flores}</div>`,`<div class="av">${mk('EDB98A','smile','medium3','dientes')}${flores}</div>`];
const js=`<script>
// la boca original es un trazo oscuro dentro del mismo path que ojos y nariz: se ubica, se tapa con piel y se dibujan labios rojos encima
document.querySelectorAll('.face').forEach(g=>{const f=g.querySelector('path');const b=f.getBBox();const ns='http://www.w3.org/2000/svg';
 let x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;const p=new DOMPoint();
 for(let y=b.y+b.height*0.72;y<=b.y+b.height;y+=1.5)for(let x=b.x;x<=b.x+b.width;x+=1.5){p.x=x;p.y=y;if(f.isPointInFill(p)){x0=Math.min(x0,x);y0=Math.min(y0,y);x1=Math.max(x1,x);y1=Math.max(y1,y);}}
 const mk=(d,a)=>{const e=document.createElementNS(ns,'path');e.setAttribute('d',d);for(const k in a)e.setAttribute(k,a[k]);g.appendChild(e);};
 const w=x1-x0,h=y1-y0;
 mk('M'+(x0-6)+' '+(y0-6)+'h'+(w+12)+'v'+(h+12)+'h'+(-(w+12))+'z',{fill:g.dataset.skin});
 const L=x0,R=x1,T=y0+h*0.15,M=x0+w*0.5;
 if(g.dataset.mouth==='dientes'){
  // boca abierta como en la foto: labio rojo, abertura oscura y dientes arriba
  const cx=x0+w*0.5,top=y0-h*0.15,wd=w*1.15,bt=y1+h*1.5;const l=cx-wd/2,r=cx+wd/2;
  mk('M'+l+' '+top+' Q'+cx+' '+(top+h*0.35)+' '+r+' '+top+' Q'+cx+' '+(bt+h*0.5)+' '+l+' '+top+'z',{fill:'#C9283E',stroke:'#2E2545','stroke-width':5,'stroke-linejoin':'round'});
  mk('M'+(l+wd*0.1)+' '+(top+h*0.32)+' Q'+cx+' '+(top+h*0.6)+' '+(r-wd*0.1)+' '+(top+h*0.32)+' Q'+cx+' '+(bt-h*0.15)+' '+(l+wd*0.1)+' '+(top+h*0.32)+'z',{fill:'#2E2545'});
  mk('M'+(l+wd*0.12)+' '+(top+h*0.34)+' Q'+cx+' '+(top+h*0.62)+' '+(r-wd*0.12)+' '+(top+h*0.34)+' Q'+cx+' '+(top+h*1.3)+' '+(l+wd*0.12)+' '+(top+h*0.34)+'z',{fill:'#FFFFFF'});
 } else {
 mk('M'+L+' '+T+' Q'+M+' '+(y1+h*0.35)+' '+R+' '+(y0)+' Q'+M+' '+(y1+h*1.6)+' '+L+' '+T+'z',{fill:'#C9283E',stroke:'#2E2545','stroke-width':5,'stroke-linejoin':'round'});
 mk('M'+L+' '+T+' Q'+M+' '+(y1+h*0.35)+' '+R+' '+(y0),{fill:'none',stroke:'#2E2545','stroke-width':8,'stroke-linecap':'round'});
 }
});</script>`;
fs.writeFileSync('karen3.html','<!doctype html><meta charset="utf-8"><style>@font-face{font-family:Outfit;src:url(../pers/Outfit-700-latin.woff2)}body{margin:0;background:#2E2545;padding:30px;width:1980px;font-family:Outfit;display:flex;gap:24px}.c{background:radial-gradient(circle at 50% 40%,#4a3f6b,#3a3058);border-radius:26px;padding:20px;text-align:center;width:620px;height:660px;display:flex;flex-direction:column;align-items:center;justify-content:space-between}.av{position:relative;width:560px;height:560px}.av>svg{width:100%;height:100%}b{color:#F5E7D6;font:700 32px Outfit}</style>'+cards.map((c,i)=>`<div class="c">${c}<b>${lab[i]}</b></div>`).join('')+js);
