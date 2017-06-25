import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt 
import pygame
import sys
from pygame.locals import *

m=1
G=6.67*10**(-11)
AU=1
GmS=4*math.pi**2
dt=0.001

class Planeta:
	def __init__(self,m,x, y, vx,vy,x2,y2,x3,y3):
		self.m=m
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.r1=np.sqrt((x-x2)**2+(y-y2)**2) 
		self.r2=np.sqrt((x+x2)**2+(y-y3)**2) 
		self.E= 0.5*m*((vx**2)+(vy**2))-(GmS*m/self.r1 + GmS*m/self.r2)

		
	def a(self,p):
		return -((GmS*m)/self.r1**3+(GmS*m)/self.r2**3)*p
				
	def movimento(self,):
		ax = self.a(self.x)
		self.x=self.x+self.vx*dt+0.5*ax*dt**2
		self.vx=self.vx+ax*dt
		ay=self.a(self.y)
		self.y=self.y+self.vy*dt+0.5*ay*dt**2
		self.vy=self.vy+ay*dt
		self.E=0.5*m*((self.vx**2)+(self.vy**2))-(GmS*m/self.r1+GmS*m/self.r2)
		
def wrap_angle(angle):
	return angle%360

p1=Planeta(1,1,0,0,0,0,np.sqrt(3),-1,0)
p2=Planeta(1,0,np.sqrt(5),0,0,1,0,-1,0)
p3=Planeta(1,-1,0,0,0,np.sqrt(3),0,1,0)

pygame.init()
screen = pygame.display.set_mode((600,600))
myfont = pygame.font.Font(None,60)

space = pygame.image.load("space.png").convert()
sun = pygame.image.load("sun.png").convert_alpha()
planeta = pygame.image.load("planeta.png").convert_alpha()
sun = pygame.transform.scale(sun,(100,100))

sunw,sunh=sun.get_size()
pygame.display.set_caption("3 planetas equidistantes")	

while True:
	for event in pygame.event.get():
		if event.type in (QUIT,KEYDOWN):
			sys.exit()
	planeta = pygame.transform.scale(planeta,(40,40))
	screen.blit(space, (0,0))
	
	p1.movimento()
	p2.movimento()
	p3.movimento()
	
	screen.blit(planeta, (p1.x*(600-20)/2 + (600-20)/2, p1.y*(600-20)/2 + (600-20)/2))
	screen.blit(planeta, (p2.x*(600-20)/2 + (600-20)/2, p2.y*(600-20)/2 + (600-20)/2))
	screen.blit(planeta, (p3.x*(600-20)/2 + (600-20)/2, p3.y*(600-20)/2 + (600-20)/2))
	pygame.display.update()
