#!/usr/bin/python3

class Settings:
    """A class to store all setings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings."""

        # Screen settings
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 2
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3 # Num of bullets visible on screen at a given time

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Fleet_direction of 1 represents right; -1 = left
        self.fleet_direction = 1
