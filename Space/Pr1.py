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

playerIMG = pygame.image.load("Player.png")
icon = pygame.image.load("ufo.png")
pygame.display.set_caption("Space Invaders")

pygame.display.set_icon(icon)

playerX = PLAYER_STRAT_X
playerY = PLAYER_STRAT_Y

player_x_change = 0

enemyIMG = []
enemyX = []
enemyY = []
enemy_x_change = []
enemy_y_change = []
num_enemies = 6

for i in range(num_enemies):
    enemyIMG.append(pygame.image.load("Enemy.png"))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_YMIN,ENEMY_START_YMAX))
    enemy_x_change.append(ENEMY_SPEED_X)
    enemy_y_change.append(ENEMY_START_Y)

bulletIMG = pygame.image.load("Bullet.png")
bulletX = 0
bulletY = PLAYER_STRAT_Y
bulletx_change  = 0
bullety_change = BULLET_SPEED_Y
bullet_state = "ready"

