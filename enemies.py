from random import randint, choice
from pygame import draw as pygameDraw
from math import dist
from paths import paths
import constants as const
class enemy:

        pathStage = 0
        state = "alive"
        def __init__(self, surface, x=0, y=0, position=[], health=10, damage=1, speed=1, cellSize=[10,10], reward = 10):
                self.surface = surface
                self.cellSize = cellSize
                self.health = health
                self.damage = damage
                self.speed = speed
                self.reward = reward
                self.level = 0

                self.path = choice(paths[const.map])



                x = 1 + (self.level * 0.25)
                print(x)
                self.size = 5 * x
                print(self.size)

                if len(position) != 2:
                        self.position = [
                                (self.path[0][0][0] * self.cellSize[0]),
                                (self.path[0][0][1] * self.cellSize[1]) + self.cellSize[1]/2,
                        ]
                else:
                        self.position = list(position)

                # Randomly chosen colour for enemy
                self.colour = (
                        randint(0, 55),
                        randint(150, 255),
                        randint(150, 255)
                )
        def init(self):
                self.speed = self.speed


        def sim(self):
                # Drawing of enemy
                pygameDraw.circle(self.surface, self.colour, tuple(self.position), self.size)

                # Movement of enemy
                #self.position[0] = (self.position[0] + self.speed) % self.surface.get_width()
                if self.health <= 0:
                        self.state = "killed"
                if self.state == "alive":
                        self.pathing()

        def pathing(self):
                if self.pathStage >= len(self.path):
                        self.state = "attacking"
                        return

                pathingNode = self.path[self.pathStage]
                pos = list(pathingNode[0])
                for i in range(len(self.cellSize)):
                        pos[i] = pos[i] * self.cellSize[i]
                        pos[i] = pos[i] + self.cellSize[i]/2
                speedModifier = pathingNode[1]


                if abs(self.position[0] - pos[0]) <= self.speed * speedModifier:
                        self.position[0] = pos[0]
                if abs(self.position[1] - pos[1]) <= self.speed * speedModifier:
                        self.position[1] = pos[1]

                if dist(tuple(self.position), pos) <= self.speed * speedModifier:
                        self.pathStage += 1#= (self.pathStage + 1) % (len(self.path))
                        return


                #direction Vector generation
                x = pos[0] - self.position[0]
                y = pos[1] - self.position[1]
                if x == 0:
                        xMove = 0
                        if y < 0:
                                slope = -1
                        else:
                                slope = 1
                else:
                        if x < 0:
                                xMove = -1
                        else:
                                xMove = 1
                        slope = y/abs(x)
                directionVector = (xMove,slope)



                for i in range(len(directionVector)):
                    self.position[i] += directionVector[i] * speedModifier * self.speed

                '''
                if self.pathStage == 4:
                        self.health = -10
                '''


class sergei(enemy):
        def init(self):
                self.level = 3
                self.speed *= 2
                self.colour = (
                        randint(150, 255),
                        randint(0, 55),
                        randint(0, 55)
                )
                x = 1 + (self.level * 0.25)
                print(x)
                self.size = 5 * x
                print(self.size)

        def explode(self):
                if self.health < 0:
                        print("bang")