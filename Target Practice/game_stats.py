class GameStats():
    # Track statistics for Target Practice
    def __init__(self, ai_settings):
        # Initialize statistics
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start Target Practice in an active state
        self.game_active = False


    def reset_stats(self):
        # Initialize statistics that can change during the game
        self.miss_left = self.ai_settings.miss_limit