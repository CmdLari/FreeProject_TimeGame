import pygame
import sys

# Import own files
from screen_map1 import Map1

class Menu:
    '''Draws the menu'''

    def __init__(self):

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
    
    def show_menu(self, settings_background, utility_saves):
        '''Draws menu'''

        self.settings_background = settings_background

        # Background
        self.settings_background.blit_img(self.menubackground, 0, 0)

        # Buttons
        self.settings_background.blit_img(self.button_newgame, 0, -self.button_continue.get_rect().height-10)
        self.settings_background.blit_img(self.button_continue, 0, 0)
        self.settings_background.blit_img(self.button_quit, 0, self.button_continue.get_rect().height+10)

        self.new_game_rect = pygame.Rect(self.settings_background.width/2 - self.button_newgame.get_rect().width/2, self.settings_background.height/2 - self.button_newgame.get_rect().height/2 -self.button_continue.get_rect().height-10, self.button_newgame.get_rect().width, self.button_newgame.get_rect().height)
        self.continue_rect = pygame.Rect(self.settings_background.width/2 - self.button_continue.get_rect().width/2, self.settings_background.height/2 - self.button_continue.get_rect().height/2, self.button_continue.get_rect().width, self.button_continue.get_rect().height)
        self.quit_rect = pygame.Rect(self.settings_background.width/2 - self.button_quit.get_rect().width/2, self.settings_background.height/2 - self.button_quit.get_rect().height/2 +self.button_continue.get_rect().height+10, self.button_quit.get_rect().width, self.button_quit.get_rect().height) 
        
        # Mouse
        self.settings_background.screen.blit(self.mouse, pygame.mouse.get_pos())

        # Check for clicks
        menu = self.menu_button_events(utility_saves, settings_background)
        return menu

    def menu_button_events(self, utility_saves, settings_background):
        '''Checks for button usage'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()            
            elif event.type == pygame.KEYDOWN:
                if pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # NEW GAME
                if self.new_game_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.Sound.stop(self.menusound)
                    map = self.new_game(utility_saves)
                    self.load_level(map, settings_background)
                    return map
                # CONTINUE GAME
                if self.continue_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.Sound.stop(self.menusound)
                    self.continue_game(utility_saves)
                    return map
                # QUIT
                if self.quit_rect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()
                   
    def new_game(self, utility_saves):
        '''Clears save game'''
        self.sanity = 20
        utility_saves.write_to_save("player_sanity", self.sanity, "0_save.json")
        self.love = 0
        utility_saves.write_to_save("player_love", self.love, "0_save.json")        
        self.rationality = 0
        utility_saves.write_to_save("player_rationality", self.rationality, "0_save.json")        
        self.health = 20
        utility_saves.write_to_save("player_health", self.health, "0_save.json")      
        self.inv01 = "-"
        utility_saves.write_to_save("inv_1", self.inv01, "0_save.json")         
        self.inv02 = "-"
        utility_saves.write_to_save("inv_2", self.inv02, "0_save.json")         
        self.inv03 = "-"
        utility_saves.write_to_save("inv_3", self.inv03, "0_save.json")         
        self.inv04 = "-"
        utility_saves.write_to_save("inv_4", self.inv04, "0_save.json")         
        self.inv05 = "-"
        utility_saves.write_to_save("inv_5", self.inv05, "0_save.json")         
        self.inv06 = "-"
        utility_saves.write_to_save("inv_6", self.inv06, "0_save.json")         
        self.inv07 = "-"
        utility_saves.write_to_save("inv_7", self.inv07, "0_save.json")         
        self.inv08 = "-"
        utility_saves.write_to_save("inv_8", self.inv08, "0_save.json")     
        self.inv09 = "-"
        utility_saves.write_to_save("inv_9", self.inv09, "0_save.json")         
        self.inv10 = "-"
        utility_saves.write_to_save("inv_10", self.inv10, "0_save.json")     
        return 1

    def continue_game(self, utility_saves):
        '''Loads save game'''
        self.map = utility_saves.read_from_save("map", "0_save.json")
        self.sanity = utility_saves.read_from_save("player_sanity", "0_save.json")
        self.love = utility_saves.read_from_save("player_love", "0_save.json")        
        self.rationality = utility_saves.read_from_save("player_rationality", "0_save.json")        
        self.health = utility_saves.read_from_save("player_health", "0_save.json")      
        self.inv01 = utility_saves.read_from_save("inv_1", "0_save.json")         
        self.inv02 = utility_saves.read_from_save("inv_2", "0_save.json")         
        self.inv03 = utility_saves.read_from_save("inv_3", "0_save.json")         
        self.inv04 = utility_saves.read_from_save("inv_4", "0_save.json")         
        self.inv05 = utility_saves.read_from_save("inv_5", "0_save.json")         
        self.inv06 = utility_saves.read_from_save("inv_6", "0_save.json")         
        self.inv07 = utility_saves.read_from_save("inv_7", "0_save.json")         
        self.inv08 = utility_saves.read_from_save("inv_8", "0_save.json")     
        self.inv09 = utility_saves.read_from_save("inv_9", "0_save.json")         
        self.inv10 = utility_saves.read_from_save("inv_10", "0_save.json")
        return self.    

    def load_level(self, map, settings_background):
        if map == 1:
            map1 = Map1()
            map1.show_map1(settings_background)