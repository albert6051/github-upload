import pygame
from alien import Alien

# 13-1 implementation
class Star(Alien):
    # A class to represent single star on the screen
    def __init__(self, ai_settings, screen):
        # Initialize the star using super() to call the Alien constructor
        super().__init__(ai_settings, screen)

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()