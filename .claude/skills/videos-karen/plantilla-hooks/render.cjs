const {chromium}=require('playwright');const {spawn}=require('child_process');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/index.html');await p.waitForTimeout(800);
const dur=await p.evaluate(()=>DUR);
const ff=spawn('ffmpeg',['-v','error','-y','-f','image2pipe','-framerate','30','-i','-','-i','voz.mp3','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','fast','-c:a','aac','-b:a','160k','-shortest','previa.mp4'],{stdio:['pipe','inherit','inherit']});
const n=Math.round(dur*30);for(let i=0;i<n;i++){await p.evaluate(t=>seek(t),i/30);const buf=await p.screenshot({type:'jpeg',quality:92});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();})();
