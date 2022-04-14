import pygame
import json

# Import own classes
from vis_background import Background

class Screeninfo:
    '''Manages any information appearing on screen that's not lvl specific'''
    def __init__(self):

        # Rename imports
        self.background = Background()

        # Variables in case of movement
        self.ix = 0
        self.iy = 0

        player_state_file = open("0-playerstate.json")
        json_data = json.load(player_state_file)
        self.mov_x = json_data["mov_x"]
        self.mov_y = json_data["mov_y"]

        self.health = json_data["player_health"]

        # Text Vars
        self.textcolour = (200, 252, 255)
        self.textcolour_health = (255, 15, 111)
        self.textfont = pygame.font.Font("0-font_press_start2p.ttf", 15)
        self.textfont_copy = pygame.font.Font("0-font_share_tech_mono.ttf", 25)
        self.textbg = (31, 13, 0)

    def screentext(self):
        '''Displays information on screen'''
        self.help_msg = "[H] HELP"
        self.help_msg_img = self.textfont.render(self.help_msg, True, self.textcolour)
        self.help_msg_img_rect = self.help_msg_img.get_rect()
        self.help_msg_img_rect.center = self.background.screen.get_rect().width -self.help_msg_img_rect.width -40, 40
        self.background.screen.blit(self.help_msg_img, self.help_msg_img_rect)

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
        self.health_msg_img_rect.center = self.background.screen.get_rect().width//2, 40
        self.background.screen.blit(self.health_msg_img, self.health_msg_img_rect)