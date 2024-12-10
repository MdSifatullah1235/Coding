import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 500
screen_height = 600

display_surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Some Images!")

# Load and scale background image
background_image = pygame.transform.scale(
    pygame.image.load("Pygame/images/Background.jpg").convert(), 
    (screen_width, screen_height)
)

# Load and scale penguin image
penguin_image = pygame.transform.scale(
    pygame.image.load("Pygame/images/Penguin.png").convert_alpha(), 
    (200, 200)
)

# Render text
font = pygame.font.Font(None, 36)
text = font.render("Penguin", True, pygame.Color("black"))

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw everything
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, (150, 200))  # Centered horizontally
        display_surface.blit(text, (180, 450))          # Adjusted text position

        # Update display
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Run the game loop
if __name__ == "__main__":
    game_loop()