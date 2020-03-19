import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('snake')

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
