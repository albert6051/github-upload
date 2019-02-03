class GameStats():
    # Track statistics for Alien Invasion
    def __init__(self, ai_settings):
        # Initialize statistics
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start Alien Invasion in an active state
        self.game_active = False

        # 14-4 implementation
        # High score is read form the file and should never be reset during the game
        self.high_score = int(self.read_high_score())

    def reset_stats(self):
        # Initialize statistics that can change during the game
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    # 14-4 implementation
    def read_high_score(self):
        # Read high_score from the file high_score.text
        f = open('high_score.txt', 'r')
        high_score = f.read()
        f.close()
        return high_score