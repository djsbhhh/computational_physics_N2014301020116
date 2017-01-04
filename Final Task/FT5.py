import numpy as np
import matplotlib.pyplot as plt
import math
def wave(r,x01,k,t,tt):
    c3=[]
    c2=[]
    cc=[]
    ca=[]
    ca1=[]
    for i in range(tt):
        tr=math.exp(-k*(i-x01)**2)
        c2.append(tr)
        cc.append(i)
    c2[0]=0
    c2[-1]=0
    ca.append(c2[tt/20])
    ca1.append(0)
    for j in range(t):
        c3.append(c2[0])
        for k in range(1,tt-1):
            c3.append(c2[k]+r*(c2[k+1]+c2[k-1]-2*c2[k]))
        c3.append(c2[-1])
        c2=[]
        for k in range(tt):
            c2.append(c3[k])
        c3=[]
        ca.append(c2[tt/20])
        ca1.append(j+1)
    return c2,cc,ca,ca1
ax1=plt.subplot(811)
ax2=plt.subplot(812)
ax3=plt.subplot(813)
ax4=plt.subplot(814)
ax5=plt.subplot(815)
ax6=plt.subplot(816)
ax7=plt.subplot(817)
ax8=plt.subplot(818)
plt.sca(ax1)
a,b,c,d=wave(0.5,1000,2000,0,2000)
plt.plot(b,a)
plt.sca(ax2)
a,b,c,d=wave(0.5,1000,2000,10,2000)
plt.plot(b,a)
plt.sca(ax3)
a,b,c,d=wave(0.5,1000,2000,100,2000)
plt.plot(b,a)
plt.sca(ax4)
a,b,c,d=wave(0.5,1000,2000,500,2000)
plt.plot(b,a)
plt.sca(ax5)
a,b,c,d=wave(0.5,1000,2000,1000,2000)
plt.plot(b,a)
plt.sca(ax6)
a,b,c,d=wave(0.5,1000,2000,2000,2000)
plt.plot(b,a)
plt.sca(ax7)
a,b,c,d=wave(0.5,1000,2000,4000,2000)
plt.plot(b,a)
plt.sca(ax8)
a,b,c,d=wave(0.5,1000,200,8000,2000)
plt.plot(b,a)
plt.show()
#plt.ylim(0,5000)