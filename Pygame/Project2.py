import pygame
pygame.init()

screen_width = 500
screen_height = 600

display_surface = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Some Images !")

background_image  = pygame.transform.scale(pygame.image.load("images/Backgorund.jpg").convert(), (screen_width,screen_height))

penguin_image = pygame.transform.scale(pygame.image.load("images/Penguin.png").convert_alpha(),(200,200))