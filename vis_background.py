# Import Libraries
import pygame
import json

class Background:
    '''Manages all backgrounds'''
    def __init__(self):

        # Variables in case of movement
        self.ix = 0
        self.iy = 0

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height
        pygame.display.set_caption("Time Game")

        self.bg = pygame.image.load('_IMGS/map_blank.png')

        # Text Vars
        self.textcolour = (200, 252, 255)
        self.textcolour_health = (255, 15, 111)
        self.textfont = pygame.font.Font("0-font_press_start2p.ttf", 15)
        self.textfont_copy = pygame.font.Font("0-font_share_tech_mono.ttf", 25)
        self.textbg = (31, 13, 0)
        
    def background(self):
        '''Blank Background to be replaced'''

        # Movement Variables
        player_state_file = open("0-playerstate.json")
        json_data = json.load(player_state_file)
        self.mov_x = json_data["mov_x"]
        self.mov_y = json_data["mov_y"]

        self.health = json_data["player_health"]

        self.bg_rect_x = (self.width//2 - self.bg.get_rect().width//2 +self.mov_x)
        self.bg_rect_y = (self.height//2 - self.bg.get_rect().height//2 +self.mov_y)
        self.bg_rect = (self.bg_rect_x, self.bg_rect_y)
        self.screen.blit(self.bg, self.bg_rect)
        
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
