# Ejemplo del 36: simulación de dominós cuadro a cuadro (shapely) → domino.json con ángulos por cuadro; cada ficha se apoya en la siguiente sin atravesarla.
# Dominós delgados que crecen. Simulación cuadro a cuadro (30 fps): cada uno cae con aceleración y no puede
# atravesar al siguiente (se apoya en él). Escribe domino.json con pivotes y ángulos por cuadro para build36.py.
import math, json
from shapely.geometry import Polygon
from shapely import affinity
H=[44,66,100,150,224]; Wd=[12,17,26,38,56]; G=400
gap=[0.45*h for h in H]
p=[150]
for k in range(4): p.append(p[k]+gap[k]+Wd[k+1])
def poly(k,th):
    r=Polygon([(p[k]-Wd[k],G-H[k]),(p[k],G-H[k]),(p[k],G),(p[k]-Wd[k],G)])
    return affinity.rotate(r,th,origin=(p[k],G))
def maxang(k,thn):          # mayor ángulo de k sin atravesar a k+1 (que está en thn)
    lo,hi=0.0,90.0
    if not poly(k,90).intersects(poly(k+1,thn)): return 90.0
    for _ in range(22):
        m=(lo+hi)/2
        if poly(k,m).intersection(poly(k+1,thn)).area>0.5: hi=m
        else: lo=m
    return lo
alpha=math.degrees(math.asin(0.45))
d=[0.55*math.sqrt(h/44) for h in H]; t=[65.0]
for k in range(4): t.append(t[k]+d[k]*math.sqrt(alpha/90))
free=lambda k,T: 0 if T<=t[k] else 90*min((T-t[k])/d[k],1)**2
frames=[]; T=t[0]; end=t[4]+d[4]+0.3
while T<=end:
    a=[0]*5; a[4]=free(4,T)
    for k in range(3,-1,-1): a[k]=min(free(k,T),maxang(k,a[k+1]))
    frames.append((round(T,3),[round(x,2) for x in a])); T+=1/30
print('pivotes',[round(x,1) for x in p],'inicio',[round(x,2) for x in t],'final',frames[-1])
json.dump(dict(H=H,W=Wd,p=p,frames=frames),open('domino.json','w'))
