import math
import pylab as pl

class Bifurcation_diagram:
    def __init__(self, F_D = 1.2, total_time = 60, init_theta = 0.2, q = 0.5, l = 9.8, g = 9.8, Omega_D = 2/3, time_step = 0.04):
        self.omega = [0]
        self.theta = [init_theta]
        self.t = [0]
        self.dt = time_step
        self.total_time = total_time
        self.q = q
        self.l = l
        self.g = g
        self.Omega_D = Omega_D
        self.F_D = F_D
    def calculate(self):
        n = 1
        self.tmp_theta = []
        self.tmp_F_D = []
        m = 100000
        self.total_time = 2 * 400 * math.pi / self.Omega_D
        self.dt = self.total_time / m
        for i in range(m + 1):
            self.omega.append(self.omega[i] + ((-self.g / self.l) * math.sin(self.theta[i]) - self.q * self.omega[i] + self.F_D * math.sin(self.Omega_D * self.t[i])) * self.dt)
            self.theta.append(self.theta[i] + self.omega[i + 1] * self.dt)
            self.t.append(self.dt * (i + 1))
            if self.theta[i + 1] < -math.pi:
                self.theta[i + 1] = self.theta[i + 1] + 2 * math.pi
            if self.theta[i + 1] > math.pi:
                self.theta[i + 1] = self.theta[i + 1] - 2 * math.pi
            #$\Omega_Dt=2n\pi$
            if  abs(self.t[i + 1] - 2 * n * math.pi / self.Omega_D) < self.dt / 2 :
                if i > 75000:
                    if round(self.theta[-1], 4) not in self.tmp_theta:
                        self.tmp_theta.append(round(self.theta[-1], 4))
                        self.tmp_F_D.append(self.F_D)
                n += 1
bif_F_D = []
bif_theta = []
len_bif_theta = 0
F_k = []
k = []
loop_i = True
step = 300
for i in range(step + 1):
    F_D = round(1.35 + 0.15 / step * i, 4)
    start = Bifurcation_diagram(F_D)
    start.calculate()
    bif_F_D += start.tmp_F_D
    bif_theta += start.tmp_theta
    print(start.tmp_theta, i, "/", step)
    temp_len_bif_theta = len(start.tmp_theta)
    if len_bif_theta != temp_len_bif_theta:
        F_k.append(F_D)
        k.append(temp_len_bif_theta)
        len_bif_theta = temp_len_bif_theta
pl.plot(bif_F_D, bif_theta, 'k.')
pl.xlabel('$F_D$', fontsize=20)
pl.ylabel('$\\theta$(radians)', fontsize=20)
pl.title('$\\theta$ versus $F_D$', fontsize=20)
pl.show()
for i in range(len(F_k)):
    print("values of F_k, k:", F_k[i], ",", k[i])