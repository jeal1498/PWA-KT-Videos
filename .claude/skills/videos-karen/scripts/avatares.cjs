// Genera las caras del personaje (Open Peeps de DiceBear, CC0) ya en colores de marca, con ids sin choques.
// Uso: NODE_PATH=<dir>/node_modules node avatares.cjs <salida/avs.json> clave:cara [clave:cara ...]
//   ej. node avatares.cjs avs.json duda:suspicious preocupada:concerned tranquila:calm sonrisa:smile
// Una vez por entorno: npm i --prefix <dir> @dicebear/core@9.2.2 @dicebear/collection@9.2.2
const {createAvatar}=require('@dicebear/core');const C=require('@dicebear/collection');const fs=require('fs');
const [out,...pares]=process.argv.slice(2);let n=0;const res={};
for(const par of pares){const [k,face]=par.split(':');const p='v'+(++n)+'-';
 let s=createAvatar(C.openPeeps,{seed:'Mar',size:600,backgroundColor:['transparent'],face:[face],head:['long'],accessoriesProbability:0,facialHairProbability:0,maskProbability:0,skinColor:['F5E7D6'],clothingColor:['C6BCE2'],headContrastColor:['433860']}).toString();
 // ids con prefijo: todos los avatares traen id="viewboxMask" y en la misma página una máscara recortaría a otra
 s=s.replace(/<metadata[\s\S]*?<\/metadata>/,'').replace(/id="([^"]+)"/g,(m,v)=>'id="'+p+v+'"').replace(/url\(#([^)]+)\)/g,(m,v)=>'url(#'+p+v+')');
 // negro → ciruela profundo, blanco → arena; dentro de <mask> el blanco es «visible», no se toca
 res[k]=s.split(/(<mask[\s\S]*?<\/mask>)/g).map(x=>x.startsWith('<mask')?x:x.replace(/#000000|#000\b/g,'#2E2545').replace(/#ffffff|#fff\b/g,'#F5E7D6')).join('');}
fs.writeFileSync(out,JSON.stringify(res));console.log(Object.keys(res).join(' '));
