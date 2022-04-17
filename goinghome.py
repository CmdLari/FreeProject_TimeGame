from random import randint
import pygame
from camera_group import CameraGroup
from level import Level
from player import Player
from test_trees import Tree

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

        self.camera_group = CameraGroup()
        self.player = Player((self.window.width/2, self.window.height/2), self.camera_group)

        for i in range(20):
            random_x = randint(1000, 2000)
            random_y = randint(1000, 2000)
            Tree((random_x, random_y), self.camera_group)

        # self.saves = Saves()
        # self.gamestate = Gamestate(self.window, self.menu, self.saves)

    def run_game(self):
        '''Runs Going Home'''      
        pygame.mixer.Sound.play(self.menu.menusound, loops=-1)
        pygame.mouse.set_visible(False)
        # Start game
        while True:

            # Check for input
            #self.inputevents.check_keyevents()

            # If the game has not been started, show the menu
            if not self.game_running:
                # Chose Setting
                self.game_running, level_selection = self.menu.show_menu(self.window)
            elif self.game_running:
                # Start game with selected level
                level = Level()
                level.load_level(level_selection, self.window)
                # Check Player input
                self.player.check_keyevents()

                self.camera_group.update()
                self.camera_group.custom_draw(self.player, level)

            #self.gamestate.setup_screen()
            #pygame.display.update()

            # Updates screen
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game
    gh = Goinghome()
    gh.run_game()