import pylab as pl
import math
import numpy as np
class simple_harmonic_motion(object):
    
    def __init__(self, time_step = 0.04, time_duration = float(input('time duration: ')), initial_theta = float(input('initial theta: ')), length = 9.8, strength_of_damping = float(input('damping factor: ')), amplitude = float(input('amplitude of driving force: ')), anguluar_frequency = 0.66666666):
        self.l = length
        self.dt = time_step
        self.T = time_duration
        self.n_steps = int(self.T / self.dt + 1)
        self.theta = [initial_theta]
        self.omega = [0]
        self.t = [0]
        self.g = 9.8
        self.q = strength_of_damping
        self.F_D = amplitude   #The unit of F_D is /s²
        self.Omega_D = anguluar_frequency
    
    def calculate(self):
        for i in range(self.n_steps):
            self.omega.append(self.omega[i] - self.g / self.l * math.sin(self.theta[i]) * self.dt - self.q * self.omega[i] * self.dt + self.F_D * math.sin(self.Omega_D * self.t[i]) * self.dt)
            self.theta.append(self.theta[i] + self.omega[i + 1] * self.dt)
            self.t.append(self.t[i] + self.dt)
        global omega
        omega = self.omega
        global time_array
        time_array = np.array(self.t)
        global a
        a = np.array(self.theta)
        
    def calculate_delta(self):
        b= simple_harmonic_motion()
        b.calculate()
        self.theta_1 = a
        b= simple_harmonic_motion(time_duration = float(input('time duration: ')), initial_theta = float(input('initial theta: ')), strength_of_damping = float(input('damping factor: ')), amplitude = float(input('amplitude of driving force: ')))
        b.calculate()
        self.theta_2 = a
        self.delta = [abs(self.theta_1[0] - self.theta_2[0])]
        self.time_array = time_array
        for i in range(self.n_steps):
            self.delta.append(abs(self.theta_1[i + 1] - self.theta_2[i + 1]))

    def phase(self):
        self.n = int(self.T / (3 * math.pi))
        self.time_phase = [0]
        self.theta_phase = [0.2]
        self.omega_phase = [0]
        for i in range(self.n):
            index = int(3 * (i + 1) * math.pi / self.dt)
            if abs(self.t[index] - 3 * (i + 1)) < self.dt / 2:
                self.time_phase.append(self.t[index])
                self.omega_phase.append(self.omega[index])
                self.theta_phase.append(self.theta[index])
            else:
                self.time_phase.append(self.t[index + 1])
                self.omega_phase.append(self.omega[index + 1])
                self.theta_phase.append(self.theta[index + 1])
        
    
    def show(self):
        pl.plot(self.time_array,self.delta)
            
    def show_log(self):
        pl.semilogy(self.time_array, self.delta, 'c')
        pl.xlabel('$time (s)$')
        pl.ylabel('$\\Delta\\theta$ (radians)')
        pl.xlim(0, self.T)
        pl.ylim(1E-6, 100)
        pl.text(35.5, 1E-5, '$\\Delta\\theta$ versus time $F_D = 1.2$', fontsize = 'x-large')
        pl.title('Chaotic Regime')
        pl.show()

    def multi_show(self):
        for i in range(2):
            a = simple_harmonic_motion(time_step = float(input('time step: ')), time_duration = float(input('time duration: ')), initial_theta = float(input('initial theta: ')), length = float(input('length: ')), strength_of_damping = float(input('stength of damping: ')), amplitude = float(input('amplitude of driving force: ')), anguluar_frequency = float(input('angular frequency of driving force: ')))
            a.calculate()
            a.show()
        pl.show()

s = simple_harmonic_motion()
s.calculate_delta()
s.show_log()