# Imports
import pygame

from screen import Screen
from menu import Menu
from level import Level

class Goinghome:

    def __init__(self):
        """ Initializes the game """
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(10)
        # Initialize window
        self.screen = Screen()
        # Initialize menu
        self.menu = Menu(self.screen)
        # Initialize Game state
        self.gamestate = False
        # Initialize Level loading
        self.level = Level(self.screen, self.menu)

    def run_game(self):
        """Runs the game"""    
        pygame.mouse.set_visible(False)
        # Start game
        while True:
            # If the game has not been started, show the menu
            if not self.gamestate:
                self.gamestate = self.menu.check_mouseclicks()
                self.menu.draw_menu()
            # If the game has been started, draw a level
            elif self.gamestate:
                self.level.start_level()
               
            # Updates screen
            pygame.display.flip()
            self.clock.tick(60)

# Game Loop
if __name__ == '__main__':
    # Make a game instance and run the game
    gh = Goinghome()
    gh.run_game()