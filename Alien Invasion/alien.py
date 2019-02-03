import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # A class to represent a single alien in the fleet
    def __init__(self, ai_settings, screen):
        # Initialize the alien
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/aliens.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def check_edges(self):
        # Return True if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True

    def update(self):
        # Move the alien down
        self.y += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.y = self.y