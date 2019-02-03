import pygame
from alien import Alien

# 13-3 implementation
class Raindrop(Alien):
    # A class to represent single rain_drop on the screen
    def __init__(self, ai_settings, screen):
        # Initialize the rain_drop using super() to call the Alien constructor
        super().__init__(ai_settings, screen)

        # Load the rain_drop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

    def update(self):
        # Move the raindrop down
        self.y += self.ai_settings.raindrop_speed_factor
        self.rect.y = self.y