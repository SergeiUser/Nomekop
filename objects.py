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


# Class for shop
class shop:



        def __init__(self, ):
                pass