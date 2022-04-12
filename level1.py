# Import Libraries
import imp
from time import sleep
import pygame
import json

# Import own files
from background import Background
from player import Player
from utils import Utils

class Level1:
    '''Manages the 1st level'''

    def __init__(self):
        self.bg = Background()
        self.player = Player()

        # Movement Variables
        player_state_file = open("playerstate.json")
        json_data = json.load(player_state_file)
        self.mov_x = json_data["mov_x"]
        self.mov_y = json_data["mov_y"]
        self.map_x = json_data["map_x"]
        self.map_y = json_data["map_y"]            

        # Player Stats
        self.playerstats_file = "playerstate.json"
        
        player_state_file = open("playerstate.json")
        json_data = json.load(player_state_file)
        
        self.player_lvl = json_data["player_level"]
        self.sanity = json_data["player_sanity"]
        self.love = json_data["player_love"]
        self.rationality = json_data["player_rationality"]
        self.health = json_data["player_health"]

        # Text Vars
        self.textcolour = (200, 252, 255)
        self.textfont = pygame.font.SysFont(None, 30)
        self.textbg = (31, 13, 0)

         # Assets

        self.portal = pygame.image.load('_IMGS/_Lvl1/portallvl1.png')
        self.ship = pygame.image.load('_IMGS/spaceship.png')
        self.ship_state = True

        self.berries1 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries1b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries2 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries2b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries3 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries3b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries4 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries4b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries5 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries5b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries6 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries6b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries7 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries7b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries8 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries8b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries9 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries9b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries10 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries10b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
    
        # Variables to make sure assets have the upper left corner of the background as a basis

        self.placement_adj_x = self.bg.width//2 - self.bg.bg.get_rect().width//2
        self.placement_adj_y = self.bg.height//2 - self.bg.bg.get_rect().height//2

        self.ship_time = 600

    def backgroundlvl1_assets(self):
        '''Initializes lvl 1 map assets'''

        # Movement Variables
        player_state_file = open("playerstate.json")
        json_data = json.load(player_state_file)
        self.map_x = json_data["map_x"]
        self.map_y = json_data["map_y"]

        # Ship

        self.ship_x = self.placement_adj_x + 3707 + self.map_x
        self.ship_y = self.placement_adj_y + 1531 + self.map_y

        self.bg.screen.blit(self.ship, (self.ship_x, self.ship_y))

        self.ship_curr_rect = pygame.Rect(self.ship_x, self.ship_y, self.ship.get_rect().width, self.ship.get_rect().height)
        if self.ship_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.ship_state == True and self.ship_time >=0:
            self.ship_time -=1
            self.ship_msg = " This is what little debris remains of a crashed ship. Did I arrive in this? Maybe there are some clues left nearby? I should take a look around! "
            self.ship_msg_img = self.textfont.render(self.ship_msg, True, self.textcolour, self.textbg)
            self.ship_msg_img_rect = self.ship_msg_img.get_rect()
            self.ship_msg_img_rect.center = self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height/2+self.player.playerimg_up.get_rect().height
            self.bg.screen.blit(self.ship_msg_img, self.ship_msg_img_rect)

        # Portal
        self.portal_x = self.placement_adj_x + 3556 + self.map_x
        self.portal_y = self.placement_adj_y + 1941 + self.map_y
        self.portal_width = self.portal.get_rect().width
        self.portal_height = self.portal.get_rect().height
        
        self.bg.screen.blit(self.portal, (self.portal_x, self.portal_y))

        self.portal_curr_rect = pygame.Rect(self.portal_x, self.portal_y, self.portal_width , self.portal_height)
        if self.portal_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2):
            self.player_lvl = 1 #2
            Utils.write_to_playerstate("player_level", self.player_lvl,self.playerstats_file)  
            print("hi stupid")

        # Berries 1
        self.berries1_state = Utils.read_from_playerstate("berries1_state", self.playerstats_file)

        self.berries1_x = self.placement_adj_x + 3556 + self.map_x #4517
        self.berries1_y = self.placement_adj_y + 1941 + self.map_y #714

        if self.berries1_state == 1:
            self.bg.screen.blit(self.berries1, (self.berries1_x, self.berries1_y))
        else:
            self.bg.screen.blit(self.berries1b, (self.berries1_x, self.berries1_y))

        self.berries1_curr_rect = pygame.Rect(self.berries1_x, self.berries1_y, self.berries1.get_rect().width, self.berries1.get_rect().height)
        if self.berries1_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.berries1_state == 1:
            self.health += 5
            Utils.write_to_playerstate("player_health", self.health, self.playerstats_file)
            self.berries1_state = 2
            Utils.write_to_playerstate("berries1_state", self.berries1_state, self.playerstats_file)

        # Berries 2

        # Berries 3

        # Berries 4

        # Berries 5

        # Berries 6

        # Berries 7

        # Berries 8

        # Berries 9

        # Berries 10

        # Dino 1

        # Dino 2

        # Dino 3

        # Dino 4

        # Dino 5 

        # Dino 6

        # Dino 7

        # Dino 8

        # Dino 9

        # Dino 10

        # Memory 1

        # Memory 2

        # Memory 3

        # Memory 4

        # Memory 5

        # Memory 6

        # Memory 7

        # Memory 8

        # Memory 9

        # Memory 10


            




