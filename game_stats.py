class GameStats:
    """Track statistic for alien invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start game in inactive state
        self.game_active = False

        # High score can't be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize dynamic statistics"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1