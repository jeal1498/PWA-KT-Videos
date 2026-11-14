const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file://'+process.cwd()+'/index.html');await p.waitForTimeout(800);
const dur=63;for(let t=0.5;t<dur;t+=1){await p.evaluate(t=>seek(t),t);await p.screenshot({path:`g_${String(Math.round(t*10)).padStart(4,'0')}.png`,clip:{x:0,y:800,width:1080,height:900}});}
await b.close()})();
