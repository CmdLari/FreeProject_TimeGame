# Import Libraries
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

        self.bg.screen.blit(self.portal, (0+self.bg.ix, 0+self.bg.iy))