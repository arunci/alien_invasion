import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            # Redraw the screen during each pass through the loop
            self.ship.update()
            self._update_screen()

            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)

    def _check_key_down_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_key_up_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
