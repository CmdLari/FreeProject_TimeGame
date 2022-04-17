from typing import Tuple
from window import Window
import pygame
import sys

class Menu:
    """ Represents the menu. """

    def __init__(self):
        """Initialize the menu"""

        # Assets Menu
        self.menubackground = pygame.image.load("_IMGS/_Menu/menu_background.png")

        # Mouse
        self.mouse = pygame.image.load("_IMGS/_Menu/menu_mouse.png")
        
        # -- Buttons
        self.button_newgame = pygame.image.load("_IMGS/_Menu/menu_button_new_game.png")
        self.button_continue = pygame.image.load("_IMGS/_Menu/menu_button_continue.png")
        self.button_quit = pygame.image.load("_IMGS/_Menu/menu_button_quit.png")  

        # Music
        self.menusound = pygame.mixer.Sound('_MUS/Timegame_menu.mp3')
        self.menusound.set_volume(0.1)
    
    def show_menu(self, window: Window) -> Tuple[bool, int]:
        """ Shows the menu on the given window.

        Args:
            window: The window to draw the menu to

        Returns:
            A tuple containing the game state and the level selection
        """
        # Background
        window.blit_img(self.menubackground, 0, 0)

        # Buttons
        window.blit_img(self.button_newgame, 0, -self.button_continue.get_rect().height-10)
        window.blit_img(self.button_continue, 0, 0)
        window.blit_img(self.button_quit, 0, self.button_continue.get_rect().height+10)

        self.new_game_rect = pygame.Rect(window.width/2 - self.button_newgame.get_rect().width/2, window.height/2 - self.button_newgame.get_rect().height/2 -self.button_continue.get_rect().height-10, self.button_newgame.get_rect().width, self.button_newgame.get_rect().height)
        self.continue_rect = pygame.Rect(window.width/2 - self.button_continue.get_rect().width/2, window.height/2 - self.button_continue.get_rect().height/2, self.button_continue.get_rect().width, self.button_continue.get_rect().height)
        self.quit_rect = pygame.Rect(window.width/2 - self.button_quit.get_rect().width/2, window.height/2 - self.button_quit.get_rect().height/2 +self.button_continue.get_rect().height+10, self.button_quit.get_rect().width, self.button_quit.get_rect().height) 
        
        # Mouse
        window.screen.blit(self.mouse, pygame.mouse.get_pos())

        # Check for clicks
        game_running, level_selection = self.menu_button_events(window)
        return game_running, level_selection

    def menu_button_events(self, window: Window) -> Tuple[bool, int]:
        """ Checks for mouse clicks on the menu buttons.

        Args:
            window: The window to check for clicks on

        Returns:
            A tuple containing the game state and the level selection
        """
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()            
            elif event.type == pygame.KEYDOWN:
                if pygame.K_ESCAPE:
                    sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # New Game
                if self.new_game_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.Sound.stop(self.menusound)
                    # Load level 1 when new game is clicked
                    level_selection = 1
                    # Set game state to running: Game running = True
                    return True, level_selection

                # Continue    
                if self.continue_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.Sound.stop(self.menusound)
                    # Read from last save file
                    level_selection = 2
                    # Set game state to running: Game running = True
                    return True, level_selection
                # Quit    
                if self.quit_rect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()
        return False, 0