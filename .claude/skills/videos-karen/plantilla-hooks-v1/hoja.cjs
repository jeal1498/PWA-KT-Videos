const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file://'+process.cwd()+'/index.html');await p.waitForTimeout(800);
const DUR=await p.evaluate(()=>window.DUR);let n=0;for(let t=0.5;t<DUR;t+=1){await p.evaluate(t=>seek(t),t);await p.screenshot({path:`g_${String(++n).padStart(3,'0')}.png`,clip:{x:0,y:240,width:1080,height:1300}});}
await b.close()})();
