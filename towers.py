# File for containing the classes for all of the towers in the game
from pygame import draw as pygameDraw
import math
from random import randint

typeColour = {
        "base" : (90,  90, 90),
        "earth": (137, 81, 41),
        "water": (0,   97, 232),
        "air"  : (230, 230, 230),
        "fire" : (232, 97, 0)
}

typeCost = {
        "earth": 150,
        "water": 500,
        "fire": 125,
        "air": 50,
}

levelColours=[
        (55,55,55),
        (55,155,55)
]


# Base class for all towers
class towerBase:
        shopPiece = False
        selected = False
        initialised = False
        range = 1.5
        cooldown = 200
        cooldownCounter = cooldown
        cooldownSpeed = 2.5
        towerCooldownPercentage = 0
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
                self.towerCooldownPercentage = ((self.cooldown - self.cooldownCounter)/self.cooldown)

                # Repeating conversion of cell co-ordinates to screen co-ordinates for tower movement
                self.drawX = self.position[0] * self.cellSize[0]
                self.drawY = self.position[1] * self.cellSize[1]
                if self.selected:
                        pygameDraw.rect(self.surface, "green", (self.drawX, self.drawY, self.cellSize[0], self.cellSize[1]))
                # Base square drawing
                pygameDraw.rect(self.surface, typeColour[self.type], (self.drawX + 5, self.drawY + 5, self.cellSize[0] - 10, self.cellSize[1] - 10))
                if not self.shopPiece:
                        pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), self.range * ((self.cellSize[0]+self.cellSize[0])/2), 2, False) # Outline circle to show range & limit of cooldown bar

        def drawCooldown(self, spiral=True): # Draws cooldown circle on the tower
                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), self.cellSize[0], 2, False) # Outline circle to show range & limit of cooldown bar

                if spiral:
                        # Standard Filling
                        pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]*self.towerCooldownPercentage), 0)
                if False: # Spiral Filling
                        if self.towerCooldownPercentage > 0.99:
                                self.towerCooldownPercentage == 1
                        if self.towerCooldownPercentage < 0.25:
                                # Top Right Quadrant filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]*self.towerCooldownPercentage*4), 0, True)
                        elif self.towerCooldownPercentage < 0.5:
                                # Bottom Right Quadrant filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]), 0, True)
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]*(self.towerCooldownPercentage-0.25)*4), 0, False, False, False, True)
                        elif self.towerCooldownPercentage < 0.75:
                                # Bottom Left Quadrant filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]), 0, True, False, False, True)
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]*(self.towerCooldownPercentage-0.5)*4), 0, False, False, True)
                        else:
                                # Top Left Quadrant filling
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]), 0, True, False, True, True)
                                pygameDraw.circle(self.surface, "darkgreen", (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2), int(self.cellSize[0]*(self.towerCooldownPercentage-0.85)*4), 0, False, True)

        def subDraw(self):
                if not self.shopPiece:
                        pygameDraw.rect(self.surface, (105,105,105), (
                                self.drawX + (self.cellSize[0]/3), self.drawY + (self.cellSize[1]*(4/9)),
                                (self.cellSize[0]/3), self.cellSize[1]/9
                                ))
                        pygameDraw.rect(self.surface, (25,155,25), (
                                self.drawX + (self.cellSize[0]/3), self.drawY + (self.cellSize[1]*(4/9)),
                                ((self.cellSize[0]/3)*self.towerCooldownPercentage)-1, self.cellSize[1]/9
                                ))
        def findClosestTarget(self, targets):
                self.targets = targets
                position = (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2)

                if self.cooldownCounter < -2: # Prevents cooldownCounter from going into the negatives & cooldown circle from growing exponentially
                        self.cooldownCounter = 0
                else:
                        self.cooldownCounter -= self.cooldownSpeed

                if len(targets) == 0: # Disables Tower attacking if no enemies
                        self.cooldownCounter -= self.cooldownSpeed
                        return
                if self.cooldownCounter < 60:
                        for t in targets:
                                if t == targets[0]: # If t is first element then log it
                                        self.target = t
                                else:
                                        if math.dist(position, t.position) < math.dist(position, self.target.position):
                                                # If t is nearer to tower than logged self.target then log it
                                                self.target = t

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
        def attack(self):
                position = (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2)
                targetPos = self.target.position
                if self.cooldownCounter < 50 and math.dist(targetPos, position) < self.range * ((self.cellSize[0]+self.cellSize[1])/2) * 1.25: #Begins drawing line to self.target
                        self.drawLine = True
                        self.cooldownCounter -= self.cooldownSpeed

                if self.cooldownCounter < 0 and math.dist(targetPos, position) < self.range * ((self.cellSize[0]+self.cellSize[1])/2) and self.drawLine: # If off cooldown then attack & Reset cooldownCounter
                        self.cooldownCounter = self.cooldown
                        self.target.health -= self.damage

                else: # Ticks cooldownCounter down & Stops drawing line
                        self.cooldownCounter -= self.cooldownSpeed
                        self.drawLine = False


                if self.drawLine: #Draws line from tower to self.target if conditions are met
                        pygameDraw.line(self.surface, "red", position, targetPos, 10)
                        pygameDraw.circle(self.surface, "red", ((self.position[0] * self.cellSize[0]) + self.cellSize[0]/2, (self.position[1] * self.cellSize[1])+ self.cellSize[1]/2), 5)


