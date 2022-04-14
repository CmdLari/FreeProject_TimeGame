# Import Libraries
import imp
import pygame
import json
import sys
from time import sleep

# Import own files
from vis_background import Background
from set_player import LEFT, RIGHT, UP, DOWN, Player
from lvl_level1 import Level1
from lvl_level2 import Level2
from ut_utils import Utils
from ut_new_game import NewGame
from set_inventory import Inventory
from vis_screeninfo import Screeninfo

# This is a change

class Timegame:
    '''Manages the game'''

    def __init__(self):
        '''Initialize game, create resources'''
        pygame.init()

        self.clock = pygame.time.Clock()

        # rename imported files
        self.bg = Background()
        self.player = Player()
        self.lvl1 = Level1()
        self.lvl2 = Level2()
        self.new_game = NewGame()
        self.inventory = Inventory()
        self.screen_info = Screeninfo()

        self.playerstats_file = "0-playerstate.json"

        # Initialize screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height

        # Movement Variables
        player_state_file = open("0-playerstate.json")
        json_data = json.load(player_state_file)
        self.mov_x = json_data["mov_x"]
        self.mov_y = json_data["mov_y"]
        self.map_x = json_data["map_x"]
        self.map_y = json_data["map_y"]            

        # Player Stats
        player_state_file = open("0-playerstate.json")
        json_data = json.load(player_state_file)
        
        self.player_lvl = json_data["player_level"]
        self.sanity = json_data["player_sanity"]
        self.love = json_data["player_love"]
        self.rationality = json_data["player_rationality"]
        self.health = json_data["player_health"]

        # Music
        if self.player_lvl == 1:
            self.ingame_music = pygame.mixer.Sound('_MUS/timegame_lvl1.mp3')
        if self.player_lvl == 2:
            self.ingame_music = pygame.mixer.Sound('_MUS/timegame_lvl1.mp3')

              
    def run_game(self):
        '''Main loop for the game'''

        pygame.key.set_repeat(int(10))

        self.game_run_active = False
        self.infoscreen = False

        if self.game_run_active == False:
            self.menusound = pygame.mixer.Sound('_MUS/timegame_menu.mp3')
            self.menusound.set_volume(0.5)
            pygame.mixer.Sound.play(self.menusound, loops=-1)

        while True:

            self.clock.tick(120)

            self.bg.menu_screen()
            self.draw_menu_buttons()
            self.draw_mouse()
            self.check_menu_buttons()

            if self.game_run_active == True:
                pygame.mouse.set_visible(False)
                self.check_player_lvl()
                self.bg.background()
                self.check_events()
                self.draw_lvl()
                self.drawplayer()
                self.screen_info.screentext()
                self.screeninfo()
                self.inventory.inventorytext()

            pygame.display.flip()

    def draw_mouse(self):
        '''Draw mouse to screen'''
        pygame.mouse.set_visible(False)

        self.mouse_img = pygame.image.load('_IMGS/mouse.png')
        self.mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(self.mouse_img, self.mouse_pos)
        self.mouse_rect = self.mouse_img.get_rect()

    def check_menu_buttons(self):
        '''Checks for clicks on menu buttons'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # New Game
                if self.ng_rect.collidepoint(pygame.mouse.get_pos()):      
                    self.new_game.restart()         
                    pygame.mixer.Sound.stop(self.menusound)
                    self.game_run_active = True
                    pygame.mixer.Sound.play(self.ingame_music, loops=-1)                        

                
                # Continue
                elif self.cont_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.Sound.stop(self.menusound)                    
                    self.game_run_active = True
                    pygame.mixer.Sound.play(self.ingame_music, loops=-1)                        
                
                # Quit
                elif self.quit_rect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()

    def check_events(self):
        '''Checks for key and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event):
        '''Respond to keypresses'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if event.type == pygame.KEYDOWN:

            # Quit
            if event.key == pygame.K_ESCAPE:
                sys.exit()

            # Movement 
            
            # --Left
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.player.direction = LEFT
                if self.bg.bg_rect_x <= self.bg.screen.get_rect().x:
                    self.mov_x += 5
                    Utils.write_to_playerstate("mov_x", self.mov_x, self.playerstats_file)
                    self.mov_x = Utils.read_from_playerstate("mov_x", self.playerstats_file)
                    self.map_x = self.bg.bg.get_rect().x+self.mov_x
                    Utils.write_to_playerstate("map_x", self.map_x, self.playerstats_file)
            
            # --Right
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT: 
                self.player.direction = RIGHT
                if self.bg.bg_rect_x >= self.bg.screen.get_rect().x - self.bg.screen.get_rect().width*3:
                    self.mov_x -= 5
                    Utils.write_to_playerstate("mov_x", self.mov_x, self.playerstats_file)
                    self.mov_x = Utils.read_from_playerstate("mov_x", self.playerstats_file)
                    self.map_x = self.bg.bg.get_rect().x+self.mov_x
                    Utils.write_to_playerstate("map_x", self.map_x, self.playerstats_file)

            # --Up
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                self.player.direction = UP
                if self.bg.bg_rect_y <= self.bg.screen.get_rect().y:
                    self.mov_y += 5
                    Utils.write_to_playerstate("mov_y", self.mov_y, self.playerstats_file)
                    self.mov_y = Utils.read_from_playerstate("mov_y", self.playerstats_file)
                    self.map_y = self.bg.bg.get_rect().y+self.mov_y
                    Utils.write_to_playerstate("map_y", self.map_y, self.playerstats_file)
            
            # --Down
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.player.direction = DOWN
                if self.bg.bg_rect_y >= self.bg.screen.get_rect().y - self.bg.screen.get_rect().height*3:
                    self.mov_y -= 5
                    Utils.write_to_playerstate("mov_y", self.mov_y, self.playerstats_file)
                    self.mov_y = Utils.read_from_playerstate("mov_y", self.playerstats_file)
                    self.map_y = self.bg.bg.get_rect().y+self.mov_y
                    Utils.write_to_playerstate("map_y", self.map_y, self.playerstats_file)

            # Return to menu
            elif event.key == pygame.K_r:
                pygame.mixer.Sound.stop(self.ingame_music)
                self.game_run_active = False
                pygame.mixer.Sound.play(self.menusound, loops=-1)

            # Journal
            elif event.key == pygame.K_j:
                self.bg.journal()

            # Inventory Info
            elif event.key == pygame.K_0:
                self.inventory.invpos_key = 0
                self.inventory.inventory_msg()
            elif event.key == pygame.K_1:
                self.inventory.invpos_key = 1
                self.inventory.inventory_msg()
            elif event.key == pygame.K_2:
                self.inventory.invpos_key = 2
                self.inventory.inventory_msg()             
            elif event.key == pygame.K_3:
                self.inventory.invpos_key = 3
                self.inventory.inventory_msg()
            elif event.key == pygame.K_4:
                self.inventory.invpos_key = 4
                self.inventory.inventory_msg()
            elif event.key == pygame.K_5:
                self.inventory.invpos_key = 5
                self.inventory.inventory_msg()
            elif event.key == pygame.K_6:
                self.inventory.invpos_key = 6
                self.inventory.inventory_msg()
            elif event.key == pygame.K_7:
                self.inventory.invpos_key = 7
                self.inventory.inventory_msg()
            elif event.key == pygame.K_8:
                self.inventory.invpos_key = 8
                self.inventory.inventory_msg()
            elif event.key == pygame.K_9:
                self.inventory.invpos_key = 9
                self.inventory.inventory_msg()

    def screeninfo(self):
        '''Display control bindings'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                # Info-Screen
                if event.key == pygame.K_h:
                    self.infoscreen = True
                elif event.key == pygame.K_g:
                    self.infoscreen = False
        if self.infoscreen == True:    
            self.screen_info.screentext()

    def draw_menu_buttons(self):
        '''Initialize menu buttons'''
        # Continue
        self.cont_button = pygame.image.load("_IMGS/continue.png")
        self.cont_rect_w = self.cont_button.get_rect().width
        self.cont_rect_h = self.cont_button.get_rect().height
        self.cont_rect = pygame.Rect((self.bg.width//2-self.cont_rect_w//2, self.bg.height//2-self.cont_rect_h//2 - self.cont_rect_h//2),(self.cont_rect_w, self.cont_rect_h))
        self.bg.screen.blit(self.cont_button, (self.bg.width//2-self.cont_rect_w//2, self.bg.height//2-self.cont_rect_h//2))

        # New Game
        self.ng_button = pygame.image.load("_IMGS/new_game.png")
        self.ng_w = self.ng_button.get_rect().width
        self.ng_h = self.ng_button.get_rect().height
        self.ng_rect = pygame.Rect((self.bg.width//2-self.ng_w//2, self.bg.height//2-self.ng_h//2 - self.cont_rect_h - 20),(self.ng_w, self.ng_h))
        self.bg.screen.blit(self.ng_button, (self.bg.width//2-self.ng_w//2, self.bg.height//2-self.ng_h//2 - self.cont_rect_h - 20))

        # Quit
        self.quit_button = pygame.image.load("_IMGS/quit.png")
        self.quit_w = self.quit_button.get_rect().width
        self.quit_h = self.quit_button.get_rect().height
        self.quit_rect = pygame.Rect((self.bg.width//2-self.quit_w//2, self.bg.height//2-self.quit_h//2 + self.cont_rect_h + 20),(self.quit_w, self.quit_h))
        self.bg.screen.blit(self.quit_button, (self.bg.width//2-self.quit_w//2, self.bg.height//2-self.quit_h//2 + self.cont_rect_h + 20))

    def drawplayer(self):
        '''Draws the player to the map'''
        self.player.playerblit()
        

    def check_player_lvl(self):
        '''Checks for player level and sets map'''
        if self.player_lvl == 1:
            self.bglvl1 = pygame.image.load('_IMGS/_lvl1/map_lvl1.png')
            self.bg.bg = self.bglvl1
            pygame.mixer.Sound.stop(self.menusound)

        elif self.player_lvl == 2:
            self.bglvl2 = pygame.image.load('_IMGS/_lvl2/map_lvl2.png')
            self.bg.bg = self.bglvl2
            pygame.mixer.Sound.stop(self.menusound)

    def draw_lvl(self):
        '''Initializes lvl assets'''
        if self.player_lvl == 1:
            self.lvl1.backgroundlvl1_assets()
        elif self.player_lvl == 2:
            self.lvl2.backgroundlvl2_assets()

if __name__ == '__main__':
    # Make a game instance and run the game
    tg = Timegame()
    tg.run_game()