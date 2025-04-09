# File for containing the classes for all of the towers in the game
from pygame import draw as pygameDraw
from math import dist
from random import randint

typeColour = {
        "base" : (90,  90, 90),
        "earth": (137, 81, 41),
        "water": (0,   97, 232),
        "air"  : (230, 230, 230),
        "fire" : (232, 97, 0)
}

typeCost = {
        "earth": 100,
        "water": 150,
        "fire": 150,
        "air": 150,
}

levelColours=[
        (55,55,55),
        (55,155,55)
]


# Base class for all towers
class towerBase:
        selected = False
        initialised = False
        range = 1.5
        cooldown = 200
        cooldownCounter = cooldown
        cooldownSpeed = 2.5
        drawLine = False
        type = "base"
        level = 0


        def __init__(self, surface, x=0, y=0, position=[], cellSize=[10,10], type="base"):
                self.surface = surface
                self.type = type
                self.cellSize = cellSize
                if len(position) != 2:
                        self.position = (x, y)
                else:
                        self.position = tuple(position)
                # Initial Conversion of cell co-ordinates to screen co-ordinates
                self.drawX = self.position[0] * self.cellSize[0]
                self.drawY = self.position[1] * self.cellSize[1]
        def init(self):
                pass
        def drawBase(self): #Defines drawing position on screen and draws base square

                # Repeating conversion of cell co-ordinates to screen co-ordinates for tower movement
                self.drawX = self.position[0] * self.cellSize[0]
                self.drawY = self.position[1] * self.cellSize[1]
                if self.selected:
                        pygameDraw.rect(self.surface, "green", (self.drawX, self.drawY, self.cellSize[0], self.cellSize[1]))
                # Base square drawing
                pygameDraw.rect(self.surface, typeColour[self.type], (self.drawX + 5, self.drawY + 5, self.cellSize[0] - 10, self.cellSize[1] - 10))

        def drawCooldown(self, spiral=True): # Draws cooldown circle on the tower
                towerCooldownPercentage = ((self.cooldown - self.cooldownCounter)/self.cooldown)
                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), self.range * ((self.cellSize[0]+self.cellSize[0])/2), 2, False) # Outline circle to show range & limit of cooldown bar
                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), self.cellSize[0], 2, False) # Outline circle to show range & limit of cooldown bar

                if not spiral:
                                # Standard Filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]*towerCooldownPercentage), 0)

                else: # Spiral Filling
                        if towerCooldownPercentage > 0.99:
                                towerCooldownPercentage == 1
                        if towerCooldownPercentage < 0.25:
                                # Top Right Quadrant filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]*towerCooldownPercentage*4), 0, True)
                        elif towerCooldownPercentage < 0.5:
                                # Bottom Right Quadrant filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]), 0, True)
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]*(towerCooldownPercentage-0.25)*4), 0, False, False, False, True)
                        elif towerCooldownPercentage < 0.75:
                                # Bottom Left Quadrant filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]), 0, True, False, False, True)
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]*(towerCooldownPercentage-0.5)*4), 0, False, False, True)
                        else:
                                # Top Left Quadrant filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]), 0, True, False, True, True)
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]*(towerCooldownPercentage-0.85)*4), 0, False, True)

        def subDraw(self):
                pass

        def findClosestTarget(self, targets):
                position = (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2)

                if self.cooldownCounter < -2: # Prevents cooldownCounter from going into the negatives & cooldown circle from growing exponentially
                        self.cooldownCounter = 0

                if len(targets) == 0: # Disables Tower attacking if no enemies
                        self.cooldownCounter -= self.cooldownSpeed
                        return

                for t in targets:
                        if t == targets[0]: # If t is first element then log it
                                self.target = t
                        else:
                                if dist(position, t.position) < dist(position, self.target.position):
                                        # If t is nearer to tower than logged self.target then log it
                                        self.target = t

                targetPos = self.target.position

                if self.cooldownCounter < 50 and dist(targetPos, position) < self.range * ((self.cellSize[0]+self.cellSize[1])/2) * 1.25: #Begins drawing line to self.target
                        self.drawLine = True
                        self.cooldownCounter -= self.cooldownSpeed

                if self.cooldownCounter < 0 and dist(targetPos, position) < self.range * ((self.cellSize[0]+self.cellSize[1])/2) and self.drawLine: # If off cooldown then attack & Reset cooldownCounter
                        self.cooldownCounter = self.cooldown
                        self.target.health -= self.damage

                else: # Ticks cooldownCounter down & Stops drawing line
                        self.cooldownCounter -= self.cooldownSpeed
                        self.drawLine = False


                if self.drawLine: #Draws line from tower to self.target if conditions are met
                        pygameDraw.line(self.surface, "red", position, targetPos, 10)
                        pygameDraw.circle(self.surface, "red", ((self.position[0] * self.cellSize[0]) + self.cellSize[0]/2, (self.position[1] * self.cellSize[1])+ self.cellSize[1]/2), 5)


class arrow(towerBase):


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
                        self.cellSize[0]/3, self.cellSize[1]/3
                        ))
                self.subDraw()

class water(arrow):
        def init(self):
                self.type = "water"
                self.cooldownSpeed = 8
                self.damage = 2

class earth(arrow):
        def init(self):
                self.type = "earth"
                self.damage = 10
                self.cooldownSpeed = 1

class air(arrow):
        def init(self):
                self.type = "air"
                self.damage = 5
class fire(arrow):
        def init(self):
                self.type = "fire"
                self.damage = 4
                self.cooldownSpeed = 2