class water(arrow):
        def init(self):
                self.type = "water"
                self.cooldownSpeed = 8
                self.damage = 2

class earth(arrow):
        def init(self):
                self.type = "earth"
                self.damage = 10
                self.cooldownSpeed = 2

class air(arrow):
        def init(self):
                self.type = "air"
                self.damage = 3
class fire(arrow):
        angleOfAttack = 30
        angle = 50
        def init(self):
                self.type = "fire"
                self.damage = 4
                self.cooldownSpeed = 2
        def attack(self):
                if self.cooldownCounter > 50:
                        return
                position = (self.drawX + self.cellSize[0]/2, self.drawY + self.cellSize[1]/2)
                targetPos = self.target.position

                cone = [position]

                width = math.cos(math.radians(90-self.angleOfAttack + self.angle)) * self.range * self.cellSize[0]
                height = math.sin(math.radians(90-self.angleOfAttack + self.angle)) * self.range * self.cellSize[1]
                x = position[0] + width
                y = position[1] + height
                cone.append((x,y))

                width = math.cos(math.radians(90+self.angleOfAttack + self.angle)) * self.range * self.cellSize[0]
                height = math.sin(math.radians(90+self.angleOfAttack) + self.angle) * self.range * self.cellSize[1]
                x = position[0] + width
                y = position[1] + height
                cone.append((x,y))



                if self.cooldownCounter < 50 and math.dist(targetPos, position) < self.range * ((self.cellSize[0]+self.cellSize[1])/2) * 1.25: #Begins drawing line to self.target
                        self.drawLine = True

                if self.cooldownCounter < 0 and math.dist(targetPos, position) < self.range * ((self.cellSize[0]+self.cellSize[1])/2) and self.drawLine: # If off cooldown then attack & Reset cooldownCounter
                        self.cooldownCounter = self.cooldown
                        hits = [self.target]
                        for target in self.targets:
                                if math.dist(targetPos, position) < self.range and target != self.target:
                                        c1 = (cone[1][0] - position[0]) * (target.position[1] - position[1]) - (cone[1][0] - position[1]) * (target.position[0] - position[0])
                                        c2 = (cone[2][0] - cone[1][0]) * (target.position[1] - cone[1][1]) - (cone[1][0] - cone[1][0]) * (target.position[0] - cone[1][0])
                                        c3 = (position[0] - cone[2][0]) * (target.position[1] - cone[2][1]) - (position[1] - cone[1][0]) * (target.position[0] - cone[2][0])

                                        if (c1 < 0 and c2 < 0 and c3 < 0) or (c1 > 0 and c2 > 0 and c3 > 0):
                                                hits.append(target)

                        for target in hits:
                                target.health -= self.damage

                else: # Ticks cooldownCounter down & Stops drawing line
                        self.drawLine = False
                self.drawLine = True

                pygameDraw.polygon(self.surface, (200, 100, 10), tuple(cone))
                print(cone)

                if self.drawLine: #Draws line from tower to self.target if conditions are met
                        pygameDraw.polygon(self.surface, (200, 100, 10), tuple(cone))