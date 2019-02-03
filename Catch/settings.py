# 13-5 & 13-6 implementation
class Settings():
    # A class to store all settings for ball catcher

    def __init__(self):
        # Initialize the game's settings
        # Screen settings
        self.screen_width = 900
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # cather settings.
        self.catcher_speed_factor = 1.5
        self.catcher_limit = 2
        
        # ball settings.
        self.ball_drop_speed = 1
