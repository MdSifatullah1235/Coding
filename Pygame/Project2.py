import pygame
pygame.init()

screen_width = 500
screen_height = 600

display_surface = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Some Images !")

background_image  = pygame.transform.scale(pygame.image.load("images/Backgorund.jpg").convert(), (screen_width,screen_height))

penguin_image = pygame.transform.scale(pygame.image.load("images/Penguin.png").convert_alpha(),(200,200))

text = pygame.font.Font(None,36).render("Penguin",True,pygame.color("black"))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        display_surface.blit(background_image,(0,0))
        display_surface.blit(penguin_image,(300,200))
        display_surface.blit(text,(350,400))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    game_loop()