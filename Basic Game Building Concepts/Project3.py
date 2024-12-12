import pygame

def main():
    pygame.init()
    screen_width = 500
    screen_height = 500
    screen = pygame.display.set_mode((screen_width,screen_height))

    pygame.display.set_caption("Color Changing Sprites")

    colors = {
        "red": pygame.Color("red"),
        "yellow": pygame.Color("yellow"),
        "green": pygame.Color("green"),
        "white": pygame.Color("white"),
        "blue": pygame.Color("blue")
    }

    current_color = colors["white"]
    x,y = 30,30
    sprite_width,sprite_height = 100,100
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: x += 3

        x = min(max(0,x), screen_width - sprite_width)
        x = min(max(0,y), screen_height - sprite_height)
        if x == 0: current_color = colors["red"]
        elif x == screen_width - sprite_width: current_color = colors["yellow"]
        elif y == screen_height - sprite_height: current_color = colors["green"]
        elif y == 0: current_color = colors["blue"]
        else: current_color = colors["white"]

        screen.fill((0,0,0))
        pygame.draw.rect(screen)


