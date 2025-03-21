import pygame, sys, random
pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 910

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Nomekop!')
a=5
ay=0
enemyX = 0
enemyY = 450

looping = True


towerPosition = (10000,10000)
while looping:
    enemyX +=a

    if enemyX == 800:
        a=0
        ay=5
        enemyY -= ay


    if enemyY == 20:
        ay = 0
        enemyX=0
        enemyY = 450
        a = 5


    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            towerPosition=(pygame.mouse.get_pos())

    WINDOW.fill(BACKGROUND)

    pygame.draw.circle(WINDOW, (255,0,0), (enemyX,enemyY), 20)
    pygame.draw.circle(WINDOW, (0,155,0), (towerPosition), 10)
    pygame.display.update()
    fpsClock.tick(FPS)