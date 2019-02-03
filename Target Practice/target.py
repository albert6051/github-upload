import pygame
from pygame.sprite import Sprite

class Target(Sprite):
    # Class create to manage the target in target practice

    def __init__(self, ai_settings, screen):
        # Create a target object at right side
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        # Create a target rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.target_width,ai_settings.target_height)

        # Set the target at the right side and 100 pix toward left
        self.rect.right = self.screen_rect.right - 100
        self.rect.centery = self.screen_rect.centery
        
        # Store the target's position as a decimal value.
        self.xcenter = float(self.rect.centerx)
        self.ycenter = float(self.rect.centery)

        # Update the target's rect position from self.center
        self.rect.centerx = self.xcenter
        self.rect.centery = self.ycenter

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.target_speed_factor
    
    def check_edges(self):
        # Return True if target is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True
    
    def update(self):
        # Move the target up and down
        self.ycenter += (self.ai_settings.target_speed_factor * self.ai_settings.target_direction)
        self.rect.y = self.ycenter

    def draw_target(self):
        # Draw the target to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)