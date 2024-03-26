import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Ship")

# Load ship image
ship_img_original = pygame.image.load("kerne1.png")  # Replace "jorden1.png" with your ship image file path
ship_rect = ship_img_original.get_rect(topleft=(50, HEIGHT // 2))  # Set ship position to left side of the screen

# Define variables for rotation
rotating = False
rotation_angle = 0
rotation_speed = 15  # Initial rotation speed (degrees per frame)
rotation_threshold = 1  # Rotation speed threshold to stop rotation

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not rotating and ship_rect.collidepoint(event.pos):  # Start rotating the ship if not already rotating and clicked on the ship
                rotating = True

    # Rotate ship if rotating is True
    if rotating:
        rotation_angle += rotation_speed
        if rotation_speed > 0:
            rotation_speed = max(0, rotation_speed - 0.05)  # Decrease rotation speed gradually
        else:
            rotating = False  # Stop rotating if rotation speed reaches 0

    # Rotate ship image
    ship_img_rotated = pygame.transform.rotate(ship_img_original, rotation_angle)
    ship_rect = ship_img_rotated.get_rect(center=ship_rect.center)  # Update ship rectangle after rotation

    # Drawing
    screen.fill((0, 0, 0))  # Fill the screen with black color
    screen.blit(ship_img_rotated, ship_rect)  # Draw the rotated ship

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)  # Limit frame rate to 60 frames per second

# Quit Pygame
pygame.quit()
sys.exit()
