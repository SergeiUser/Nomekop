import towers, enemies, objects, tilemap
import pygame, random

gravity = -2



windowDimensions = (1600, 800)
gridSize = (40, 20)

cellSize = [windowDimensions[x]/gridSize[x] for x in range(len(gridSize))]
tilemapCellSize = tuple(cellSize)
print(cellSize)
pygame.init()

window = pygame.display.set_mode(windowDimensions)
seed = random.randint(100000, 999999)

towersInScene = []

money = 0
health = 100

# Makes randomly placed towers
#towersInScene = [towers.arrow(window,position=[random.randint(0,gridSize[0]-1), random.randint(2,gridSize[1]-2)],cellSize=cellSize)for x in range(6)]

for x in range(len(towersInScene)):
        print(f"Tower {x} is: {type(towersInScene[x])}")

enemyTypes = [enemies.enemy,enemies.sergei]
# Generator for enemies
enemiesInScene = [random.choice(enemyTypes)(
        window,
        x = windowDimensions[0] * random.random(),
        y = (windowDimensions[1]/3) * random.random() + windowDimensions[1]/3,
        cellSize=cellSize,
        speed = random.uniform(1,2)
        ) for x in range(0, 10)]

for enemy in enemiesInScene:
        enemy.init()

#shop = objects.shop()
cursor = objects.cursor(0,0)
#enemies.append(cursor) # Makes cursor targettable by towers

run = True
while run:
        cursor.position = pygame.mouse.get_pos()
        pygame.time.delay(10)
        tilemap.drawBackground(window, tilemapCellSize, seed)
        #window.fill((30, 30, 120))

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                        #Cell that the mouse is in
                        print(money)
                        mouseCell = (
                                cursor.position[0] // cellSize[0],
                                cursor.position[1] // cellSize[1]
                        )
                        print(mouseCell)
                        if tilemap.tilemap[int(mouseCell[1])][int(mouseCell[0])] == 1:
                                if pygame.mouse.get_pressed()[0]: # Creates tower on left click
                                        towersInScene.append(towers.arrow(window, position=mouseCell, cellSize=cellSize))

                                elif pygame.mouse.get_pressed()[2]: # Deletes right clicked tower
                                        x = 0
                                        for tower in towersInScene: # Finds towers in the same cell as the mouse and deletes them
                                                if tower.position == mouseCell:
                                                        del towersInScene[x]
                                                else:
                                                        x += 1
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                        enemiesInScene.append(enemies.enemy(
                                        window,
                                        x = windowDimensions[0] * random.random(),
                                        y = (windowDimensions[1]/3) * random.random() + windowDimensions[1]/3,
                                        cellSize=cellSize,
                                        speed = random.randint(2,5)
                        ))

        for tower in towersInScene: #Draws cooldown circle for each tower
                tower.drawCooldown(False)
                # False: Fills whole circle at once as cooldownCounter decreases
                # True : Fills circle in by quadrant as cooldownCounter decreases


        for tower in towersInScene: # Draws each tower
                tower.draw()
        for tower in towersInScene: # Attacking logic for tower
                tower.findClosestTarget(enemiesInScene)

        x = 0
        for enemy in enemiesInScene: #Enemy Logic
                enemy.sim() # Draws enemy to screen & Moves enemy to right at it's speed

                if enemy.state != "alive":
                        if enemy.state == "killed":
                                money += enemy.reward
                        else:
                                health -= enemy.damage
                        del enemiesInScene[x]
                else:
                        x += 1

        pygame.display.update()
print(f"Enemy Count: {len(enemiesInScene)}")
x = 0
for enemy in enemiesInScene:
        x += 1
        print(f"Enemy {x} Pos: {tuple(enemy.position)}\nSpeed: {enemy.speed}")
