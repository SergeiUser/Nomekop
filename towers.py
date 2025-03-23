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

# Base class for all towers
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
                # Initial Conversion of cell co-ordinates to screen co-ordinates
                self.drawX = self.position[0] * self.cellSize[0]
                self.drawY = self.position[1] * self.cellSize[1]

        def drawBase(self): #Defines drawing position on screen and draws base square
                # Repeating conversion of cell co-ordinates to screen co-ordinates for tower movement
                self.drawX = self.position[0] * self.cellSize[0]
                self.drawY = self.position[1] * self.cellSize[1]
                # Base square drawing
                pygameDraw.rect(self.surface, typeColour[self.type], (self.drawX + 5, self.drawY + 5, self.cellSize[0] - 10, self.cellSize[1] - 10))

        def drawCooldown(self, spiral=False): # Draws cooldown circle on the tower
                towerCooldownPercentage = ((self.cooldown - self.cooldownCounter)/self.cooldown)
                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), self.range, 2, False) # Outline circle to show range & limit of cooldown bar

                if not spiral:
                                # Standard Filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.range*towerCooldownPercentage), 0)

                else: # Spiral Filling
                        if towerCooldownPercentage < 0.25:
                                # Top Right Quadrant filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.range*towerCooldownPercentage*4), 0, True)
                        elif towerCooldownPercentage < 0.5:
                                # Bottom Right Quadrant filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.range), 0, True)
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.range*(towerCooldownPercentage-0.25)*4), 0, False, False, False, True)
                        elif towerCooldownPercentage < 0.75:
                                # Bottom Left Quadrant filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.range), 0, True, False, False, True)
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.range*(towerCooldownPercentage-0.5)*4), 0, False, False, True)
                        else:
                                # Top Left Quadrant filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.range), 0, True, False, True, True)
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.range*(towerCooldownPercentage-0.76)*4), 0, False, True)

        def findClosestTarget(self, targets):
                position = (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2)

                if self.cooldownCounter < -2: # Prevents cooldownCounter from going into the negatives & cooldown circle from growing exponentially
                        self.cooldownCounter = -2

                if len(targets) == 0: # Disables Tower attacking if no enemies
                        self.cooldownCounter -= self.cooldownSpeed
                        return

                for t in targets:
                        if t == targets[0]: # If t is first element then log it
                                target = t
                        else:
                                if dist(position, t.position) < dist(position, target.position):
                                        # If t is nearer to tower than logged target then log it
                                        target = t

                targetPos = target.position

                if self.cooldownCounter < 50 and dist(targetPos, position) < self.range: #Begins drawing line to target
                        self.drawLine = True

                if self.cooldownCounter < 0 and dist(targetPos, position) < self.range: # If off cooldown then attack & Reset cooldownCounter
                        self.cooldownCounter = self.cooldown
                        target.health -= self.damage

                else: # Ticks cooldownCounter down & Stops drawing line
                        self.cooldownCounter -= self.cooldownSpeed
                        self.drawLine = False


                if self.drawLine: #Draws line from tower to target if conditions are met
                        pygameDraw.line(self.surface, "red", position, targetPos, 10)


class arrow(towerBase):
        type = "arrow"
        damage = 2

        def draw(self):
                self.drawBase()
                # White Diamond vector drawing
                pygameDraw.polygon(self.surface, (255, 255, 255),(
                        (self.drawX + (self.cellSize[0]/2), self.drawY +5),
                        (self.drawX -5 + self.cellSize[0], self.drawY + (self.cellSize[1]/2)),
                        (self.drawX + (self.cellSize[0]/2), self.drawY + self.cellSize[1] -5),
                        (self.drawX +5, self.drawY + (self.cellSize[1]/2))
                ))

                # Small Black Square vector drawing
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

                # Randomly chosen colour for enemy
                self.colour = (
                        randint(10, 255),
                        randint(10, 255),
                        randint(10, 255)
                )



        def sim(self):
                # Drawing of enemy
                pygameDraw.circle(self.surface, self.colour, self.position, 5)

                # Movement of enemy
                self.position = ((self.position[0] + self.speed) % self.surface.get_width(), self.position[1])

