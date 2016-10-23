import math
#Calculate the trajectory
class cannon_shell:
    def __init__(self, init_v = 0, init_theta = 0, time_step = 0, target_altitude = 0, wind_speeed = 0):
        self.x = [0]
        self.y = [0]
        self.init_v = init_v
        self.init_theta = init_theta
        self.vx = [self.init_v * math.cos(self.init_theta / 180 * math.pi) / 1000]
        self.vy = [self.init_v * math.sin(self.init_theta / 180 * math.pi) / 1000]
        self.v_wind = wind_speeed / 1000
        self.dt = time_step
        self.C = 0
        self.h = target_altitude
    def launch(self):
        i = 0
        j = 0
        global high_enough
        global math_error
        math_error = True
        loop_launch = True
        while(loop_launch):
            if (1 - 6.5 * self.y[i] / 288.15) < 0:
                math_error = False
                break
            self.C = 4E-2 * math.pow(1 - 6.5 * self.y[i] / 288.15, 2.5)
            self.x.append(self.x[i] + self.vx[i] * self.dt)
            self.y.append(self.y[i] + self.vy[i] * self.dt)
            self.vx.append(self.vx[i] - self.C * math.sqrt(self.vx[i] ** 2 + self.vy[i] ** 2 + self.v_wind ** 2 + 2 * self.vx[i] * self.v_wind) * abs(self.vx[i] - self.v_wind) * self.dt)
            self.vy.append(self.vy[i] - 9.8E-3 * self.dt - self.C * math.sqrt(self.vx[i] ** 2 + self.vy[i] ** 2 + self.v_wind ** 2 + 2 * self.vx[i] * self.v_wind) * self.dt)
            i += 1
            if (self.y[i] < self.y[i-1]) and (self.y[i-1] < self.h):
                high_enough = False
                loop_launch = False
            if (self.y[i] > self.h) or j:
                j += 1
            if (self.y[i] < self.h) and j:
                loop_launch = False
        if self.y[i-1] > self.h:
            self.x[i] = -(self.y[i-1] - self.h) * (self.x[i] - self.x[i-1]) / (self.y[i] - self.y[i-1]) + self.x[i-1]
            self.y[i] = self.h
            high_enough = True

class shoot(cannon_shell):
    #Given a fixed initial velocity, calculate the maximum of distance
    def find_maxrange(self):
        self.max_range = 0
        self.max_range_theta = self.theta_begin
        temp_max = 0
        loop_maxrange = True
        while(loop_maxrange):
            cannon_shell.__init__(self, self.v, self.max_range_theta, user_input.time_step, user_input.target_y, user_input.wind_speeed)
            cannon_shell.launch(self)
            temp_max = self.x[-1]
            if high_enough and math_error:
                if self.max_range <= temp_max:
                    self.max_range = temp_max
                    self.max_range_theta += self.theta_step
                else:
                    self.max_range_theta -= self.theta_step
                    loop_maxrange = False
            else:
                self.max_range_theta += self.theta_step
            if self.max_range_theta > self.theta_stop:
                loop_maxrange = False
    #scaning range and step
    def detal(self):
        if self.C == 0:
            self.detal_i = 0
            self.v_step = 10
            self.theta_step = 1
            self.v_begin = 0
            self.v_stop = 1000
            self.theta_begin = 0
            self.theta_stop = 90
            print("Please wait...\n\n", [self.v_begin, self.v_stop, self.v_step], [self.theta_begin, self.theta_stop, self.theta_step], "\n")
        else:
            self.v_begin = round(self.temp_v, self.detal_i - 1) - 2 * self.v_step
            self.v_stop = round(self.temp_v, self.detal_i - 1) + 2 * self.v_step
            self.theta_begin = round(self.temp_theta, self.detal_i) - 2 * self.theta_step
            self.theta_stop = round(self.temp_theta, self.detal_i) + 2 * self.theta_step
            self.v_step = round(self.v_step / 10, self.detal_i)
            self.theta_step = round(self.theta_step / 10, self.detal_i + 1)
            print([round(self.v_begin, self.detal_i - 1), round(self.v_stop, self.detal_i - 1), round(self.v_step, self.detal_i)], [round(self.theta_begin, self.detal_i), round(self.theta_stop, self.detal_i), round(self.theta_step, self.detal_i + 1)], "\n")
            self.detal_i += 1
    #Find the closest drop point to the target and the corresponding initial velocity
    def find_close_v(self):
        self.temp_v = 0
        self.temp_theta = 0
        self.d = 0
        self.v = self.v_begin
        loop_v = True
        while(loop_v):
            shoot.find_maxrange(self)
            if high_enough and self.max_range >= user_input.target_x:
                self.temp_v = self.v
                self.temp_theta = self.max_range_theta
                self.d = self.max_range - user_input.target_x
                loop_v = False
            self.v += self.v_step
            if self.v > self.v_stop:
                loop_v = False
    #Further calculation
    def find(self):
        temp_loop_level = 0
        loop_find = True
        print("\n expected loop_level: %.i"%user_input.loop_level, "\n---------------------\n")
        while(loop_find):
            shoot.detal(self)
            shoot.find_close_v(self)
            print("Minimum of initial velocity:", round(self.temp_v, (self.detal_i - 1)), "m/s")
            print("Corresponding angle:", round(self.temp_theta, (self.detal_i)), "°")
            print("Difference relative to the target in horizontal direction:", self.d * 1000, "m")
            temp_loop_level +=1
            print("\n loop_level = ", temp_loop_level, "\n---------------------")
            if temp_loop_level >= user_input.loop_level:
                loop_find = False
        print("\n Minimum of initial velocity:", round(self.temp_v, (self.detal_i - 1)), "m/s")
        print("Corresponding angle:", round(self.temp_theta, (self.detal_i)), "°")
        print("ifference relative to the target in horizontal direction:", self.d * 1000, "m")

#Input datas
class user_input:
    num_str_in = input("Please input Time step dt(s), Wind speed(m/s), Distance of the target(km), Hight of the target(km), Amount of calculating circles, separated by space:\n")
    num = [float(n) for n in num_str_in.split()]
    init_v = 0
    init_theta = 0
    time_step = num[0]
    wind_speeed = num[1]
    target_x = num[2]
    target_y = num[3]
    loop_level = num[4]

#Run
user_input()
start = shoot(user_input.init_v, user_input.init_theta, user_input.time_step, user_input.target_y, user_input.wind_speeed)
start.find()
end = input("--------------------\n Type enter to quit......")