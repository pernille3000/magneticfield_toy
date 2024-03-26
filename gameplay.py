import pygame

class Game:
    def __init__(self, screen, player, sun):
        self.screen = screen
        self.player = player
        self.sun = sun
        self.score = 0
        self.aurora = False

    def handle_mouse_click(self, pos):
        if not self.player.rotating and self.player.ship_rect.collidepoint(pos):
            self.player.rotating = True

    def update(self):
        if self.player.rotating:
            self.player.rotation_angle += self.player.rotation_speed
            if self.player.rotation_speed > 0:
                self.player.rotation_speed = max(0, self.player.rotation_speed - 0.05)
            else:
                self.player.rotating = False
            # Check if the magnetic field is activated
            if self.player.rotation_speed <= self.player.rotation_threshold:
                self.score += 1  # Increment score
                self.aurora = True  # Activate aurora
            else:
                self.aurora = False  # Deactivate aurora

        # Add logic for sun's behavior (e.g., attacking Earth with radiation)

    def draw(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black color
        # Draw sun, Earth, and other game elements
        # self.screen.blit(self.sun.sun_img_original, self.sun.sun_rect) 
        self.screen.blit(self.player.ship_img_original, self.player.ship_rect)
        
        # Draw score on the screen
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
