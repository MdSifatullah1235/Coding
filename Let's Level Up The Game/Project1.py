import pygame
import random

import pygame.image

screen_height, screen_width = 500,400
movement_speed = 5
font_size = 70

pygame.init()
background_image = pygame.image.load("./images/GameBG.jpg")
Font = pygame.font.SysFont("Times New Roman",font_size)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color,height,width):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(pygame.Color("blue"))
        pygame.draw.rect(self.image,color,pygame.rect(0,0,width,height))
        self.rect = self.image.get_rect()

    def move(self,x,y):
        self.rect.x = max(min(self.rect.x + x, screen_width - self.rect.width), 0 )
        self.rect.y = max(min(self.rect.y + y, screen_height - self.rect.height), 0 )


Screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Sprite Collision")

all_sprites = pygame.sprite.Group()

sp1 = Sprite(pygame.Color("red"),20,30)
sp1.rect.x , sp1.rect.y = random.randint(0,screen_width - sp1.rect.width),random.randint(0,screen_height - sp1.rect.height)
all_sprites.add(sp1)

sp2 = Sprite(pygame.Color("black"),20,30)
sp2.rect.x , sp2.rect.y = random.randint(0,screen_width - sp2.rect.width),random.randint(0,screen_height - sp2.rect.height)
all_sprites.add(sp2)

running, win  = True, False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not win:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * movement_speed
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP])* movement_speed

        sp1.move(x_change,y_change)

        if sp1.rect.colliderect(sp2.rect):
            all_sprites.remove(sp2)
            won = True

    Screen.blit(background_image,(0,0))
    all_sprites.draw(Screen)

    if win:
        text = Font.render("Tou Win",True,pygame.Color("black"))
        Screen.blit(text, (100,100))


    pygame.display.flip()
    clock.tick(90)

