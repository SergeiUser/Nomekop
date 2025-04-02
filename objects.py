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
                "position":(18, 4),
                "cost":100,
                "tower": towers.arrow
        },
        {
                "item": "waterT",
                "position":(19, 4),
                "cost":100,
                "tower": towers.arrow
        },
        {
                "item": "earthT",
                "position":(18, 5),
                "cost":100,
                "tower": towers.arrow
        },
        {
                "item": "airT",
                "position":(19, 5),
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
                        cellsize = (self.cellSize[0]*0.8,self.cellSize[1]*0.8)
                        position = item["position"]
                        tower = item["tower"](self.display,cellSize=cellsize, position=item["position"])
                        tower.draw()

        def click(self, mousePos):
                mouseCell = (
                        cursor.position[0] // self.cellSize[0],
                        cursor.position[1] // self.cellSize[1]
                        )
                for item in self.items:
                        if item["position"] == mouseCell:
                                return item

