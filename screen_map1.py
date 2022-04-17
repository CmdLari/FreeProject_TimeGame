import pygame
import sys

class Map1:
    '''Draws the menu'''

    def __init__(self):
        self.number = 1
        self.levelbackground = pygame.image.load("_IMGS/_Lvl1/level1_bg.png")

    def show_map1(self, settings_background):
            '''Draws menu'''

            # Background
            settings_background.blit_img(self.levelbackground, 0, 0)
            print("i am here")



