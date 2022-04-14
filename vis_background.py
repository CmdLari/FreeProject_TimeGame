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
        

    def screentext(self):
        '''Displays information on screen'''
        self.help_msg = "[H] HELP"
        self.help_msg_img = self.textfont.render(self.help_msg, True, self.textcolour)
        self.help_msg_img_rect = self.help_msg_img.get_rect()
        self.help_msg_img_rect.center = self.screen.get_rect().width -self.help_msg_img_rect.width -40, 40
        self.screen.blit(self.help_msg_img, self.help_msg_img_rect)

        # Player health
        if self.health >= 81 and self.health <= 100:
            self.health_msg = "♥♥♥♥♥"

        elif self.health >= 61 and self.health <= 80:
            self.health_msg = "♥♥♥♥"

        elif self.health >= 41 and self.health <= 60:
            self.health_msg = "♥♥♥"

        elif self.health >= 21 and self.health <= 40:
            self.health_msg = "♥♥"

        elif self.health >= 1 and self.health <= 20:
            self.health_msg = "♥"

        self.health_msg_img = self.textfont.render(self.health_msg, True, self.textcolour_health)
        self.health_msg_img_rect = self.health_msg_img.get_rect()
        self.health_msg_img_rect.center = self.screen.get_rect().width//2, 40
        self.screen.blit(self.health_msg_img, self.health_msg_img_rect)

    def info_screen(self):
        '''Displays info page'''
      
        # [ESC]
        self.esc_msg = " [ESC] to quit the game "
        self.esc_msg_img = self.textfont_copy.render(self.esc_msg, True, self.textcolour, self.textbg)
        self.esc_msg_img_rect = self.esc_msg_img.get_rect()
        self.esc_msg_img_rect.center = self.screen.get_rect().width//2, self.screen.get_rect().height/2
        self.screen.blit(self.esc_msg_img, self.esc_msg_img_rect)

        # [G]
        self.g_msg = " [G] to close this screen "
        self.g_msg_img = self.textfont_copy.render(self.g_msg, True, self.textcolour, self.textbg)
        self.g_msg_img_rect = self.g_msg_img.get_rect()
        self.g_msg_img_rect.center = self.screen.get_rect().width//2, self.screen.get_rect().height/2 - self.g_msg_img_rect.height - 15
        self.screen.blit(self.g_msg_img, self.g_msg_img_rect)

        # [R]
        self.r_msg = " [R] to return to the game menu "
        self.r_msg_img = self.textfont_copy.render(self.r_msg, True, self.textcolour, self.textbg)
        self.r_msg_img_rect = self.r_msg_img.get_rect()
        self.r_msg_img_rect.center = self.screen.get_rect().width//2, self.screen.get_rect().height/2 + self.r_msg_img_rect.height + 15
        self.screen.blit(self.r_msg_img, self.r_msg_img_rect)

        # [Movement]
        self.mov_msg = " [WASD or the ARROW KEYS] to move "
        self.mov_msg_img = self.textfont_copy.render(self.mov_msg, True, self.textcolour, self.textbg)
        self.mov_msg_img_rect = self.mov_msg_img.get_rect()
        self.mov_msg_img_rect.center = self.screen.get_rect().width//2, self.screen.get_rect().height/2 + self.mov_msg_img_rect.height*2 + 30
        self.screen.blit(self.mov_msg_img, self.mov_msg_img_rect)

        # [Inventory]
        self.inv_msg = " [1]-[0] to view info about items in your inventory "
        self.inv_msg_img = self.textfont_copy.render(self.inv_msg, True, self.textcolour, self.textbg)
        self.inv_msg_img_rect = self.inv_msg_img.get_rect()
        self.inv_msg_img_rect.center = self.screen.get_rect().width//2, self.screen.get_rect().height/2 + self.inv_msg_img_rect.height*2 + 30
        self.screen.blit(self.inv_msg_img, self.inv_msg_img_rect)

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
