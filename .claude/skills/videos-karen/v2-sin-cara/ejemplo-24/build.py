import json, html as H
AV=json.load(open('avs.json')); W=json.load(open('words.json'))
DUR=round(W[-1][2]+0.6,2)
L,R,A,D,G='#C6BCE2','#F9DEE3','#F5E7D6','#2E2545','#10b77f'
# ---- subtítulos ----
ch=[];cur=[]
def fl():
    global cur
    if cur: ch.append([' '.join(x[0] for x in cur),cur[0][1],cur[-1][2]]); cur=[]
for w in W:
    cur.append(w); n=len(' '.join(x[0] for x in cur))
    if w[0][-1] in '.?:' or (w[0][-1]==',' and n>16) or n>30: fl()
fl()
caps=[]
for i,(t,a,b) in enumerate(ch):
    nx=ch[i+1][1]-0.04 if i+1<len(ch) else DUR
    e=min(max(b+0.12,a+0.3),nx); a=max(0.02,a-0.02)
    caps.append((t,round(a,2),round(e-a,2)))
SC=[]  # (id,a,b,html)
def sc(i,a,b,body): SC.append((i,a,b,body))
def av(k,cls,style): return f'<div class="av {cls}" style="{style}">{AV[k]}</div>'
def svg(inner,txt=''): return f'<svg class="full" viewBox="0 0 1080 1920"><g filter="url(#rough)">{inner}</g>{txt}</svg>'
def chip(t,col=A,top=330): return f'<div class="chip" style="top:{top}px;background:{col}">{t}</div>'
def card(x,y,w=300,h=320,fill=A): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="34" fill="{fill}" stroke="{D}" stroke-width="8"/>'
def T(x,y,t,size=40,col=D,cls=''): return f'<text class="tx {cls}" x="{x}" y="{y}" font-size="{size}" fill="{col}">{t}</text>'

