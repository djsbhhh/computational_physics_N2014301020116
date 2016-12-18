import numpy as np
import matplotlib.pyplot
from pylab import *
from math import *
import mpl_toolkits.mplot3d
def power_spe(xe,xo):#xe excited, xo observed
    dx=0.01
    c=300.0 #speed
    dt=dx/c
    length=int(1.0/dx)
    time=3000
    k=1000
    y=[[0 for i in range(length)]for n in range(time)]#i represents x, n represents t
#initialize
    for i in range(length):
        y[0][i]=exp(-k*(i*dx-xe)**2)
        y[1][i]=exp(-k*(i*dx-xe)**2)
    r=c*dt/dx
        
#iteration
    for n in range(time-2):
        for i in range(1,length-1):
            y[n+2][i]=2*(1-r**2)*y[n+1][i]-y[n][i]+r**2*(y[n+1][i+1]+y[n+1][i-1])
    y=array(y)
    yo=[]
    t=array(range(time))*dt
    for n in range(time):
        yo.append(y[n][int(xo/dx)])
    p=abs(np.fft.rfft(yo))**2
    f = np.linspace(0, int(1/dt/2), len(p))
    plot(f, p,color='black')
    xlim(0,3000)
    xlabel('Frequency(Hz)')
    ylabel('Power(arbitrary units)')
    title('Problem 6.13')

figure(figsize=[10,10])
power_spe(0.8,0.5)
show()