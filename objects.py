import towers
from pygame import draw as pygameDraw

# Class for cursor
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

'''Combos
water + earth = mud (slow, splatter)
water + fire = steam (quick, smaller cone than fire, short range)
fire + earth = lava (DOT, splatter, lava pools)
fire + air = lighting (chain)
earth + air =
'''



applicableTowers = {
        "water": ["earth", "fire"],
        "earth": ["water",],
        "fire": ["water",],
        "air": []
}


class stone:
        def __init__(self, type):
                self.type = type


# Class for shop
class shop:
        items = [
        {
                "item": "airT",
                "position":(11.32, 3),
                "cost":50,
                "tower": towers.air
        },
        {
                "item": "waterT",
                "position":(12.32, 3),
                "cost":500,
                "tower": towers.water
        },
        {
                "item": "fireT",
                "position":(11.32, 4),
                "cost":125,
                "tower": towers.fire
        },
        {
                "item": "earthT",
                "position":(12.32, 4),
                "cost":150,
                "tower": towers.earth
        }
]
        money = 0

        def __init__(self, cellSize, display):
                self.display = display
                self.cellSize = cellSize

        def draw(self, money, texts):
                for item in self.items:
                        self.cellSizeAdjusted = (self.cellSize[0]*1.5,self.cellSize[1]*1.5)
                        position = item["position"]
                        tower = item["tower"](self.display,cellSize=self.cellSizeAdjusted, position=position)
                        tower.init()
                        if money < item["cost"]:
                                tower.type = "base"
                        tower.shopPiece = True
                        tower.draw()
                        del tower
                for text in texts:
                        self.display.blit(text[0], (text[1][0]*self.cellSize[0], text[1][1]*self.cellSize[1]))

        def click(self, mousePos):
                mouseCell = (
                        (mousePos[0] // self.cellSizeAdjusted[0]) + 0.32,
                        (mousePos[1] // self.cellSizeAdjusted[1])
                        )
                for item in self.items:
                        #pygameDraw.rect(self.display, "red", (mouseCell[0]*self.cellSizeAdjusted[0], mouseCell[1]*self.cellSizeAdjusted[1], self.cellSizeAdjusted[0], self.cellSizeAdjusted[1]))
                        '''if item["position"] == mouseCell:
                                print(item)
                                return item
                                '''

                        if mousePos[0] > self.cellSizeAdjusted[0] * item["position"][0] and mousePos[0] < self.cellSizeAdjusted[0] * (item["position"][0] + 1):
                                if mousePos[1] > self.cellSizeAdjusted[1] * item["position"][1] and mousePos[1] < self.cellSizeAdjusted[1] * (item["position"][1] + 1):
                                        return item
                return self.items[0]

class button:
        rotundness = 50
        def __init__(self, cellSize, display, command, position, dimensions:tuple, colour, font, text):
                self.display = display
                self.cellSize = cellSize
                self.position = position
                self.dimensions = dimensions
                self.colour = colour
                self.command = command
                self.font = font
                self.textArguments = text
                
        def init(self,mode):
                if mode == "START/QUIT":
                        self.text =[
                                self.font.render(self.textArguments[0],self.textArguments[1],self.textArguments[2]),
                                [self.position[0]+4/3, self.position[1]+1/4]
                        ]
                elif mode == "mapSelector":
                        self.text =[
                                self.font.render(self.textArguments[0],self.textArguments[1],self.textArguments[2]),
                                [self.position[0]+0.9, self.position[1]+0.75]
                        ]

        def draw(self):
                pygameDraw.rect(
                        self.display,
                        self.colour,
                        (self.position[0]*self.cellSize[0], self.position[1]*self.cellSize[1], self.dimensions[0]*self.cellSize[0], self.dimensions[1]*self.cellSize[1]),
                        0,
                        self.rotundness,self.rotundness,self.rotundness,self.rotundness
                        )
                self.display.blit(self.text[0], (self.text[1][0]*self.cellSize[0], self.text[1][1]*self.cellSize[1]))

        def click(self, mousePos):
                
                print(mousePos)
                if mousePos == self.position:
                        return self.command
                elif mousePos[0] >= self.position[0]*self.cellSize[0] and mousePos[0] <= (self.position[0] + self.dimensions[0])*self.cellSize[0]:
                        if mousePos[1] >= self.position[1]*self.cellSize[1] and mousePos[1] <= (self.position[1] + self.dimensions[1])*self.cellSize[1]:
                                return self.command
                else:
                        return print