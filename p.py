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
	def __init__(self,m,x, y, vx,vy):
		self.m=m
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
		self.r=np.sqrt(x**2+y**2) 
		self.E= 0.5*m*((vx**2)+(vy**2))-GmS*m/self.r

		
	def a(self,p):
		r=np.sqrt(self.x**2+self.y**2)
		return -((GmS*m)/r**3)*p
				
	def movimento(self,):
		ax = self.a(self.x)
		self.x=self.x+self.vx*dt+0.5*ax*dt**2
		self.vx=self.vx+ax*dt
		ay=self.a(self.y)
		self.y=self.y+self.vy*dt+0.5*ay*dt**2
		self.vy=self.vy+ay*dt
		self.E=0.5*m*((self.vx**2)+(self.vy**2))-GmS*m/self.r
		
def wrap_angle(angle):
	return angle%360

terra=Planeta(1,1,0,0,2*np.pi)
pygame.init()
screen = pygame.display.set_mode((600,600))
myfont = pygame.font.Font(None,60)

space = pygame.image.load("space.png").convert()
sun = pygame.image.load("sun.png").convert_alpha()
planeta = pygame.image.load("planeta.png").convert_alpha()
sunw,sunh=sun.get_size()
pygame.display.set_caption("O Sol e a Terra")	

while True:
	for event in pygame.event.get():
		if event.type in (QUIT,KEYDOWN):
			sys.exit()
	planeta = pygame.transform.scale(planeta,(50,50))
	screen.blit(space, (0,0))
	screen.blit(sun, (300-sunw/2, 300-sunh/2))
	
	xant, yant=terra.x,terra.y
	terra.movimento()
	dx = terra.x - xant
	dy = terra.y - yant
	angulo=math.atan2(dy,dx)
	angulo=wrap_angle(-math.degrees(angulo)+90)
	dayplaneta = pygame.transform.rotate(planeta,angulo)
	
	screen.blit(dayplaneta,(terra.x*250+275,terra.y*250+275))
	pygame.display.update()
