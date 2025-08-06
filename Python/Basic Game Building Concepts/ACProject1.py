import pygame
pygame.init()

screen = pygame.display.set_mode((640,480))

isclose = True

while isclose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isclose = False

    pygame.draw.rect(screen, (0, 125, 225), pygame.Rect(290, 210, 60, 60))
    pygame.display.flip()