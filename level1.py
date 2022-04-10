# Import Libraries
import imp
import pygame
import json

# Import own files
from background import Background

class Level1:
    '''Manages the 1st level'''

    def __init__(self):
        self.bg = Background()

         # Assets

        self.portal = pygame.image.load('_IMGS/_Lvl1/portallvl1.png')
    
    def backgroundlvl1_assets(self):
        '''Initializes lvl 1 map assets'''

       # Movement Variables
        player_state_file = open("playerstate.json")
        json_data = json.load(player_state_file)
        self.map_x = json_data["map_x"]
        self.map_y = json_data["map_y"]

        self.bg.screen.blit(self.portal, (1225+self.map_x, 985+self.map_y))
        