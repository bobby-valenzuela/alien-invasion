#!/usr/bin/python3

import sys,os,pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

# try:
#     os.environ["DISPLAY"]
# except:
#     os.environ["SDL_VIDEODRIVER"] = "dummy"

class AlienInvasion():

    """Overall class to manage game behavior"""

    def __init__(self):
        """Initialize game and resources."""
        pygame.init()
        self.settings = Settings()
        self.fullscreen = False
        # ^ Use this to set full screen for H/W specified in settings

        if self.fullscreen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main game loop."""

        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            self._update_bullets()

    def _check_events(self):
        """Watch for keyboard/mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create new bullet and addit to the bullet group"""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
            # Get rid of bullets that have disappeard.
            for bullet in self.bullets.copy():

                if bullet.rect.bottom <= 0 :
                    self.bullets.remove(bullet)

    def _update_screen(self):
        # Redraw screen - on each iteration
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():

            bullet.draw_bullet()

        # Make most recent drawn screen visible 
        # Note: should run at end of this method to catch all changes
        pygame.display.flip()



if __name__ == '__main__':
    # Make a game instance and run game.
    ai = AlienInvasion()
    ai.run_game()

"""
== Requirements==

Win: python -m pip install pygame
Lin: python3 -m pip install pygame


Copy to local...
    cp -r ../alien-invasion /mnt/c/Users/Bobby/Documents/
"""

