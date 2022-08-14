#!/usr/bin/python3

import sys,os,pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats

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

        # Create an instance to store game stats
        self.stats = GameStats(self)
        self.stats.game_active = False
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main game loop."""

        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                # self.bullets.update()
                
            self._update_screen()

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

            self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""
        # Remove bullets and aliens that have collided

        collisions = pygame.sprite.groupcollide( self.bullets, self.aliens, True, True )

        # Check for any bullets that have hit aliens
        # If so, get rid of the bullet and the alien
        if not self.aliens:
            """Destroy existing bullets and create new fleet"""
            self.bullets.empty()
            self._create_fleet()
        

    def _update_screen(self):
        # Redraw screen - on each iteration
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():

            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Make most recent drawn screen visible 
        # Note: should run at end of this method to catch all changes
        pygame.display.flip()

    def _create_alien(self, alien_number, row_number):
        # Create aliens and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """Create a fleet of aliens"""
        # Make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - ( 2 * alien_width )
        number_aliens_x = available_space_x // ( 2 * alien_width )

        # Determine the number of rows aliens that fit on screen
        ship_height = self.ship.rect.height
        available_space_y = ( self.settings.screen_height - ( 3 * alien_height ) - ship_height )
        number_rows = available_space_y // ( 2 * alien_height )

        # Create fleet row of aliens
        for row_number in range( number_rows ):
            # Create row of aliens
            for alien_number in range(number_aliens_x) :
                self._create_alien(alien_number, row_number)

    def _update_aliens(self):
        """Check  if fleet is at an edge - Update positions of all aliens in fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for alients hitting the bottom of the screen
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """response as needed if alien  reaches an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:

            # Decrements ships left
            self.stats.ships_left =- 1

            # Get rid of remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            # pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        """Check if any aliens have reaced the bottom of the screen"""
        screen_rect = self.screen.get.rect()

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this ship the same as if the ship got hit
                self._ship_hit()
                break

            # # Look for aliens hitting the bottom of the screen
            # self._check_aliens_bottom()

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

