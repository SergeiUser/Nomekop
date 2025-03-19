import pygame, sys, random
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Nomekop!')
a=5
ay=0
enemyx = 0
enemyy = 450

looping = True


towerloc = (10000,10000)
while looping:
  

  enemyx +=a

  if enemyx == 800:
  	a=0
  	ay=5
  	enemyy -= ay


  if enemyy == 20:
  	ay = 0
  	enemyx=0
  	enemyy = 450
  	a = 5

  


  for event in pygame.event.get() :
    if event.type == QUIT :
      pygame.quit()
      sys.exit()
    if event.type == MOUSEBUTTONDOWN:
      towerloc=(pygame.mouse.get_pos())

  WINDOW.fill(BACKGROUND)

  pygame.draw.circle(WINDOW, (255,0,0), (enemyx,enemyy), 20)
  pygame.draw.circle(WINDOW, (0,155,0), (towerloc), 10)
  pygame.display.update()
  fpsClock.tick(FPS)

 


