import towers, enemies, objects, tilemap
import pygame, random


gravity = -2

gameTimer = 0
gameDelay = 10


windowDimensions = (1460, 730)
gridSize = (20, 10)

cellSize = [windowDimensions[x]/gridSize[x] for x in range(len(gridSize))]
tilemapCellSize = tuple(cellSize)
print(cellSize)
pygame.init()
pygame.font.init()
window = pygame.display.set_mode(windowDimensions)
seed = random.randint(100000, 999999)

towersInScene = []
selectedTower ={
        "item": "airT",
        "position":(11.32, 3),
        "cost":50,
        "tower": towers.air
}
font = pygame.font.SysFont("Helvetica", int(cellSize[1]/2))

levels = [500, 1250, 2000, 3000, 5000]

money = 275
health = 100
points = 0
level = 1

# Makes randomly placed towers
#towersInScene = [towers.arrow(window,position=[random.randint(0,gridSize[0]-1), random.randint(2,gridSize[1]-2)],cellSize=cellSize)for x in range(6)]

for x in range(len(towersInScene)):
        print(f"Tower {x} is: {type(towersInScene[x])}")

enemyTypes = [enemies.enemy, enemies.sergei]
# Generator for enemies
enemiesInScene = [enemyTypes[0](
        window,
        x = windowDimensions[0] * random.random(),
        y = (windowDimensions[1]/3) * random.random() + windowDimensions[1]/3,
        cellSize=cellSize,
        speed = (random.uniform(1,2)*(63/cellSize[0]))
        ) for x in range(5)]

for enemy in enemiesInScene:
        enemy.init()

shop = objects.shop(cellSize,window)
cursor = objects.cursor(0,0)
#enemies.append(cursor) # Makes cursor targettable by towers
shop.draw(money, [])

