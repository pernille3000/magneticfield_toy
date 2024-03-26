import pygame

class Sun:
    def __init__(self, screen):
        self.screen = screen
        # Add sun properties and behavior here
        self.sun_img_original = pygame.image.load("jorden2d.png") 
        self.sun_rect = self.sun_img_original.get_rect(topleft=(100, self.screen.get_height() // 2))
        self.rotating = False
        self.rotation_angle = 0
        self.rotation_speed = 15
        self.rotation_threshold = 1

    def rotate(self):
        pass  # Add rotation logic here