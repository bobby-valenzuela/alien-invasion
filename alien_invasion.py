#!/usr/bin/python3

import sys
import pygame
from settings import Settings

class AlienInvasion():

    """Overall class to manage game behavior"""

    def __init__(self):
        """Initialize game and resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main game loop."""

        while True:
            """Watch for keyboard/mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                print(pygame.QUIT)

            # Redraw screen - on each iteration
            self.screen.fill(self.settings.bg_color)

            # Make most recent drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run game.
    ai = AlienInvasion()
    ai.run_game()

"""
== Requirements==

Win: python -m pip install pygame
Lin: python3 -m pip install pygame

"""
