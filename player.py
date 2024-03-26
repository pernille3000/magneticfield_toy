import pygame

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.ship_img_original = pygame.image.load("kernen2d.png")  
        self.ship_rect = self.ship_img_original.get_rect(topleft=(50, self.screen.get_height() // 2))
        self.rotating = False
        self.rotation_angle = 0
        self.rotation_speed = 15
        self.rotation_threshold = 1

    def rotate(self):
        pass  # Add rotation logic here
