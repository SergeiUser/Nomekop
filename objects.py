# Class for cuRHor
class cursor:
        health = 100
        def __init__(self, x,y):
                self.x = x
                self.y = y
                self.position = (x,y)

        def draw(self): #obselete, only used for targetting by toweRH
                pass

        def sim(self): #obselete, only used for targetting by toweRH
                print(f"Health: {self.health}")

import pygame
'''
N = 0
G = 1
Grasses = [
        pygame.image.load("Nomekop/Assets/Grass And Road Tiles/Tiles/Grass0 - 0.png"),
        pygame.image.load("Nomekop/Assets/Grass And Road Tiles/Tiles/Grass0 - 1.png"),
        pygame.image.load("Nomekop/Assets/Grass And Road Tiles/Tiles/Grass0 - 2.png"),
        pygame.image.load("Nomekop/Assets/Grass And Road Tiles/Tiles/Grass0 - 3.png"),
        pygame.image.load("Nomekop/Assets/Grass And Road Tiles/Tiles/Grass0 - 4.png"),
]
W = 2
RH = 3
RV = 4
RC = 5



textures = {
        N  : [pygame.surface.Surface((32,32))],
        G  : Grasses,
        W  : [pygame.image.load("Nomekop/Assets/Grass And Road Tiles/Tiles/Water1.png")],
        RH : [pygame.image.load("Nomekop/Assets/Grass And Road Tiles/Tiles/Road3 - 0.png")],
        RV : [pygame.image.load("Nomekop/Assets/Grass And Road Tiles/Tiles/Road1 - 1.png")],
        RC : [pygame.image.load("Nomekop/Assets/Grass And Road Tiles/Tiles/Road4.png")],

}

''''''[G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#20
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#19
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#18
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#17
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#16
    [RH,G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#15
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#14
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#13
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#12
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, W],#11'''
'''
tilemap = [
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#10
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#9
    [G, G, G, G, G, G, G, G, RV,G, G, G, G, G, G, G, G, G, G, G],#8
    [G, G, G, G, G, G, G, G, RV,G, G, G, G, G, G, G, G, G, G, G],#7
    [G, G, G, G, G, G, G, G, RV,G, G, G, G, G, G, G, G, G, G, G],#6
    [RH,RH,RH,RH,RH,RH,RH,RH,RC,G, G, G, G, G, G, G, G, G, G, G],#5
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#4
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#3
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G],#2
    [G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, G, W],#1
]



tilesize = 64
mapwidth = 4
mapheight = 4

'''