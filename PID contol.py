import turtle
import math as m
import matplotlib.pyplot as plt

mass=0.949
force= 11
g=-9.8
A_angle = 70 #Actual angle of rocket
E_angle = 0 #Error in agle
R_angle = 90 # Angle required
T_angle = 0 
i=0
t=0.001
#kp=0.06
#ki=11.939
#kd=0.000075378

kp=0.054
ki=10.2859
kd=0.00007086

#kp=0.3
#ki=15.66
#kd=0.0001483485
L=0.62

axl=(force/mass)+g
print(axl)
Y=[]
X=[]
Y1=[]
X1=[]
Y2=[]
X2=[]
kpy=[]
kiy=[]
kdy=[]
class start(object):
    def __init__ (self):
        self.Rocket = turtle.Turtle()
        self.Rocket.shape('square')
        self.Rocket.color('black')
        self.Rocket.penup()
        self.Rocket.goto(60,90)
        self.Rocket.speed(0)
        self.marker = turtle.Turtle()
        self.marker.penup()
        self.marker.left(0)
        self.marker.goto(15,90)
        self.marker.color('red')

        self.Ag=A_angle
        self.Eg=E_angle
        self.Rg=R_angle
        self.G=g
        self._mass=mass
        self._force=force
        self.KP=kp
        self.KI=ki
        self.KD=kd
        self.kperr=0
        self.kierr=0
        self.kderr=0
        self.EGL=0
        self.dt=t
        self.Length=L
        self.time=0
        self.teta=0
        self._Tangle=T_angle
        self.marker.sety(self.Ag)
        self.I=0
    def PID(self):
        self.Eg = ( self.Rg - self.Ag )
        self.kperr = (self.KP * self.Eg)
        self.kierr = self.kierr+(self.KI * self.Eg * self.dt)
        self.kderr = (self.KD * ((self.Eg-self.EGL)/self.dt))
        self.EGL = self.Eg
        self.piderr = self.kperr + self.kperr + self.kderr
        kpy.append(self.kperr)

        kiy.append(self.kierr)
        kdy.append(self.kderr)
        if self.piderr<=30:
            self._Tangle=self.piderr
        else:
            self._Tangle=30
            
        if self.piderr<= -30:
            self._Tangle=self.piderr
        else:
            self._Tangle=-30
        
        Y1.append(self._Tangle)
        X1.append(self.I)
        Y2.append(self.Eg)
        X2.append(self.I)
        self.I = self.I+1
        print(self.Eg)
        return self._Tangle
    
    def trust(self):
        self.time+=self.dt
        if(self._Tangle!=90):
            self.teta = self.teta + ((6 * self._force * m.cos(m.radians(90-self.piderr))) / (self._mass * self.Length))
        self.Ag= self.Ag + (self.teta)
        
        self.marker.sety(self.Ag)
        Y.append(self.Ag)
        X.append(self.time)
        
        
    def plotG(self):
        plt.plot(X,Y)
        plt.show()

    def plotG1(self):
        fig, axs = plt.subplots(2)
        fig.suptitle('angle and pid')
        axs[0].plot(X2,Y2)
        axs[1].plot(X1,Y1)
        plt.show()

    def plotG2(self):
        fig, axe = plt.subplots(3)
        fig.suptitle('KP,KI,KD')
        axe[0].plot(X,kpy)
        axe[1].plot(X,kiy)
        axe[2].plot(X,kdy)
        plt.show()
def main():
    d = start()
    for i in range(0,200):
        d.PID()
        d.trust()
    turtle.done()
    d.plotG()
    d.plotG1()
    d.plotG2()
main()
