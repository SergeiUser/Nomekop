from random import randint
from pygame import draw as pygameDraw
from math import dist
class enemy:
        path = [
                ((0,   300), 0, (0, 0)),
                ((450, 450), 1, (3, 1)),
                ((750, 450), 1, (3, 0)),
                ((750, 150), 5, (0, -2)),
                ((600, 100), 1, (-3,-1)),
                ((0,   300), 2, (-3, 1))

        ]
        pathStage = 0
        def __init__(self, surface, x=0, y=0, position=[], health=10, damage=5, speed=1, cellSize=[10,10]):
                self.surface = surface
                self.cellSize = cellSize
                self.health = health
                self.damage = damage
                self.speed = speed
                if len(position) != 2:
                        self.position = [x,y]
                else:
                        self.position = list(position)

                # Randomly chosen colour for enemy
                self.colour = (
                        randint(50, 255),
                        randint(50, 255),
                        randint(50, 255)
                )



        def sim(self):
                # Drawing of enemy
                pygameDraw.circle(self.surface, self.colour, tuple(self.position), 5)

                # Movement of enemy
                #self.position[0] = (self.position[0] + self.speed) % self.surface.get_width()
                self.pathing()

        def pathing(self):
                pathingNode = self.path[self.pathStage]
                pos = pathingNode[0]
                speedModifier = pathingNode[1]
                directionVector = pathingNode[2]

                if self.pathStage == 0:
                        self.pathStage = 1
                        self.position = list(pos)
                        return


                if self.position == list(pos):
                            self.pathStage = (self.pathStage + 1) % (len(self.path))
                            pos = self.path[self.pathStage][0]
                            speedModifier = self.path[self.pathStage][1]
                            directionVector = self.path[self.pathStage][2]

                if self.pathStage > len(self.path):
                        self.attack()

                for i in range(len(directionVector)):
                    self.position[i] += directionVector[i] * speedModifier * self.speed