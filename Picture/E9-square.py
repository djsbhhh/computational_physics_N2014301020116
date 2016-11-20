import math
import pylab as pl

class billiaro_collision_square:
    #初始化
    def __init__(self, x = 0.2, y = 0, vx = 1.2, vy = 1.332, l = 1, total_time = 100):
        self.l = l
        self.x = [x]
        self.y = [y]
        self.vx = vx
        self.vy = vy
        self.ps_x = []
        self.ps_vx = []
        self.total_road = total_time * math.hypot(vx, vy)
        self.passed_road = [0]
        print("\n小球的横向与纵向的分速度分别为：", self.vx, self.vy)
        print("运动总时间为：", total_time)
        print("运动的总路程为：", self.total_road)       
    #计算部分
    def calculate(self):
        loop_calculate = True
        while(loop_calculate):
            k = self.vy / self.vx
            m = self.y[-1] - self.x[-1] * k
            temp_vx = self.vx
            #匀速直线运动部分（循环）
            while(True):
                #速度方向垂直于y轴时
                if self.vx == 0 and self.vy > 0:
                    self.x.append(self.x[-1])
                    self.y.append(self.l)
                    self.vy = -self.vy
                    break
                #速度方向垂直于y轴时
                if self.vx == 0 and self.vy < 0:
                    self.x.append(self.x[-1])
                    self.y.append(-self.l)
                    self.vy = -self.vy
                    break
                #速度方向在第一象限
                if self.vx > 0 and self.vy >= 0:
                    #以小球位置与墙壁拐角处连线把第一象限分成两部分，速度在逆时针方向的前一半
                    if k < (self.l - self.y[-1]) / (self.l - self.x[-1]):
                        self.y.append(self.l * k + m)
                        self.x.append(self.l)
                        self.vx = -self.vx
                        break
                    #以小球位置与墙壁拐角处连线把第一象限分成两部分，速度在逆时针方向的后一半
                    if k > (self.l - self.y[-1]) / (self.l - self.x[-1]):
                        self.x.append((self.l - m) * self.vx / self.vy)
                        self.y.append(self.l)
                        self.vy = -self.vy
                        break
                    #速度与小球位置与墙壁拐角处连线的方向重合
                    if k == (self.l - self.y[-1]) / (self.l - self.x[-1]):
                        self.x.append(self.l)
                        self.y.append(self.l)
                        self.vx = -self.vx
                        self.vy = -self.vy
                        break
                #速度方向在第二象限
                if self.vx < 0 and self.vy >= 0:
                    if k < (self.l - self.y[-1]) / (-self.l - self.x[-1]):
                        self.x.append((self.l - m) / k)
                        self.y.append(self.l)
                        self.vy = -self.vy
                        break
                    if k > (self.l - self.y[-1]) / (-self.l - self.x[-1]):
                        self.y.append(-k * self.l + m)
                        self.x.append(-self.l)
                        self.vx = -self.vx
                        break
                    if k == (self.l - self.y[-1]) / (-self.l - self.x[-1]):
                        self.x.append(-self.l)
                        self.y.append(self.l)
                        self.vx = -self.vx
                        self.vy = -self.vy
                        break
                #速度方向在第三象限
                if self.vx < 0 and self.vy <= 0:
                    if k < (-self.l - self.y[-1]) / (-self.l - self.x[-1]):
                        self.y.append(-k * self.l + m)
                        self.x.append(-self.l)
                        self.vx = -self.vx
                        break
                    if k > (-self.l - self.y[-1]) / (-self.l - self.x[-1]):
                        self.x.append((-self.l - m) / k)
                        self.y.append(-self.l)
                        self.vy = -self.vy
                        break
                    if k == (-self.l - self.y[-1]) / (-self.l - self.x[-1]):
                        self.x.append(-self.l)
                        self.y.append(-self.l)
                        self.vx = -self.vx
                        self.vy = -self.vy
                        break
                #速度方向在第四象限
                if self.vx > 0 and self.vy <= 0:
                    if k < (-self.l - self.y[-1]) / (self.l - self.x[-1]):
                        self.x.append((-self.l - m) / k)
                        self.y.append(-self.l)
                        self.vy = -self.vy
                        break
                    if k > (-self.l - self.y[-1]) / (self.l - self.x[-1]):
                        self.y.append(k * self.l + m)
                        self.x.append(self.l)
                        self.vx = -self.vx
                        break
                    if k == (-self.l - self.y[-1]) / (self.l - self.x[-1]):
                        self.x.append(self.l)
                        self.y.append(-self.l)
                        self.vx = -self.vx
                        self.vy = -self.vy
                        break
            #累计路程
            self.passed_road.append(self.passed_road[-1] + math.hypot(self.x[-1] - self.x[-2], self.y[-1] - self.y[-2]))
            #判断路程是不是超过了总路程
            if self.passed_road[-1] > self.total_road:
                temp_x = self.x[-1]
                temp_y = self.y[-1]
                #计算出小球的停止位置
                self.x[-1] = self.x[-2] + (temp_x - self.x[-2]) * (self.total_road - self.passed_road[-2]) / math.hypot(temp_x - self.x[-2], temp_y - self.y[-2])
                self.y[-1] = self.y[-2] + (temp_y - self.y[-2]) * (self.total_road - self.passed_road[-2]) / math.hypot(temp_x - self.x[-2], temp_y - self.y[-2])
                loop_calculate = False
            #经过的路程恰好等于总路程
            if self.passed_road[-1] == self.total_road:
                loop_calculate = False
            #记录Poincare section的数据
            if self.y[-1] * self.y[-2] < 0:
                self.ps_vx.append(temp_vx)
                self.ps_x.append(self.x[-2] + (self.x[-1] - self.x[-2]) * (0 - self.y[-2]) / (self.y[-1] - self.y[-2]))
    #画碰撞轨迹图
    def show_result(self):
        pl.title('Trajectory of a billiard on a square table', fontsize=20)
        pl.xlabel('x', fontsize=20)
        pl.ylabel('y', fontsize=20)
        pl.xlim(-self.l, self.l)
        pl.ylim(-self.l, self.l)
        pl.plot(self.x, self.y)
        pl.plot(self.x[0], self.y[0], 'o')
        pl.show()
    #画Poincare section图
    def show_result_ps(self):
        pl.title('Poincare section $v_x$ versus x', fontsize=20)
        pl.xlabel('x', fontsize=20)
        pl.ylabel('$v_x$', fontsize=20)
        pl.xlim(-self.l, self.l)
        pl.plot(self.ps_x, self.ps_vx, '.')
        pl.show()

#num_str_in = input("请输入小球初始位置的横、纵坐标x、y，小球初始速度的横、纵分量vx、vy，半边长l，运动持续时间t的值,并用空格隔开:\n")
#num = [float(n) for n in num_str_in.split()]
#x = num[0]
#y = num[1]
#vx = num[2]
#vy = num[3]
#l = num[4]
#total_time = num[5]
#start = billiaro_collision_square(x, y, vx, vy, l, total_time)
#start.calculate()
#start.show_result()
#start.show_result_ps()

start = billiaro_collision_square()
start.calculate()
start.show_result()
start.show_result_ps()