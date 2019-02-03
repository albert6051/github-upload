import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    # A class represent the space ship
    def __init__(self, ai_settings, screen):
        super().__init__()
        # Ship initilization and set up
        self.screen = screen
        self.ai_settings = ai_settings

        # 12-5 implementation
        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship_sideway.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set the ship at the center of the screen at every start
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the ship's center
        self.xcenter = float(self.rect.centerx)
        self.ycenter = float(self.rect.centery)

        # 12-3 implementation
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    # 12-3 implementation
    def update(self):
        # Update the ship's center base on movement flag and bound its moveing range within the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.xcenter += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.xcenter -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.ycenter -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.ycenter += self.ai_settings.ship_speed_factor
        
        # Update the ship's rect position from self.center
        self.rect.centerx = self.xcenter
        self.rect.centery = self.ycenter

    def blitme(self):
        # Paint the ship on the screen
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        # Move the ship back to original position
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery
        self.xcenter = float(self.rect.centerx)
        self.ycenter = float(self.rect.centery)
        self.rect.centerx = self.xcenter
        self.rect.centery = self.ycenter