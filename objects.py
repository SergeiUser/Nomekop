# Class for cursor
class cursor:
        health = 100
        def __init__(self, x,y):
                self.x = x
                self.y = y
                self.position = (x,y)

        def draw(self): #obselete, only used for targetting by towers
                pass

        def sim(self): #obselete, only used for targetting by towers
                print(f"Health: {self.health}")

import pygame as pygame

GRASS = 0
WATER = 1




textures = {
    GRASS : pygame.image.load("Nomekop/Assets/Grass And Road Tiles/Tiles/Grass0 - 0.png"),
    WATER : pygame.image.load("Nomekop/Assets/Grass And Road Tiles/Tiles/Water1.png")

    }


tilemap = [
    [GRASS, GRASS, GRASS, WATER],
    [GRASS, GRASS, WATER, GRASS],
    [GRASS, WATER, GRASS, GRASS],
    [WATER, GRASS, GRASS, GRASS]
    ]



tilesize = 64
mapwidth = 4
mapheight = 4

