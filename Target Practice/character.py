import pygame
from ship import Ship

# 12-2 implementation
class Character(Ship):
    def __init__(self, ai_settings, screen):
        # Initialize the Character using super() to call the Ship constructor
        super().__init__(ai_settings, screen)

        # Load the character image and get its rect
        self.image = pygame.image.load('images/Star_Fox.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set the ship at the bottom center of the screen at every start
        self.rect.center = self.screen_rect.center