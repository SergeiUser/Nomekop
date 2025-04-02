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
                "item": "fireT",
                "position":(11.32, 4),
                "cost":100,
                "tower": towers.arrow
        },
        {
                "item": "waterT",
                "position":(12.32, 4),
                "cost":150,
                "tower": towers.quickArrow
        },
        {
                "item": "earthT",
                "position":(18, 5),
                "cost":100,
                "tower": towers.arrow
        },
        {
                "item": "airT",
                "position":(20, 5),
                "cost":100,
                "tower": towers.arrow
        }
]
        money = 0

        def __init__(self, cellSize, display):
                self.display = display
                self.cellSize = cellSize

        def draw(self):
                for item in self.items:
                        self.cellsize = (self.cellSize[0]*1.5,self.cellSize[1]*1.5)
                        position = item["position"]
                        tower = item["tower"](self.display,cellSize=self.cellsize, position=position)
                        tower.init()
                        tower.draw()

        def click(self, mousePos):
                mouseCell = (
                        (mousePos[0] // self.cellsize[0]) + 0.32,
                        (mousePos[1] // self.cellsize[1])
                        )
                print(mouseCell)
                for item in self.items:
                        tempItem = item
                        print(tempItem)
                        if item["position"] == mouseCell:
                                print(tempItem)
                                return tempItem
                return self.items[0]

