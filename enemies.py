from random import randint
from pygame import draw as pygameDraw
from math import dist
class enemy:
        path = [
                ((0,   300), 1),
                ((450, 450), 1),
                ((750, 450), 1),
                ((750, 150), 1),
                ((600, 100), 1),
                ((1000,300), 1)

        ]
        pathStage = 0
        state = "alive"
        def __init__(self, surface, x=0, y=0, position=[], health=10, damage=1, speed=1, cellSize=[10,10], reward = 10):
                self.surface = surface
                self.cellSize = cellSize
                self.health = health
                self.damage = damage
                self.speed = speed
                self.reward = reward
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
                if self.health <= 0:
                        self.state = "killed"
                if self.state == "alive":
                        self.pathing()

        def pathing(self):
                if self.pathStage >= len(self.path):
                        self.state = "attacking"
                        return

                pathingNode = self.path[self.pathStage]
                pos = pathingNode[0]
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