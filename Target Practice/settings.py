class Settings():
    # Class to store all the settings for the target practice game

    def __init__(self):
        # Initialize the game's static settings
        # Screen settings
        self.screen_width = 900
        self.screen_height = 700
        # Setting background color
        self.bg_color = (0,190,220)

        # Ship settings
        self.miss_limit = 2

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # Target setting
        self.target_width = 15
        self.target_height = 200
        self.target_color = 60, 60, 60
        self.target_hit = 0

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        # Initialize settings that change throughout the game
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 2
        self.target_speed_factor = 1

        # target_direction of 1 represents down; -1 represents up
        self.target_direction = 1
    
    def increase_speed(self):
        # Increase speed settings
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.target_speed_factor *= self.speedup_scale