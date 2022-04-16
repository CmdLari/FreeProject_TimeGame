import pygame
from level import Level

# Import own classes
from window import Window
from settings_inputevents import Inputevents
from settings_gamestate import Gamestate
from menu import Menu
from util import Util

class Goinghome:
    '''Manages the game'''

    def __init__(self):
        '''Initializes the game'''
        pygame.init()
        
        # Create window
        self.window = Window()
        # Create inputevents
        self.inputevents = Inputevents()
        # Create menu
        self.menu = Menu()
        self.game_running = False

        # self.saves = Saves()
        # self.gamestate = Gamestate(self.window, self.menu, self.saves)

    def run_game(self):
        '''Runs Going Home'''      
        pygame.mixer.Sound.play(self.menu.menusound, loops=-1)
        pygame.mouse.set_visible(False)
        # Start game
        while True:

            # Check for input
            self.inputevents.check_keyevents()

            # If the game has not been started, show the menu
            if not self.game_running:
                # Chose Setting
                self.game_running = self.menu.show_menu(self.window)

            #self.gamestate.setup_screen()

            # Updates screen
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game
    gh = Goinghome()
    gh.run_game()