from __future__ import division 
import matplotlib 
import numpy as np 
import matplotlib.cm as cm 
import matplotlib.mlab as mlab 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
from copy import deepcopy
from pylab import *

#初始化函数，规定边界条件
v = []
for i in range(101):    
    row_i = []
    for j in range(101):
        if i == 0 or i == 100 or j == 0 or j == 100:
            voltage = 0
        elif 40<=i<=60 and j == 40:
            voltage = 1
        elif 40<=i<=60 and j == 60:
            voltage = -1
        else:
            voltage = 0
        row_i.append(voltage)
    v.append(row_i)

#计算过程，定义更新函数
def update_V(v):

    delta_V = 0

    for i in range(101):    
        for j in range(101):
            if i == 0 or i == 100 or j == 0 or j == 100:
                pass
            elif 40<=i<=60 and j == 40:
                pass
            elif 40<=i<=60 and j == 60:
                pass
            else:
                voltage_new = (v[i+1][j]+v[i-1][j]+v[i][j+1]+v[i][j-1])/4
                voltage_old = v[i][j]
                delta_V += abs(voltage_new - voltage_old)
                v[i][j] = voltage_new

    return v, delta_V
 #定义laplace函数方程，设置迭代   
def Laplace_calculate(v):
    
    epsilon = 10**(-5)*100**2
    delta_V = 0
    N_iter = 0

    while delta_V >= epsilon or N_iter <= 10:
        v1, delta_V = update_V(v)
        v2, delta_V = update_V(v1)
        v = v2
        N_iter += 1

    return v2

x = np.linspace(0,100,101)
y = np.linspace(0,100,101)
X, Y = np.meshgrid(x, y)
Z = Laplace_calculate(v)
Ex = deepcopy(Z)
Ey = deepcopy(Z)
E = deepcopy(Z)

for i in range(101):
    for j in range(101):
        if i == 0 or i == 100 or j == 0 or j == 100:
            Ex[i][j] = 0
            Ey[i][j] = 0
        else:
            Ex_value = -(Z[i+1][j] - Z[i][j])/2
            Ey_value = -(Z[i][j+1] - Z[i][j])/2
            Ex[i][j] = Ex_value
            Ey[i][j] = Ey_value

for i in range(101):
    for j in range(101):
        E_value = np.sqrt(Ex[i][j]**2 + Ey[i][j]**2)
        E[i][j] = E_value

plt.figure()
plt.figure(figsize=(10,10))
CS = plt.contour(X,Y,Z, 30, alpha=1,colors='black')
plt.clabel(CS, inline=1, fontsize=12)
plt.title('Electric potential near two metal plates(1)')
plt.xlabel('x')
plt.ylabel('y')

fig = figure()
ax = Axes3D(fig)
surf=ax.plot_surface(X, Y, Z,rstride=1, cstride=1, cmap=cm.cool,linewidth=0, antialiased=False) 
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('voltage(V)')
ax.set_title('Electric potential near two metal plates(2)')
fig.colorbar(surf,shrink=0.5,aspect=5)

fig0, ax0 = plt.subplots()
plt.figure(figsize=(10,10))
strm = ax0.streamplot(X, Y, np.array(Ey), np.array(Ex), color='black', linewidth=0.1, cmap=plt.cm.autumn)
ax0.set_xlabel('x')
ax0.set_ylabel('y')
ax0.set_xlim(0,100)
ax0.set_title('Electric field')

plt.show()