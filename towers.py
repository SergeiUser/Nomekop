# File for containing the classes for all of the towers in the game
from pygame import draw as pygameDraw
from math import dist
from random import randint

typeColour = {
        "base" : (90, 90, 90),
        "arrow": (137, 81, 41),
        "fire" : (232, 97 ,0),
        "chain": (70, 130, 180)
}



class cursor:
        health = 1000
        def __init__(self, x,y):
                self.x = x
                self.y = y
                self.position = (x,y)

        def draw(self):
                pass

        def sim(self):
                print(f"Health: {self.health}")

class towerBase:
        range = 150
        cooldown = 500
        cooldownCounter = cooldown
        cooldownSpeed = 2.5
        drawLine = False
        type = "base"
        def __init__(self, surface, x=0, y=0, position=[], cellSize=[10,10]):
                self.surface = surface
                self.cellSize = cellSize
                if len(position) != 2:
                        self.position = (x, y)
                else:
                        self.position = tuple(position)
                self.drawX = self.position[0] * self.cellSize[0]
                self.drawY = self.position[1] * self.cellSize[1]

        def drawBase(self):
                self.drawX = self.position[0] * self.cellSize[0]
                self.drawY = self.position[1] * self.cellSize[1]
                pygameDraw.rect(self.surface, typeColour[self.type], (self.drawX, self.drawY, self.cellSize[0], self.cellSize[1]))



        def findClosestTarget(self, targets):
                position = ((self.position[0] * self.cellSize[0]) + self.cellSize[0]/2, (self.position[1] * self.cellSize[1]) + self.cellSize[1]/2)
                target = enemy(self.surface, position=position, health=10000000, speed=0)

                for t in targets:
                        if target.health > 100000:
                                target = t
                                self.drawLine = False
                        else:
                                self.drawLine = True
                                if dist(position, t.position) < dist(position, target.position):
                                        target = t
                targetPos = target.position
                if self.cooldownCounter < 50 and dist(targetPos, position) < self.range:
                        if target.health < 100000:
                                self.drawLine = True
                        if self.cooldownCounter < 0 and dist(targetPos, position) < self.range:
                                self.cooldownCounter = self.cooldown
                                target.health -= self.damage
                        else:
                                self.cooldownCounter -= self.cooldownSpeed
                else:
                        self.drawLine = False
                        self.cooldownCounter -= self.cooldownSpeed
                if self.drawLine:
                        pygameDraw.line(self.surface, "green", position, targetPos, 4)


class arrow(towerBase):
        type = "arrow"
        damage = 2

        def draw(self):
                self.drawBase()
                pygameDraw.polygon(self.surface, (255, 255, 255),(
                        (self.drawX + (self.cellSize[0]/2), self.drawY +5),
                        (self.drawX -5 + self.cellSize[0], self.drawY + (self.cellSize[1]/2)),
                        (self.drawX + (self.cellSize[0]/2), self.drawY + self.cellSize[1] -5),
                        (self.drawX +5, self.drawY + (self.cellSize[1]/2))
                ))
                pygameDraw.rect(self.surface, (55,55,55), (
                        self.drawX + (self.cellSize[0]/3), self.drawY + (self.cellSize[1]/3),
                        self.cellSize[0]/3, self.cellSize[0]/3
                        ))


class enemy:

        def __init__(self, surface, x=0, y=0, position=[], health=10, damage=5, speed=5, cellSize=[10,10]):
                self.surface = surface
                self.cellSize = cellSize
                self.health = health
                self.damage = damage
                self.speed = speed
                if len(position) != 2:
                        self.position = (x, y)
                else:
                        self.position = tuple(position)

                self.colour = (
                        randint(10, 255),
                        randint(10, 255),
                        randint(10, 255)
                )



        def draw(self):

                pygameDraw.circle(self.surface, self.colour, self.position, 5)

        def sim(self):
                self.position = ((self.position[0] + self.speed) % self.surface.get_width(), self.position[1])
                if self.health < 0:
                        self.colour = (0,0,0)

