import math
import random
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_STRAT_X = 370
PLAYER_STRAT_Y = 380
ENEMY_START_YMIN = 50
ENEMY_START_YMAX = 150
ENEMY_SPEED_X = 4
ENEMY_START_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
bg = pygame.image.load("SpaceBG.jpg")
