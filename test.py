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

pygame.display.set_mode((800, 500))
icon_32x32 = pygame.image.load("snake-icon.png").convert_alpha()
pygame.display.set_icon(icon_32x32)
 
exit = False
while exit == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True