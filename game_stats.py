#!/usr/bin/env python3

from cgitb import reset


class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien invasation in an inactive state
        self.game_active = True

    def reset_stats(self):
        """Initialize stats that change during game"""
        self.ships_left = self.settings.ship_limit