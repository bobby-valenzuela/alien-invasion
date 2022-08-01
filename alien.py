#!/usr/bin/env python

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single Alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize alien and set starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load alien image and set its rect attribute
        self.image = pygame.image.load('images/alien_ship.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store aliens exact horizontal position
        self.x = float(self.rect.x)