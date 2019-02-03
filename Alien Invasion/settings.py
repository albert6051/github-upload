import pygame

class Settings():
    # Class to store all the settings for the Alien Invasion game

    def __init__(self):
        # Initialize the game's static settings
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        # 12-1 implementation Setting background color
        self.bg_color = (0,190,220)

        # Ship settings
        self.ship_limit = 3

        # 12-5 implementation
        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_forward_speed = 20

        # Raindrop settings
        self.raindrop_speed_factor = 5
        self.raindrop_allowed = 40

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        # 14-6 implementation Set sound effects
        self.shooting_sound = pygame.mixer.Sound('sound/Shooting.wav')
        self.explosion_sound = pygame.mixer.Sound('sound/Explosion.wav')

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        # Initialize settings that change throughout the game
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50
    
    def increase_speed(self):
        # Increase speed settings and alien point values
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)