import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))

isclose = True

while isclose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isclose = False

    pygame.draw.rect(screen,(0,125,225),pygame.Rect(30,30,60,60))
    pygame.display.flip()