import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt 


mT=1
G=6.67*10**(-11)
AU=1
GmS=4*math.pi**2
dt=0.0001

class Planeta:
	def __init__(self,x, y, vx,vy):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.r=np.sqrt(x**2+y**2) 
		self.E= 0.5*mT*((vx**2)+(vy**2))-GmS*mT/self.r

		
	def a(self,p):
		r=np.sqrt(self.x**2+self.y**2)
		return -((GmS*mT)/r**3)*p
				
	def movimento(self,t):
		ax = self.a(self.x)
		self.x=self.x+self.vx*dt+0.5*ax*dt**2
		self.vx=self.vx+ax*dt
		ay=self.a(self.y)
		self.y=self.y+self.vy*dt+0.5*ay*dt**2
		self.vy=self.vy+ay*dt
		self.E=0.5*mT*((self.vx**2)+(self.vy**2))-GmS*mT/self.r

p1=Planeta(1.,0.,0.,2*math.pi+1.0)



tmax=4
t=np.arange(0, tmax, dt)

x=np.zeros(t.size)
y=np.zeros(t.size)
vx=np.zeros(t.size)
		
for i in range(t.size):
	p1.movimento(t[i])
	x[i]=p1.x
	y[i]=p1.y
	vx[i]=p1.vx
	
plt.figure(figsize=(6,5), dpi=96)
ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()

plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.title(r'Planeta', fontsize=12)

plt.grid()
plt.plot(x,y,'g-', linewidth=2 )

plt.legend(loc='upper right')
plt.axes().set_aspect('equal','datalim')
plt.savefig("1.pdf", dpi=96)

plt.show()				
		
		
