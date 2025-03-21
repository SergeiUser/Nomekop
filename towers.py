# File for containing the classes for all of the towers in the game
from pygame import draw as pygameDraw

typeColour = {
        "arrow": (137, 81, 41),
        "fire" : (232, 97 ,0),
        "chain": (70, 130, 180)
}





class towerBase:

        def __init__(self, type, x=0, y=0, position=[], cellSize=10):
                self.type = type





                if len(position) != 2:
                        self.position = [x, y]
                else:
                        self.position = position

        def drawBase(self, surface, ):
                drawX = self.position[0] * self.cellSize
                drawY = self.position[1] * self.cellSize
                pygameDraw.rect(surface, typeColour[self.type], (drawX, drawY, self.cellSize, self.cellSize))


class arrow(towerBase):
        pass