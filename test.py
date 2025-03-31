import pygame
import tilemap
import random

pygame.init()
display = pygame.display.set_mode((1280, 640))



def draw_game():
    for row in range(len(tilemap.tilemap)):
        for column in range(len(tilemap.tilemap[row])):
            image = tilemap.textures[tilemap.tilemap[row][column]]
            destination = (column*tilemap.tilesize, row*tilemap.tilesize)

            image = pygame.transform.scale(image, (64,64))
            display.blit(image, destination)




run = True
while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        tilemap.drawBackground(display)
        pygame.display.update()