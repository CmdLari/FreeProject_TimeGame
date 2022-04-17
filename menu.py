from typing import Tuple
from camera_group import CameraGroup
from window import Window
import pygame
import sys

from level import Level

class Menu:
    '''Draws the menu'''

    def __init__(self):
        """Initialize the menu"""

        # Assets Menu
        # -- Background
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
        '''Draws menu'''
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
        '''Checks for button usage'''
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
                    # self.new_game(utility_saves)
                    level_selection = 1
                    # Set game state to running: Game running = True
                    return True, level_selection

                # Continue    
                if self.continue_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.Sound.stop(self.menusound)
                    level_selection = 2
                    # self.continue_game(utility_saves)
                    #self.level = 1
                    # Set game state to running: Game running = True
                    return True, level_selection
                # Quit    
                if self.quit_rect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()
        return False, 0

        

    # def new_game(self, utility_saves):
    #     '''Clears save game'''
    #     self.level = 1
    #     utility_saves.write_to_save("level", self.level, "0_save.json")
    #     self.sanity = 20
    #     utility_saves.write_to_save("player_sanity", self.sanity, "0_save.json")
    #     self.love = 0
    #     utility_saves.write_to_save("player_love", self.love, "0_save.json")        
    #     self.rationality = 0
    #     utility_saves.write_to_save("player_rationality", self.rationality, "0_save.json")        
    #     self.health = 20
    #     utility_saves.write_to_save("player_health", self.health, "0_save.json")      
    #     self.inv01 = "-"
    #     utility_saves.write_to_save("inv_1", self.inv01, "0_save.json")         
    #     self.inv02 = "-"
    #     utility_saves.write_to_save("inv_2", self.inv02, "0_save.json")         
    #     self.inv03 = "-"
    #     utility_saves.write_to_save("inv_3", self.inv03, "0_save.json")         
    #     self.inv04 = "-"
    #     utility_saves.write_to_save("inv_4", self.inv04, "0_save.json")         
    #     self.inv05 = "-"
    #     utility_saves.write_to_save("inv_5", self.inv05, "0_save.json")         
    #     self.inv06 = "-"
    #     utility_saves.write_to_save("inv_6", self.inv06, "0_save.json")         
    #     self.inv07 = "-"
    #     utility_saves.write_to_save("inv_7", self.inv07, "0_save.json")         
    #     self.inv08 = "-"
    #     utility_saves.write_to_save("inv_8", self.inv08, "0_save.json")     
    #     self.inv09 = "-"
    #     utility_saves.write_to_save("inv_9", self.inv09, "0_save.json")         
    #     self.inv10 = "-"
    #     utility_saves.write_to_save("inv_10", self.inv10, "0_save.json")     

    # def continue_game(self, utility_saves):
    #     '''Loads save game'''
    #     self.level = utility_saves.read_from_save("level", "0_save.json")
    #     self.sanity = utility_saves.write_to_save("player_sanity", "0_save.json")
    #     self.love = utility_saves.write_to_save("player_love", "0_save.json")        
    #     self.rationality = utility_saves.write_to_save("player_rationality", "0_save.json")        
    #     self.health = utility_saves.write_to_save("player_health", "0_save.json")      
    #     self.inv01 = utility_saves.write_to_save("inv_1", "0_save.json")         
    #     self.inv02 = utility_saves.write_to_save("inv_2", "0_save.json")         
    #     self.inv03 = utility_saves.write_to_save("inv_3", "0_save.json")         
    #     self.inv04 = utility_saves.write_to_save("inv_4", "0_save.json")         
    #     self.inv05 = utility_saves.write_to_save("inv_5", "0_save.json")         
    #     self.inv06 = utility_saves.write_to_save("inv_6", "0_save.json")         
    #     self.inv07 = utility_saves.write_to_save("inv_7", "0_save.json")         
    #     self.inv08 = utility_saves.write_to_save("inv_8", "0_save.json")     
    #     self.inv09 = utility_saves.write_to_save("inv_9", "0_save.json")         
    #     self.inv10 = utility_saves.write_to_save("inv_10", "0_save.json")    