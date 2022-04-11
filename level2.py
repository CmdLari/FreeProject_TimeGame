# Import Libraries
import imp
import pygame
import json

# Import own files
from background import Background

class Level2:
    '''Manages the 1st level'''

    def __init__(self):
        self.bg = Background()

         # Assets

        self.portal = pygame.image.load('_IMGS/_Lvl1/portallvl1.png')
    
        # Variables to make sure assets have the upper left corner of the background as a basis

        self.placement_adj_x = self.bg.width//2 - self.bg.bg.get_rect().width//2
        self.placement_adj_y = self.bg.height//2 - self.bg.bg.get_rect().height//2

    def backgroundlvl2_assets(self):
        '''Initializes lvl 1 map assets'''

       # Movement Variables
        player_state_file = open("playerstate.json")
        json_data = json.load(player_state_file)
        self.map_x = json_data["map_x"]
        self.map_y = json_data["map_y"]

        self.bg.screen.blit(self.portal, (self.placement_adj_x + 985 + self.map_x, self.placement_adj_y + 985 + self.map_y))        