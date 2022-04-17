import pygame

# Import own classes
from settings_background import Background
from settings_inputevents import Inputevents
from screen_menu import Menu
from utility_saves import Saves

class Goinghome:
    '''Manages the game'''

    def __init__(self):
        
        pygame.init()

        self.player_lvl = 0

        # Rename Imports
        self.background = Background()
        self.inputevents = Inputevents()
        self.menu = Menu()
        self.saves = Saves()

        self.menusound = pygame.mixer.Sound('_MUS/Timegame_menu.mp3')

    def run_game(self):
        '''Runs Going Home'''

        self.menusound.set_volume(0.5)
        pygame.mixer.Sound.play(self.menusound, loops=-1)

        # Start game
        while True:

            pygame.mouse.set_visible(False)

            # Start ingame events
            self.background.create_window()

            # Check for input
            self.inputevents.check_keyevents()

            # Start in menu
            map = self.menu.show_menu(self.background, self.saves)

            # Load map
            self.menu.load_level(map, self.background)

            # Updates screen
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game
    gh = Goinghome()
    gh.run_game()