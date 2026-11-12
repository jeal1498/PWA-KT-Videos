# Uso: python3 -I scopes.py antes.png despues.png salida.png  (cuadro, acercamiento a la cara, forma de onda y vectorescopio; línea de piel a 123°)
import numpy as np, sys, math
from PIL import Image, ImageDraw, ImageFont
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',26); f2=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',18)
def scopes(p):
    im=np.asarray(Image.open(p).convert('RGB')).astype(float)/255
    r,g,b=im[...,0],im[...,1],im[...,2]; y=0.2126*r+0.7152*g+0.0722*b; cb=(b-y)/1.8556; cr=(r-y)/1.5748
    # forma de onda
    Wf,Hf=420,220; wf=np.zeros((Hf,Wf))
    xs=(np.arange(y.shape[1])*Wf//y.shape[1]); yy=np.clip(((1-y)*(Hf-1)).astype(int),0,Hf-1)
    np.add.at(wf,(yy,np.broadcast_to(xs,y.shape)),1)
    wf=np.clip(np.log1p(wf)/np.log1p(wf.max())*1.6,0,1)
    W=Image.fromarray((np.stack([wf*0.55,wf,wf*0.6],2)*255).astype(np.uint8))
    d=ImageDraw.Draw(W)
    for v in (0,0.25,0.5,0.75,1): d.line((0,(1-v)*(Hf-1),Wf,(1-v)*(Hf-1)),fill=(70,70,70))
    # vectorescopio
    S=220; vs=np.zeros((S,S)); k=S/2/0.32
    xi=np.clip((S/2+cb*k).astype(int),0,S-1); yi=np.clip((S/2-cr*k).astype(int),0,S-1)
    np.add.at(vs,(yi[::2,::2],xi[::2,::2]),1)
    vs=np.clip(np.log1p(vs)/np.log1p(vs.max())*1.5,0,1)
    V=Image.fromarray((np.stack([vs,vs,vs],2)*255).astype(np.uint8)); d=ImageDraw.Draw(V)
    d.ellipse((5,5,S-5,S-5),outline=(80,80,80)); a=math.radians(123)
    d.line((S/2,S/2,S/2+math.cos(a)*S/2,S/2-math.sin(a)*S/2),fill=(255,170,90),width=2)
    return W,V
a,b,out=sys.argv[1],sys.argv[2],sys.argv[3]
A=Image.open(a).convert('RGB'); B=Image.open(b).convert('RGB'); s=0.42
A=A.resize((int(A.width*s),int(A.height*s))); B=B.resize(A.size)
Wa,Va=scopes(a); Wb,Vb=scopes(b)
col=max(A.width,Wa.width+10+Va.width)
FA=Image.open(a).convert('RGB'); FB=Image.open(b).convert('RGB'); w0,h0=FA.size; box=(int(w0*.22),int(h0*.14),int(w0*.78),int(h0*.44))
FA=FA.crop(box); FB=FB.crop(box); kz=col/FA.width; FA=FA.resize((col,int(FA.height*kz))); FB=FB.resize(FA.size)
im=Image.new('RGB',(col*2+30,A.height+FA.height+Wa.height+100),(22,20,30)); d=ImageDraw.Draw(im)
for i,(P,W,V,t) in enumerate(((A,Wa,Va,'ANTES'),(B,Wb,Vb,'DESPUÉS'))):
    x=i*(col+30); im.paste(P,(x+(col-P.width)//2,0))
    d.rectangle((x+(col-P.width)//2+10,10,x+(col-P.width)//2+10+len(t)*19+14,46),fill=(46,37,69)); d.text((x+(col-P.width)//2+17,13),t,font=F,fill='white')
    im.paste((FA,FB)[i],(x,P.height+10)); y0=P.height+FA.height+50; im.paste(W,(x,y0)); im.paste(V,(x+W.width+10,y0))
    d.text((x,y0-26),'Forma de onda',font=f2,fill=(200,200,200)); d.text((x+W.width+10,y0-26),'Vectorescopio',font=f2,fill=(200,200,200))
im.save(out); print(im.size)
