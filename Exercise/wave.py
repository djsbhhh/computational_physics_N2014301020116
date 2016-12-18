import matplotlib.pyplot as plt
import numpy as np
import math
#设置常量
constant_dx=0.005
constant_c=300.0
constant_dt=constant_dx/constant_c
constant_r=constant_c*constant_dt/constant_dx
total_L=1.0
total_t=0.1
total_M=int(total_L/constant_dx)
total_N=int(total_t/constant_dt)
#初始化Cy
Cy=[[0.0 for i in range(total_M+1)] for n in range (total_N+1)]
for n in range(total_N+1):
    for i in range(total_M+1):
        Cy[n][i]=0.0
Cx0=0.3

#constant_k=1000
#for n in range(total_N+1):
#    for i in range(total_M+1):
#        Cy[n][i]=math.e**(-constant_k*((i*constant_dx-Cx0)**2))
#    Cy[n][0]=0.0
#    Cy[n][-1]=0.0

constant_k=1000
intCx0=int(Cx0/constant_dx)
for n in range(total_N+1):
    for i in range(0,intCx0):
        Cy[n][i]=1.0/0.3*i*constant_dx
    for i in range(intCx0,total_M+1):
        Cy[n][i]=-1.0/0.7*(i*constant_dx-Cx0)+1
    Cy[n][0]=0.0
    Cy[n][-1]=0.0

#计算过程
for n in range(2,total_N):
    for i in range(1,total_M): 
        Cy[n+1][i]=2*(1-constant_r**2)*Cy[n][i]-Cy[n-1][i]+(constant_r**2)*(Cy[n][i+1]+Cy[n][i-1])
    Cy[n][0]=0.0
    Cy[n][-1]=0.0
#绘制图像
plt.figure(figsize=(15,15))
plot_cx=[]
plot_cy=[]
for i in range(total_M+1):
    plot_cx.append(i*constant_dx)
    plot_cy.append(Cy[0][i])
plt.subplot(12, 1, 1)
plt.title("problem 6.12(Gaussian profile)")
plt.xlim(0,1)
plt.ylim(-1,1)
plt.plot(plot_cx,plot_cy,color='black',label="0")
for nt in range(11):
    plot_cx=None
    plot_cy=None
    plot_cx=[]
    plot_cy=[]
    for i in range(total_M+1):
        plot_cx.append(i*constant_dx)
        plot_cy.append(Cy[(nt+1)*8][i])
    plt.subplot(12, 1, nt+2)
    plt.xlim(0,1)
    plt.ylim(-1,1)
    plt.plot(plot_cx,plot_cy,color='black',label=str(nt))
plt.show()
plot_ct=[]
plot_cyt=[]
Ctx=0.01
Nposition=int(Ctx/constant_dx)
for i in range(total_N+1):
    plot_ct.append(i*constant_dt)
    plot_cyt.append(Cy[i][Nposition])
plt.figure(figsize=(15,15))
plt.title("problem 6.12(Gaussian profile)")
plt.plot(plot_ct,plot_cyt,color='black')
plt.xlabel("Time(s)")
plt.ylabel("y(m)")
plt.show()