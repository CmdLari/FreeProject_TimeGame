# Import Libraries
import imp
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

        self.playerstats_file = "playerstate.json"

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

         # Assets

        self.portal = pygame.image.load('_IMGS/_Lvl1/portallvl1.png')
    
        # Variables to make sure assets have the upper left corner of the background as a basis

        self.placement_adj_x = self.bg.width//2 - self.bg.bg.get_rect().width//2
        self.placement_adj_y = self.bg.height//2 - self.bg.bg.get_rect().height//2

    def backgroundlvl1_assets(self):
        '''Initializes lvl 1 map assets'''

        # Movement Variables
        player_state_file = open("playerstate.json")
        json_data = json.load(player_state_file)
        self.map_x = json_data["map_x"]
        self.map_y = json_data["map_y"]

        # Portal
        self.portal_x = self.placement_adj_x + 3556 + self.map_x
        self.portal_y = self.placement_adj_y + 1941 + self.map_y
        self.portal_width = self.portal.get_rect().width
        self.portal_height = self.portal.get_rect().height
        
        # Draw Portal to screen
        self.bg.screen.blit(self.portal, (self.portal_x, self.portal_y))

        self.portal_curr_rect = pygame.Rect(self.portal_x, self.portal_y, self.portal_width , self.portal_height)
        if self.portal_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2):
            self.player_lvl = 2
            Utils.write_to_playerstate("player_level", self.player_lvl,self.playerstats_file)  
            print("hi stupid")   

            




