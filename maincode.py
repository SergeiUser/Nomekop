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

enemyx = 800
enemyy = 450

looping = True

While looping:
  enemyx-=10


WINDOW.fill(BACKGROUND)

enemy = pygame.draw.circle(WINDOW, (255,0,0), (enemyx,enemyy), 20)
pygame.display.update()
  fpsClock.tick(FPS)


