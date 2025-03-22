import towers
import pygame, random

windowDimensions = (1080, 605)
gridSize = (16, 9)

cellSize = [windowDimensions[x]/gridSize[x] for x in range(len(gridSize))]
print(cellSize)
pygame.init()

window = pygame.display.set_mode(windowDimensions)

#tower = towers.arrow(window, position=[8, 0], cellSize=cellSize)
towersInScene = [
        towers.arrow(
                window,
                position=[random.randint(0,gridSize[0]-1), random.randint(2,gridSize[1]-2)],
                cellSize=cellSize)
                for x in range(6)]

for x in range(len(towersInScene)):
        print(f"Tower {x} is: {type(towersInScene[x])}")
cursor = towers.cursor(0,0)

enemies = [towers.enemy(
        window,
        x = windowDimensions[0] * random.random(),
        y = (windowDimensions[1]/3) * random.random() + windowDimensions[1]/3,
        cellSize=cellSize,
        speed = random.uniform(3,6)
        ) for x in range(6)]
enemies.append(cursor)
run = True
while run:
        cursor.position = pygame.mouse.get_pos()
        window.fill("darkblue")
        pygame.time.delay(5)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        #tower.position[0] = (tower.position[0] + 1) % (gridSize[0] + 2)

        for tower in towersInScene:
                pygame.draw.circle(tower.surface, "darkgreen", (tower.drawX + tower.cellSize[0]/2, tower.drawY + tower.cellSize[1]/2), tower.range)
        for tower in towersInScene:
                tower.draw()
                tower.findClosestTarget(enemies)

        x = 0
        for enemy in enemies:
                enemy.draw()
                enemy.sim()
                if enemy.health < 0:
                        del enemies[x]
                else:
                        x += 1
        pygame.display.update()
