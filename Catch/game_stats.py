# 13-5 & 13-6 implementation
class GameStats():
    # Track statistics for ball catcher
    
    def __init__(self, ai_settings):
        # Initialize statistics
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start ball catcher in an active state.
        self.game_active = True
        
    def reset_stats(self):
        # Initialize statistics that can change during the game
        self.catcher_left = self.ai_settings.catcher_limit
