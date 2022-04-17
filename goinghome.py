import pygame
from random import randint
from camera_group import CameraGroup
from events import Events
from level import Level
from player import Player
from portal import Portal
from window import Window
from menu import Menu

class Goinghome:
    '''Manages the game'''

    def __init__(self):
        '''Initializes the game'''
        pygame.init()
        self.clock = pygame.time.Clock()
        # Initialize window
        self.window = Window()
        # Initialize event handler
        self.events = Events()
        # Initialize menu
        self.menu = Menu()
        # Initialize Game state
        self.game_running = False
        # Initialize camera_group
        self.camera_group = CameraGroup()
        # Initialize player
        self.player = Player((self.window.width/2, self.window.height/2), self.camera_group)
        # Initialize portals on random positions
        for i in range(20):
            random_x = randint(1000, 2000)
            random_y = randint(1000, 2000)
            Portal((random_x, random_y), self.camera_group)

    def run_game(self):
        '''Runs Going Home'''      
        pygame.mixer.Sound.play(self.menu.menusound, loops=-1)
        pygame.mouse.set_visible(False)
        # Start game
        while True:
            # If the game has not been started, show the menu
            if not self.game_running:
                # Chose Setting
                self.game_running, level_selection = self.menu.show_menu(self.window)
            elif self.game_running:
                # Start game with selected level
                level = Level()
                level.load_level(level_selection, self.window)

                # Checks input events for player and camera
                self.events.check_events(self.player, self.camera_group)

                self.camera_group.update()
                self.camera_group.custom_draw(self.player, level)

            # Updates screen
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance and run the game
    gh = Goinghome()
    gh.run_game()