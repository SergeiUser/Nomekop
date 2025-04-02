import pygame, random
import tilemap, enemies, objects, towers

windowDimensions = (1440, 720)
gridSize = (20, 10)

cellSize = [windowDimensions[x]/gridSize[x] for x in range(len(gridSize))]
tilemapCellSize = tuple(cellSize)
print(cellSize)
pygame.init()


window = pygame.display.set_mode(windowDimensions)
seed = random.randint(100000, 999999)
enemy = enemies.enemy(window, speed=1, cellSize=cellSize)


tilemap.drawBackground(window, tilemapCellSize, seed)
shop = objects.shop(cellSize,window)
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
#tower = items[0]["tower"](window,cellSize=cellSize, position=items[0]["position"])
#tower.draw()
shop.draw()
run = True
while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
        enemy.sim()

        pygame.display.update()