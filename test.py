import pygame
import objects

pygame.init()
window = pygame.display.set_mode((1260, 810))



def draw_game():
    global window
    for row in range(len(objects.tilemap)):

        for column in range(len(objects.tilemap[row])):

            x = objects.textures[objects.tilemap[row][column]]
            y = (column*objects.tilesize, row*objects.tilesize)
            window.blit(x, y)




run = True
while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False

        draw_game()
        pygame.display.update()