import random
import numpy as np
import matplotlib.pyplot as plt
import math
def comp(a1,b1,c):
    a=a1[:]
    b=b1[:]
    tq=0
    tq2=[]
    q=False
    while c in b:
          ty=b.index(c)
          tq2.append(ty+tq)
          del b[ty]
          tq=tq+1
    for i in tq2:
        if a[i]==a[-1]:
           q=True
    a=[]
    b=[]
    return q
def addit(x,y):
    t=[0,0,0,0]
    if y[-1]+1 in y and comp(x,y,y[-1]+1):
          t[0]=1
    if y[-1]-1 in y and comp(x,y,y[-1]-1):
          t[1]=1
    if x[-1]-1 in x and comp(y,x,x[-1]-1):
          t[2]=1
    if x[-1]+1 in x and comp(y,x,x[-1]+1):
          t[3]=1 
    return sum(t),t
def randpath(a,b1,x,y):
    b=b1[:]
    xx=[]
    yy=[]
    cx=[]
    cy=[]
    tb=0
    cx.append(x[-1])
    cx.append(x[-1])
    for k in range(-1,2,2):
        cx.append(x[-1]+k)
        cy.append(y[-1]-k)
    cy.append(y[-1])
    cy.append(y[-1])
    while 0 in b:
      ts=[]
      tr=b.index(0)
      ts.append(tr+tb)
      tb=tb+1
      del b[tr]
      for ii in ts:
           x.append(cx[ii])
           y.append(cy[ii])     
           xx.append(x[:])
           yy.append(y[:])
           x.pop()
           y.pop()              
    return xx,yy
"""
x=[0,0,1,1]
y=[0,1,1,0]
q,p=addit(x,y)
print p
"""

tt2=[]
cr=[]
rr=[]
x1=[0]
y1=[0]
ty=[]
pp=[]
a,b=addit(x1,y1)
c,d= randpath(a,b,x1,y1)
rr1=0
rt=0
tt2.append(1)
for k in range(len(c)):
        rr1=rr1+(c[k][-1]**2+d[k][-1]**2)*1.0/len(c)
rr.append(rr1)
for ii in range(len(c)):
        rt=rt+((c[ii][-1]**2+d[ii][-1]**2)-rr1)**2*1.0/len(c)
cr.append(math.sqrt(rt))
pp.append(len(c))
for j in range(9):
    tt2.append(j+2)
    rr1=0
    rt=0
    tw=[]
    te=[]
    for i in range(len(c)):
        a,b=addit(c[i],d[i])
        g,h=randpath(a,b,c[i],d[i])
        tw=tw+g
        te=te+h
    pp.append(len(tw))
    c=tw[:]
    d=te[:]
    for k in range(len(c)):
        rr1=rr1+(c[k][-1]**2+d[k][-1]**2)*1.0/len(c)
    rr.append(rr1)
    for ii in range(len(c)):	
        rt=rt+((c[ii][-1]**2+d[ii][-1]**2)-rr1)**2*1.0/len(c)
    cr.append(math.sqrt(rt))
"""
ax1=plt.subplot(121)
ax2=plt.subplot(122)
plt.sca(ax1)
plt.plot(tt2,cr,color='blue')
for k in range(len(tt2)):
    plt.scatter([tt2[k],],[cr[k],],12,color='red')
    plt.plot([tt2[k],tt2[k]],[0,cr[k]],linewidth=1.0,linestyle='--',color='orange')
plt.ylim(0,)
plt.xlim(1,)
plt.xlabel('time/number of steps')
plt.ylabel('the average of standard deviation')
plt.title('the variation of standard deviation versus time')
plt.sca(ax2)
plt.plot(tt2,rr,color='blue')
for k in range(len(tt2)):
    plt.scatter([tt2[k],],[rr[k],],12,color='red')
    plt.plot([tt2[k],tt2[k]],[0,rr[k]],linewidth=1.0,linestyle='--',color='orange')
plt.ylim(0,)
plt.xlim(1,)
plt.xlabel('time/number of steps')
plt.ylabel('the average of square distance')
plt.title('the variation of distance versus time')
plt.show()
"""
"""
plt.plot(tt2,pp,color='blue')
for k in range(len(tt2)):
    plt.scatter([tt2[k],],[pp[k],],12,color='red')
    plt.plot([tt2[k],tt2[k]],[0,pp[k]],linewidth=1.0,linestyle='--',color='orange')
plt.ylim(0,)
plt.xlim(1,)
plt.xlabel('time/number of steps')
plt.ylabel('number of SAWs')
plt.title('number of SAWS versus time')
plt.show()
"""
tt3=[]
rg=[]
rg.append(rr[0])
tt3.append(1)
for i in range(1,len(rr)):
    rg.append(rr[i]/rr[i-1])
    tt3.append(1.0/(tt2[i]-1))
plt.plot(tt2,rg)
plt.show()
#print pp
#print rr