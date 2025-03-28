import pygame
import objects
import random

pygame.init()
display = pygame.display.set_mode((1280, 640))



def draw_game():
    for row in range(len(objects.tilemap)):
        for column in range(len(objects.tilemap[row])):
            image = objects.textures[objects.tilemap[row][column]]
            destination = (column*objects.tilesize, row*objects.tilesize)

            image = pygame.transform.scale(image, (64,64))
            display.blit(image, destination)




run = True
while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        draw_game()
        pygame.display.update()