import math
import matplotlib.pylab as pl
#The unit: time: yr, length: AU
class about_Mercury:
    def __init__(self, alpha = 0.01, total_time = 1, x = 1, y = 0, a = 0.39, e = 0.206):
        #the initial condition: apogee
        self.C = 4 * math.pi**2 #GM_S
        self.alpha = alpha
        self.x = [a * (1 + e)]
        self.y = [0]
        self.vx = 0
        self.vy = math.sqrt((1 - e) / (1 + e) * self.C / a)
        self.r = [a * (1 + e)]
        self.total_time = total_time
        self.dt = 0.0001
        self.t = [0]
        #远日点的相关参数初始化
        self.p_x = []
        self.p_y = []
        self.p_t = []
        self.n = 0
        self.theta = []
    def calculate(self):
        while(self.t[-1] <= self.total_time):
            self.vx = self.vx - self.C * self.x[-1] * self.dt / self.r[-1]**3 * (1 + (self.alpha / self.r[-1]**2))
            self.x.append(self.x[-1] + self.vx * self.dt)
            self.vy = self.vy - self.C * self.y[-1] * self.dt / self.r[-1]**3 * (1 + (self.alpha / self.r[-1]**2))
            self.y.append(self.y[-1] + self.vy * self.dt)
            self.r.append(math.hypot(self.x[-1], self.y[-1]))
            self.t.append(self.t[-1] + self.dt)
            #记录远日点的相关参数
            if self.t[-1] > self.dt * 3 and self.r[-2] > self.r[-1] and self.r[-2] > self.r[-3]:
                self.p_x.append(self.x[-2])
                self.p_y.append(self.y[-2])
                self.p_t.append(self.t[-2])
                self.n = self.n + 1
    #进动轨迹图
    def show_result_precession(self):
        pl.title('Simulation of the precession of Mercury', fontsize=20)
        pl.xlabel('x($AU$)', fontsize=20)
        pl.ylabel('y($AU$)', fontsize=20)
        pl.text(-0.45, -0.45, '$\\alpha = %f$'%self.alpha, fontsize=20)
        pl.xlim(-0.5, 0.5)
        pl.ylim(-0.5, 0.5)
        pl.plot(self.x, self.y, '.k')
        for i in range(self.n):
            pl.plot([0, self.p_x[i]], [0, self.p_y[i]], 'k')
        pl.grid()
        pl.show()
    #时间与进动角度关系图
    def show_result_theta_versus_time(self):
        for i in range(self.n):
            self.theta.append(math.atan(self.p_y[i] / self.p_x[i]) / 2 / math.pi * 360)
        pl.title('Orbit orientation versus time', fontsize=20)
        pl.xlabel('time($yr$)', fontsize=20)
        pl.ylabel('$\\theta$(degrees)', fontsize=20)
        pl.text(self.p_t[-1] * 0.1, self.theta[-1] * 0.9, '$\\alpha = %f$'%self.alpha, fontsize=20)
        pl.xlim(0, self.p_t[-1] * 1.1)
        pl.ylim(0, self.theta[-1] * 1.1)
        pl.plot(self.p_t, self.theta, 'ok')
        pl.plot([0, self.p_t[-1] * 1.05], [0, self.theta[-1] * 1.05], 'k')
        pl.show()
        print(self.theta[-1] / self.p_t[-1])
    #进动率与相对论系数关系图
    def show_result_precession_rate_versus_alpha(self):
        self.alpha_1 = [0]
        self.dtheta_dt = [0]
        for i in range(10):
            alpha = 0.001 + 0.0003 * i
            tmp = about_Mercury(alpha, 2)
            tmp.calculate()
            tmp.show_result_theta_versus_time()
            self.alpha_1.append(alpha)
            self.dtheta_dt.append(tmp.theta[-1] / tmp.p_t[-1])
        pl.title('Simulation of the precession of Mercury', fontsize=20)
        pl.xlabel('$\\alpha$', fontsize=20)
        pl.ylabel('$\\theta/dt$(degrees/yr)', fontsize=20)
        pl.text(self.alpha_1[-1] * 0.05, self.dtheta_dt[-1] * 0.95, 'Precession rate versus $\\alpha$', fontsize=20)
        pl.xlim(0, self.alpha_1[-1] * 1.1)
        pl.ylim(0, self.dtheta_dt[-1] * 1.1)
        pl.plot(self.alpha_1, self.dtheta_dt, 'ok')
        pl.plot([0, self.alpha_1[-1] * 1.05], [0, self.dtheta_dt[-1] * 1.05], 'k')
        pl.show()
        

start = about_Mercury(0.001, 2)
start.calculate()
start.show_result_precession()
start.show_result_theta_versus_time()
#start.show_result_precession_rate_versus_alpha()