def pill(n,t): return f'<div class="pill"><b>{n}</b>{t}</div>'
def pl(inner,cx,cy,s,ox,oy): return f'<g transform="translate({cx-ox*s:.1f},{cy-oy*s:.1f}) scale({s})">{inner}</g>'
exec(open("scenes.py").read())
css=f'''@font-face{{font-family:"Outfit";src:url("fonts/Outfit-700-latin.woff2") format("woff2");font-weight:500 700;font-display:block}}
@font-face{{font-family:"Maven Pro";src:url("fonts/MavenPro-700-latin.woff2") format("woff2");font-weight:400 700;font-display:block}}
*{{margin:0;padding:0;box-sizing:border-box}}html,body{{width:1080px;height:1920px;overflow:hidden;background:#000}}
#root{{position:relative;width:1080px;height:1920px;overflow:hidden;background:{D};font-family:"Maven Pro",sans-serif;color:#fff}}
#cam{{position:absolute;inset:0}}.lay{{position:absolute;inset:0}}
#glow{{background:radial-gradient(660px 660px at 540px 920px,rgba(107,95,138,.55),rgba(46,37,69,0) 70%)}}
#vig{{background:radial-gradient(900px 1200px at 540px 900px,rgba(0,0,0,0) 45%,rgba(16,11,28,.5) 100%)}}
svg.full{{position:absolute;left:0;top:0;width:1080px;height:1920px;overflow:visible}}
.sc{{position:absolute;inset:0}}
.av{{position:absolute}}.av svg{{width:100%;height:100%}}
.tx{{font-family:"Outfit";font-weight:700;text-anchor:middle}}.tx.left{{text-anchor:start}}
.t{{position:absolute;left:60px;right:60px;font:700 96px/1.16 "Outfit",sans-serif;letter-spacing:-.02em}}
.st{{display:inline-block;background:{A};color:{D};padding:0 20px;border-radius:22px;box-shadow:7px 8px 0 {L};transform:rotate(-2.5deg)}}
.w{{display:inline-block}}
.chip{{position:absolute;left:60px;color:{D};font:700 32px/1 "Maven Pro";letter-spacing:.1em;text-transform:uppercase;padding:15px 26px;border-radius:40px;border:5px solid {D};box-shadow:5px 6px 0 rgba(198,188,226,.6)}}
.chip.ced{{font-size:26px;letter-spacing:.04em;text-transform:none;padding:12px 22px}}
.pill{{position:absolute;left:60px;top:340px;display:flex;align-items:center;gap:20px;font:700 66px/1 "Outfit"}}
.pill b{{display:grid;place-items:center;width:96px;height:96px;border-radius:50%;background:{L};color:{D};border:6px solid {D};box-shadow:5px 6px 0 {R};font:700 56px/1 "Outfit"}}
.q{{position:absolute;left:50px;right:50px;text-align:center;font:700 84px/1.18 "Outfit";letter-spacing:-.02em}}
.q2{{position:absolute;left:60px;right:60px;text-align:center;font:700 64px/1.2 "Outfit"}}
.cap2{{position:absolute;left:60px;right:60px;text-align:center;font:700 50px/1.2 "Outfit";color:{L}}}
.web{{position:absolute;left:0;right:0;top:1345px;text-align:center;font:700 40px "Maven Pro";color:{L}}}
#tr{{position:absolute;left:0;top:0;width:1080px;height:1920px;pointer-events:none}}
.cap{{position:absolute;left:60px;right:60px;top:1460px;text-align:center}}
.plate{{display:inline;background:rgba(46,37,69,.9);color:#fff;font:700 54px/1.42 "Maven Pro",sans-serif;padding:6px 22px;border-radius:18px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}'''
doodles=f'''<svg class="full" viewBox="0 0 1080 1920"><defs><filter id="rough" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence id="turb" type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="1" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="6" xChannelSelector="R" yChannelSelector="G"/></filter></defs>
<g filter="url(#rough)"><g fill="{L}"><path class="sp" d="M120 600l10 26 26 10-26 10-10 26-10-26-26-10 26-10z"/><path class="sp" d="M960 700l8 20 20 8-20 8-8 20-8-20-20-8 20-8z"/><path class="sp" d="M100 1260l7 17 17 7-17 7-7 17-7-17-17-7 17-7z"/><path class="sp" d="M985 1230l9 22 22 9-22 9-9 22-9-22-22-9 22-9z"/></g>
<path class="sq" d="M840 250q20-24 40 0t40 0t40 0" fill="none" stroke="{R}" stroke-width="7" stroke-linecap="round"/><path class="sq" d="M90 260q20-24 40 0t40 0" fill="none" stroke="{L}" stroke-width="7" stroke-linecap="round"/></g></svg>'''
trsvg=f'<svg id="tr" viewBox="0 0 1080 1920"><g filter="url(#rough)"><line id="trl" x1="-40" y1="1380" x2="-40" y2="1380" stroke="{L}" stroke-width="12" stroke-linecap="round" opacity="0"/><circle id="trn" cx="-40" cy="1380" r="26" fill="{A}" stroke="{D}" stroke-width="7" opacity="0"/></g></svg>'
body=''.join(f'<div class="sc clip" id="{i}" data-start="{a}" data-duration="{round(b-a,2)}" data-track-index="1">{h}</div>' for i,a,b,h in SC)
capsh=''.join(f'<div class="cap clip" id="cap{k}" data-start="{a}" data-duration="{d}" data-track-index="5"><span class="plate">{H.escape(t)}</span></div>' for k,(t,a,d) in enumerate(caps))
js=open('anim.js').read().replace('__DUR__',str(DUR)).replace('__BOUND__',json.dumps(BOUND)).replace('__NCAP__',str(len(caps))).replace('__CAPS__',json.dumps([[a] for _,a,_ in caps]))
doc=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=1080, height=1920"><style>{css}</style></head><body>
<div id="root" data-composition-id="kt24full" data-start="0" data-duration="{DUR}" data-width="1080" data-height="1920" data-fps="30">
<div id="cam"><div class="lay" id="glow"></div>{doodles}{body}<div class="lay" id="vig"></div></div>{trsvg}{capsh}
<script src="gsap.min.js"></script><script>(function(){{{js}}})();</script></div></body></html>'''
open('public/index.html','w').write(doc); print(len(SC),'escenas',len(caps),'subtítulos')
