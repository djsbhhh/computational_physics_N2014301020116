import random
import numpy as np
import matplotlib.pyplot as plt
import math
def randpath(tt):
    b=[]
    bb=[]
    b.append(0)
    bb.append(0)
    b2=[]
    for i in range(tt):
        c=random.random()
        bb.append(i+1)
        if c<=0.5:
           b.append(b[-1]+1)
        else:
           b.append(b[-1]-1)
    for j in range(len(b)):
        b2.append(b[j])
    return b,bb,b2
a,b,c=randpath(1000)
a1,b1,c1=randpath(1000)
for k in range(len(b)):
    plt.scatter([b[k],],[c[k],],10,color='blue')
    plt.scatter([b1[k],],[c1[k],],10,color='red')
plt.xlim(0,1000)
plt.xlabel('time/step number')
plt.ylabel('X')
plt.title('1D random walk')
plt.show()
"""
c111=[0]*101
for i in range(2000):
    a1,b1,c1=randpath(100)
    for j in range(len(a1)):
        c111[j]=c111[j]+c1[j]/2000.0
for k in range(len(b1)):
    plt.scatter([b1[k],],[c111[k],],5,color='orange',label='the average for 2000')
c22=[]
c11=[0]*101
for i in range(20000):
    a1,b1,c1=randpath(100)
    for j in range(len(a1)):
        c11[j]=c11[j]+c1[j]/20000.0
for k in range(len(b1)):
    plt.scatter([b1[k],],[c11[k],],5,color='green',label='the average for 20000')
# plt.scatter([b1[k],],[a1[k],], 3, color ='orange')
z1=np.polyfit(b1, c11,1)
for i in range(len(b1)):
    c22.append(z1[0]*b1[i]+z1[1])
plt.plot(b1,c22,color='red')
plt.xlim(0,100)
plt.ylim(0,100)
plt.xlabel('time/step number')
plt.ylabel('the average square distance')
plt.title('1D random walk')
print z1
#plt.legend(loc='upper right',frameon=True)
plt.show()
"""