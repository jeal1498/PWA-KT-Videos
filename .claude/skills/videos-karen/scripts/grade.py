# Uso: python3 -I grade.py <salida.cube>  (regenera assets/karen.cube; ajustar P y comparar con scopes)
# Corrección de color "por nodos" para los videos de Karen, exportada como LUT 3D (.cube) para ffmpeg (lut3d).
# Nodo 1 balance de blancos (camisa blanca neutra), 2 exposición en lineal, 3 curva fílmica, 4 secundaria de piel
# (tono a la línea de piel, croma y luz), 5 separación de fondo (morados y verdes del fondo bajan), 6 look sutil de marca.
import numpy as np, sys
def s2l(x): return np.where(x<=0.04045,x/12.92,((x+0.055)/1.055)**2.4)
def l2s(x): x=np.clip(x,0,None); return np.where(x<=0.0031308,x*12.92,1.055*x**(1/2.4)-0.055)
def ycc(r,g,b):
    y=0.2126*r+0.7152*g+0.0722*b; cb=(b-y)/1.8556; cr=(r-y)/1.5748; return y,cb,cr
def rgb(y,cb,cr):
    r=y+1.5748*cr; b=y+1.8556*cb; g=(y-0.2126*r-0.0722*b)/0.7152; return r,g,b
def smooth(x,a,b):   # 0 en a, 1 en b
    t=np.clip((x-a)/(b-a),0,1); return t*t*(3-2*t)
def hue_win(h,c,w):  # ventana suave de tono (grados), c centro, w medio ancho
    d=np.abs((h-c+180)%360-180); return 1-smooth(d,w*0.5,w)
def grade(R,G,B,P):
    # 1 balance + 2 exposición (lineal)
    r,g,b=s2l(R)*P['wb'][0]*P['exp'],s2l(G)*P['wb'][1]*P['exp'],s2l(B)*P['wb'][2]*P['exp']
    r,g,b=l2s(r),l2s(g),l2s(b)
    # 3 curva fílmica en luma (pivote 0.42), con hombro suave
    y,cb,cr=ycc(r,g,b)
    piv=0.42; k=P['contraste']
    yc=piv+(y-piv)*k
    yc=np.where(yc>0.76,0.76+(1-np.exp(-(yc-0.76)/0.24))*0.23,yc)   # hombro: nunca pasa de 0.99
    yc=np.where(yc<0.06,0.06*smooth(yc,-0.05,0.06)+0.012*(1-smooth(yc,-0.05,0.06)),yc) # pie: negros apenas levantados
    yc=np.clip(yc,0.012,0.99)
    sc=np.where(y>1e-4,1.0,1.0); cb,cr=cb*sc,cr*sc; y=yc
    # 4 secundaria de piel (tono en el plano CbCr)
    hue=np.degrees(np.arctan2(cr,cb))%360; ch=np.hypot(cb,cr)
    m=hue_win(hue,126,22)*smooth(ch,0.02,0.05)*(1-smooth(ch,0.20,0.28))*smooth(y,0.18,0.30)*(1-smooth(y,0.92,0.98))
    target=P['piel_tono']
    dh=((target-hue+180)%360-180)*P['piel_fuerza']*m
    hue2=np.radians(hue+dh); ch2=ch*(1+(P['piel_croma']-1)*m)
    cb,cr=ch2*np.cos(hue2),ch2*np.sin(hue2)
    y=y+P['piel_luz']*m
    # 5 separación del fondo: morados/magentas y verdes/turquesas pierden croma y bajan un poco
    hsv_like=hue
    bg=np.maximum(hue_win(hsv_like,10,40),hue_win(hsv_like,300,45))   # morado-azulado en CbCr ~ 330-20°
    bg=np.maximum(bg,hue_win(hsv_like,215,40))                         # verdes y turquesas en CbCr ~ 200-230°
    bg=bg*(1-m)*smooth(ch,0.05,0.10)
    cb,cr=cb*(1-P['fondo_croma']*bg),cr*(1-P['fondo_croma']*bg); y=y*(1-P['fondo_luz']*bg)
    # 6 look: sombras hacia ciruela, luces neutras-cálidas (muy sutil)
    sh=1-smooth(y,0.08,0.40); hl=smooth(y,0.60,0.95)
    cb=cb+P['sombra'][0]*sh+P['luz'][0]*hl; cr=cr+P['sombra'][1]*sh+P['luz'][1]*hl
    r,g,b=rgb(y,cb,cr)
    return np.clip(r,0,1),np.clip(g,0,1),np.clip(b,0,1)
P=dict(wb=(1.072,0.988,0.978),exp=1.10,contraste=1.07,piel_tono=122.0,piel_fuerza=1.0,piel_croma=0.93,piel_luz=0.012,
       fondo_croma=0.22,fondo_luz=0.05,sombra=(0.006,0.004),luz=(-0.004,0.003))
def cube(path,N=33):
    v=np.linspace(0,1,N); B,G,R=np.meshgrid(v,v,v,indexing='ij')
    r,g,b=grade(R.ravel(),G.ravel(),B.ravel(),P)
    with open(path,'w') as f:
        f.write('TITLE "Karen grading"\nLUT_3D_SIZE %d\n'%N)
        for a,c,d in zip(r,g,b): f.write('%.6f %.6f %.6f\n'%(a,c,d))
if __name__=='__main__': cube(sys.argv[1])
