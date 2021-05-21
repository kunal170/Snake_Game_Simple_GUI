import pygame, sys, os
from pygame.locals import *

pygame.init()

DISPLAYSURF=pygame.display.set_mode((1000,600),0,32)
pygame.display.set_caption('Drawing')

BLACK=[0,0,0]
WHITE=[255,255,255]
RED=[255,0,0]
GREEN=[0,255,0]
BLUE=[0,0,255]

DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF,GREEN,((146,200),(191,106),(236,200),(236,300),(146,300)))
pygame.draw.line(DISPLAYSURF,BLUE,(60,60),(120,60),4)
pygame.draw.line(DISPLAYSURF,BLUE,(120,60),(60,120))
pygame.draw.line(DISPLAYSURF,BLUE,(60,120),(120,120),4)
pygame.draw.circle(DISPLAYSURF,BLUE,(300,50),20,0)
pygame.draw.ellipse(DISPLAYSURF,RED,(300,200,40,80),1)
pygame.draw.rect(DISPLAYSURF,RED,(200,150,100,50))

pixObj=pygame.PixelArray(DISPLAYSURF)
pixObj[380][280]=BLACK
pixObj[382][282]=BLACK
pixObj[384][284]=BLACK
pixObj[386][286]=BLACK
pixObj[388][288]=BLACK
del pixObj

while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()

pygame.display.update()
	