run = True
while run:
        if points > levels[level-1]:
                level += 1
        spawnEnemy = False
        spawnedEnemies = []
        if level == 1:
                if gameTimer/gameDelay % (gameDelay * 10) == 0:
                        spawnEnemy = True
                        e = enemyTypes[0](
                                window,
                                x = windowDimensions[0] * random.random(),
                                y = (windowDimensions[1]/3) * random.random() + windowDimensions[1]/3,
                                cellSize=cellSize,
                                speed = random.uniform(1,2)*(63/cellSize[0])
                        )
                        spawnedEnemies.append(e)

        elif level == 2:
                if gameTimer/gameDelay % (gameDelay * 8) == 0:
                        spawnEnemy = True
                        e = enemyTypes[0](
                                window,
                                x = windowDimensions[0] * random.random(),
                                y = (windowDimensions[1]/3) * random.random() + windowDimensions[1]/3,
                                cellSize=cellSize,
                                speed = random.uniform(1,2)*(63/cellSize[0])
                        )
                        spawnedEnemies.append(e)

        elif level == 3:
                if gameTimer/gameDelay % (gameDelay * 8) == 0:
                        spawnEnemy = True
                        e = enemyTypes[0](
                                window,
                                x = windowDimensions[0] * random.random(),
                                y = (windowDimensions[1]/3) * random.random() + windowDimensions[1]/3,
                                cellSize=cellSize,
                                speed = random.uniform(1,2)*(63/cellSize[0])
                        )
                        spawnedEnemies.append(e)
                if gameTimer/gameDelay % (gameDelay * 50) == 0:
                        spawnEnemy = True
                        e = enemyTypes[1](
                                window,
                                x = windowDimensions[0] * random.random(),
                                y = (windowDimensions[1]/3) * random.random() + windowDimensions[1]/3,
                                cellSize=cellSize,
                                speed = random.uniform(1,2)*(63/cellSize[0])
                        )
                        spawnedEnemies.append(e)

        elif level == 4:
                if gameTimer/gameDelay % (gameDelay * 5) == 0:
                        spawnEnemy = True
                        e = enemyTypes[0](
                                window,
                                x = windowDimensions[0] * random.random(),
                                y = (windowDimensions[1]/3) * random.random() + windowDimensions[1]/3,
                                cellSize=cellSize,
                                speed = random.uniform(1,2)*(63/cellSize[0])
                        )
                        spawnedEnemies.append(e)
                if gameTimer/gameDelay % (gameDelay * 25) == 0:
                        spawnEnemy = True
                        e = enemyTypes[1](
                                window,
                                x = windowDimensions[0] * random.random(),
                                y = (windowDimensions[1]/3) * random.random() + windowDimensions[1]/3,
                                cellSize=cellSize,
                                speed = random.uniform(1,2)*(63/cellSize[0])
                        )
                        spawnedEnemies.append(e)

        elif level >= 5:
                mod = level - 4
                mod = mod ** 0.5
                if gameTimer/gameDelay % int(gameDelay * 5 / mod) == 0:
                        spawnEnemy = True
                        e = enemyTypes[0](
                                window,
                                x = windowDimensions[0] * random.random(),
                                y = (windowDimensions[1]/3) * random.random() + windowDimensions[1]/3,
                                cellSize=cellSize,
                                speed = random.uniform(1,2)*(63/cellSize[0])
                        )
                        spawnedEnemies.append(e)
                if gameTimer/gameDelay % int(gameDelay * 15 / mod) == 0:
                        spawnEnemy = True
                        e = enemyTypes[1](
                                window,
                                x = windowDimensions[0] * random.random(),
                                y = (windowDimensions[1]/3) * random.random() + windowDimensions[1]/3,
                                cellSize=cellSize,
                                speed = random.uniform(1,2)*(63/cellSize[0])
                        )
                        spawnedEnemies.append(e)
        for e in spawnedEnemies:
                e.init()
                enemiesInScene.append(e)

        cursor.position = pygame.mouse.get_pos()

        pygame.time.delay(gameDelay)
        gameTimer += gameDelay
        #print(gameTimer/gameDelay)

        tilemap.drawBackground(window, tilemapCellSize, seed)
        #window.fill((30, 30, 120))
        pygame.draw.rect(window, "green", (shop.cellSizeAdjusted[0] * selectedTower["position"][0], shop.cellSizeAdjusted[1] * selectedTower["position"][1], shop.cellSizeAdjusted[1], shop.cellSizeAdjusted[1]))
        moneyText =  (
                        font.render(f"Money: {money}", True, (20,190,20)),
                        (17, 0)
                )
        healthText = (
                        font.render(f"Health: {health}", True, (200,20,20)),
                        (17, 0.5)
                )
        pointsText =   (
                        font.render(f"Points: {points}", True, (60,120,200)),
                        (17, 1)
                )
        costText =   (
                        font.render(f"Cost: {selectedTower['cost']}", True, (120,120,0)),
                        (17, 9)
                )

        texts = [moneyText, healthText, pointsText, costText]
        shop.draw(money, texts)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                        #Cell that the mouse is in
                        mouseCell = (
                                cursor.position[0] // cellSize[0],
                                cursor.position[1] // cellSize[1]
                        )
                        if tilemap.tilemap[int(mouseCell[1])][int(mouseCell[0])] == 1:
                                if pygame.mouse.get_pressed()[0]: # Creates tower on left click
                                        isTower = False
                                        for tower in towersInScene: # Finds towers in the same cell as the mouse and deletes them
                                                if tower.position == mouseCell:
                                                        isTower = True
                                                        break
                                        if not isTower and money >= selectedTower["cost"]:
                                                T = selectedTower["tower"](window, position=mouseCell, cellSize=cellSize)
                                                T.init()
                                                towersInScene.append(T)
                                                money -= selectedTower["cost"]
                        else:
                                if pygame.mouse.get_pressed()[0] and mouseCell[0]>16: # Creates tower on left click
                                        selectedTower = shop.click(cursor.position)
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                        enemiesInScene.append(random.choice(enemyTypes)(
                                        window,
                                        x = windowDimensions[0] * random.random(),
                                        y = (windowDimensions[1]/3) * random.random() + windowDimensions[1]/3,
                                        cellSize=cellSize,
                                        speed = random.uniform(1,2)
                                        )
                        )
        if pygame.mouse.get_pressed()[2]: # Deletes right clicked tower
                x = 0
                mouseCell = (
                        cursor.position[0] // cellSize[0],
                        cursor.position[1] // cellSize[1]
                )
                for tower in towersInScene: # Finds towers in the same cell as the mouse and deletes them
                        if tower.position == mouseCell:
                                del towersInScene[x]
                                money += towers.typeCost[tower.type] * 0.9
                                break
                        else:
                                x += 1



        for tower in towersInScene: #Draws cooldown circle for each tower
                #tower.drawCooldown(False)
                # False: Fills whole circle at once as cooldownCounter decreases
                # True : Fills circle in by quadrant as cooldownCounter decreases
                if tower.initialised == False:
                        tower.init()


        for tower in towersInScene: # Draws each tower
                tower.draw()
        for tower in towersInScene: # Attacking logic for tower
                tower.findClosestTarget(enemiesInScene)
                tower.attack()

        x = 0
        for enemy in enemiesInScene: #Enemy Logic
                enemy.sim() # Draws enemy to screen & Moves enemy to right at it's speed

                if enemy.state != "alive":
                        if enemy.state == "killed":
                                money += enemy.reward
                                points += enemy.reward * 4.5
                        else:
                                health -= enemy.damage
                        del enemiesInScene[x]
                else:
                        x += 1

        pygame.display.flip()
        if health <= 0:
                break
x = 0
for enemy in enemiesInScene:
        x += 1


while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
        window.fill("black")
        pygame.display.update()