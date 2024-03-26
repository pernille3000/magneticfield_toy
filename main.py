import pygame
import sys
from player import Player
from sun import Sun
from gameplay import Game

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Magneticfield toy")

# Create game objects
player = Player(screen)
sun = Sun(screen)
game = Game(screen, player, sun)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.handle_mouse_click(event.pos)

    # Update game state
    game.update()

    # Drawing
    game.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)  # Limit frame rate to 60 frames per second

# Quit Pygame
pygame.quit()
sys.exit()
