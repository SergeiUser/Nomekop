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
                "cost":150,
                "tower": towers.water
        },
        {
                "item": "fireT",
                "position":(11.32, 4),
                "cost":100,
                "tower": towers.fire
        },
        {
                "item": "earthT",
                "position":(12.32, 4),
                "cost":100,
                "tower": towers.earth
        }
]
        money = 0

        def __init__(self, cellSize, display):
                self.display = display
                self.cellSize = cellSize

        def draw(self, money):
                for item in self.items:
                        self.cellsize = (self.cellSize[0]*1.5,self.cellSize[1]*1.5)
                        position = item["position"]
                        tower = item["tower"](self.display,cellSize=self.cellsize, position=position)
                        tower.init()
                        if money < item["cost"]:
                                tower.type = "base"
                        tower.draw()
                        del tower

        def click(self, mousePos):
                mouseCell = (
                        (mousePos[0] // self.cellsize[0]) + 0.32,
                        (mousePos[1] // self.cellsize[1])
                        )
                print(mouseCell)
                for item in self.items:
                        pygameDraw.rect(self.display, "red", (mouseCell[0]*self.cellsize[0], mouseCell[1]*self.cellsize[1], self.cellsize[0], self.cellsize[1]))
                        '''if item["position"] == mouseCell:
                                print(item)
                                return item
                                '''
                        print(mousePos)
                        print(item["item"],self.cellsize[0] * (item["position"][0] -1))
                        print(item["item"],self.cellsize[0] * (item["position"][0]))
                        print(item["item"],self.cellsize[1] * (item["position"][1] -1))
                        print(item["item"],self.cellsize[1] * (item["position"][1]))

                        if mousePos[0] > self.cellsize[0] * item["position"][0] and mousePos[0] < self.cellsize[0] * (item["position"][0] + 1):
                                if mousePos[1] > self.cellsize[1] * item["position"][1] and mousePos[1] < self.cellsize[1] * (item["position"][1] + 1):
                                        print(item)
                                        return item
                return self.items[0]

