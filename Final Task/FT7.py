import random
import numpy as np
import matplotlib.pyplot as plt
import math
def randpath(n,t,tt):
    y=[]
    a=[]
    b=[]
    for i in range(tt):
        if i<=7*tt/16 or i>=9*tt/16:
           b.append(0)
        else:
           b.append(n)
    c=[0]*tt
    for j in range(tt):
        y.append(c[:])
        if j<=7*tt/16 or j>=9*tt/16:
           a.append(c[:])
        else:
           a.append(b[:])
    for j in range(t):
        for q in range(len(a)):
            for u in range(len(a)):
                if a[q][u]!=0:
                   for i in range(a[q][u]):
                       cc=random.random()
                       a[q][u]=a[q][u]-1
                       if cc<=0.25:
                          if u+1<=len(a)-1:
                             a[q][u+1]=a[q][u+1]+1
                       elif cc<=0.5:
                          if u-1>=0:
                             a[q][u-1]=a[q][u-1]+1
                       elif cc<=0.75:
                          if q-1>=0:
                             a[q-1][u]=a[q-1][u]+1
                       else:
                          if q+1<=len(a)-1:
                             a[q+1][u]=a[q+1][u]+1                           
    return a
ax1=plt.subplot(421)
ax2=plt.subplot(422)
ax3=plt.subplot(423)
ax4=plt.subplot(424)
ax5=plt.subplot(425)
ax6=plt.subplot(426)
ax7=plt.subplot(427)
ax8=plt.subplot(428)
plt.sca(ax1)
tt=128
y=randpath(10,0,tt)
for i in range(len(y)):
    for j in range(len(y[0])):
        if y[i][j]!=0:
           plt.scatter([i,],[j,],7,color='green')
plt.xlim(0,tt)
plt.ylim(0,tt)
plt.sca(ax2)
tt=128
y=randpath(10,10,tt)
for i in range(len(y)):
    for j in range(len(y[0])):
        if y[i][j]!=0:
           plt.scatter([i,],[j,],7,color='green')
plt.xlim(0,tt)
plt.ylim(0,tt)
plt.sca(ax3)
tt=128
y=randpath(10,50,tt)
for i in range(len(y)):
    for j in range(len(y[0])):
        if y[i][j]!=0:
           plt.scatter([i,],[j,],7,color='green')
plt.xlim(0,tt)
plt.ylim(0,tt)
plt.sca(ax4)
tt=128
y=randpath(10,80,tt)
for i in range(len(y)):
    for j in range(len(y[0])):
        if y[i][j]!=0:
           plt.scatter([i,],[j,],7,color='green')
plt.xlim(0,tt)
plt.ylim(0,tt)
plt.sca(ax5)
tt=128
y=randpath(10,100,tt)
for i in range(len(y)):
    for j in range(len(y[0])):
        if y[i][j]!=0:
           plt.scatter([i,],[j,],7,color='green')
plt.xlim(0,tt)
plt.ylim(0,tt)
plt.sca(ax6)
tt=128
y=randpath(10,150,tt)
for i in range(len(y)):
    for j in range(len(y[0])):
        if y[i][j]!=0:
           plt.scatter([i,],[j,],7,color='green')
plt.xlim(0,tt)
plt.ylim(0,tt)
plt.sca(ax7)
tt=128
y=randpath(10,200,tt)
for i in range(len(y)):
    for j in range(len(y[0])):
        if y[i][j]!=0:
           plt.scatter([i,],[j,],7,color='green')
plt.xlim(0,tt)
plt.ylim(0,tt)
plt.sca(ax8)
tt=128
y=randpath(10,300,tt)
for i in range(len(y)):
    for j in range(len(y[0])):
        if y[i][j]!=0:
           plt.scatter([i,],[j,],7,color='green')
plt.xlim(0,tt)
plt.ylim(0,tt)
plt.show()