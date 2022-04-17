import pygame
from random import randint
from camera_group import CameraGroup
from events import Events
from level import Level
from player import Player
from portal import Portal
from window import Window
from menu import Menu
from text import Text

class Goinghome:

    def __init__(self):
        """ Initializes the game """
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
        # Load level 1 initially
        self.level = Level(level_background="assets/_IMGS/_Lvl1/level1_bg.png")
        # Initialize camera_group
        self.camera_group = CameraGroup(self.level)
        # Initialize portal
        self.level.place_portal(self.camera_group)
        # Initialize player
        self.player = Player((self.window.width/2, self.window.height/2), self.camera_group)

    def run_game(self):
        """Runs the game"""    
        pygame.mixer.Sound.play(self.menu.menusound, loops=-1)
        pygame.mouse.set_visible(False)
        # Start game
        while True:
            # If the game has not been started, show the menu
            if not self.game_running:
                # Choose setting an get the chosen level
                self.game_running, level_selection = self.menu.show_menu(self.window)
            elif self.game_running:
                # Start game with selected level
                self.level.load_level(level_selection, self.camera_group)

                # Checks input events for player and camera
                self.events.check_events(self.camera_group)

                # Calls update method of every sprite in the camera group
                self.camera_group.update()
                self.camera_group.custom_draw(self.player, self.level)

                self.level.portal.check_collision(self.player, self.window)

            # Updates screen
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance and run the game
    gh = Goinghome()
    gh.run_game()