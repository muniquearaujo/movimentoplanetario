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
		self.r1=np.sqrt((x-1)**2+y**2) 
		self.r2=np.sqrt((x+1)**2+y**2) 
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

terra=Planeta(1,0.1,1,0,0)
pygame.init()
screen = pygame.display.set_mode((600,600))
myfont = pygame.font.Font(None,60)

space = pygame.image.load("space.png").convert()
sun = pygame.image.load("sun.png").convert_alpha()
planeta = pygame.image.load("planeta.png").convert_alpha()
sun = pygame.transform.scale(sun,(50,50))
sunw,sunh=sun.get_size()
pygame.display.set_caption("Duas estrelas e um planeta")	

while True:
	for event in pygame.event.get():
		if event.type in (QUIT,KEYDOWN):
			sys.exit()
	planeta = pygame.transform.scale(planeta,(40,40))
	screen.blit(space, (0,0))
	screen.blit(sun, (25, 300-25))
	screen.blit(sun, (600-75, 300-25))
	
	xant, yant=terra.x,terra.y
	terra.movimento()
	dx = terra.x - xant
	dy = terra.y - yant
	angulo=math.atan2(dy,dx)
	angulo=wrap_angle(-math.degrees(angulo)+90)
	dayplaneta = pygame.transform.rotate(planeta,angulo)
	
	screen.blit(dayplaneta, (terra.x*(600-25)/2 + (600-25)/2, terra.y*(600-25)/2 + (600-25)/2))
	pygame.display.update()
