# Import Libraries
import pygame
import json

# Import own files
from player import Player

class Background:
    '''Manages all backgrounds'''
    def __init__(self):

        self.player = Player()

        # Variables in case of movement
        self.ix = 0
        self.iy = 0

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height
        pygame.display.set_caption("Time Game")

        self.bg = pygame.image.load('_IMGS/map_blank.png')
        
    def background(self):
        '''Blank Background to be replaced'''
        self.bg_rect_x = (self.width//2 - self.bg.get_rect().width//2 +self.ix)
        self.bg_rect_y = (self.height//2 - self.bg.get_rect().height//2 +self.iy)
        self.bg_rect = (self.bg_rect_x, self.bg_rect_y)
        self.screen.blit(self.bg, self.bg_rect)
        

    def screentext(self):
        '''Displays information on screen'''
        self.help = pygame.image.load('_IMGS/_screeninfo/press_h.png')
        self.screen.blit(self.help, (self.width - self.help.get_rect().width- 20, 0 +20))

    def info_screen(self):
        '''Displays info page'''
        self.info = pygame.image.load('_IMGS/_screeninfo/help_info.png')
        self.screen.blit(self.info, (self.width//2 - self.info.get_rect().width//2, self.height//2 - self.info.get_rect().height//2))

    def menu_screen(self):
        '''Initializes a menu'''
        self.menu_img = pygame.image.load('_IMGS/menu.png')
        self.menu_img = pygame.transform.scale(self.menu_img,(self.width, self.height))
        self.screen.blit(self.menu_img,(0,0))

    def journal(self):
        '''Handles the journal / memory'''

        # Draw Journal background
        self.jl_info = pygame.image.load('_IMGS/_screeninfo/journal.png')
        self.screen.blit(self.jl_info, (self.width//2 - self.jl_info.get_rect().width//2, self.height//2 - self.jl_info.get_rect().height//2))
