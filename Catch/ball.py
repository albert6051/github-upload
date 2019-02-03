import pygame
from pygame.sprite import Sprite

# 13-5 & 13-6 implementation
class Ball(Sprite):
    # A class to represent a falling ball

    def __init__(self, ai_settings, screen):
        # Initialize the ball, and set its starting position
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image, and set its rect attribute.
        self.image = pygame.image.load('images/ball.PNG')
        self.rect = self.image.get_rect()

        # Start each new ball near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        # Draw the ball at its current location
        self.screen.blit(self.image, self.rect)
    
    def update(self, ai_settings):
        # Update ball position as it is droping
        self.rect.y += ai_settings.ball_drop_speed
