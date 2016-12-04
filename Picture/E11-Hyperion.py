import numpy as np
from pylab import *
from math import *
#函数定义
def Hyperion(theta0):
    x=[]
    x.append(1)
    v_x=[]
    v_x.append(0)
    y=[]
    y.append(0)
    v_y=[]
    v_y.append(2*pi+1)
    #初值的设置
    omega=[]
    omega.append(10)
    theta=[]
    theta.append(theta0)
    t=[]
    t.append(0)
    time=20.0
    dt=0.0001
    #循环语句的设置
    for i in range(int(time/dt)):
        r=sqrt(x[i]**2+y[i]**2)
        v_x.append(v_x[i]-4*pi**2*x[i]*r**(-3)*dt)
        x.append(x[i]+v_x[i+1]*dt)
        v_y.append(v_y[i]-4*pi**2*y[i]*r**(-3)*dt)
        y.append(y[i]+v_y[i+1]*dt)
        omega.append(omega[i]-dt*12*pi**2*r**(-5)*(x[i]*sin(theta[i])-y[i]*cos(theta[i]))*(x[i]*cos(theta[i])+y[i]*sin(theta[i])))
        theta.append(theta[i]+omega[i+1]*dt)
        t.append(t[i]+dt)
        #角度限制的设置
    return [theta,omega,t,x,y]
H0=Hyperion(0)
theta=H0[0]
omega=H0[1]
t=H0[2]
x=H0[3]
y=H0[4]
H1=Hyperion(0.01)
dtheta=np.array(H1[0])-np.array(H0[0])
#绘制图像
figure(figsize=[15,5])

subplot(131)
plot(x,y,color = "black")
xlim(-3,3)
ylim(-3,3)
title('The trajectory of centroid',fontsize=15)
xlabel('$x_{C}$/HU')
ylabel('$y_{C}$/HU')


subplot(132)
plot(t,theta,color = "black")
title('Hyperion $\theta$ versus time',fontsize=15)
xlabel('time/yr')
ylabel('theta/rad')

subplot(133)
plot(t,omega,color = "black")
title('Hyperion $\omega$ versus time',fontsize=15)
xlabel('time/yr')
ylabel('omega/(rad/yr)')
show()

figure(figsize=[8,8])
plot(t,dtheta,color = "black")
title('Hyperion $\Delta\theta$ versus time',fontsize=15)
xlabel('time/yr')
ylabel('$\Delta\theta$/rad')

figure(figsize=[8,8])
plot(theta,omega,color = "black")
title('Hyperion $\omega$ versus $\theta $',fontsize=15)
xlabel('theta/rad')
ylabel('omega/(rad/yr)')
show()