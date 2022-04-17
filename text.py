import pygame
from typing import List
from window import Window

class Text:
    """ Handles all on screen texts."""

    def __init__(self, window: Window):        
        self.window = window

    def copy_text(self, msgs: List):
        """ Copy text in the middle of the screen """

        copy_colour = (239, 255, 135)
        copy_font = pygame.font.Font("assets/_FONTS/share_tech_mono.ttf", 25)
        copy_bg = (9, 0, 21)
        
        for i, msg in enumerate(msgs):
            copy_msg_img = copy_font.render(msg, True, copy_colour, copy_bg)
            copy_msg_rect = copy_msg_img.get_rect()
            yi = i - 0.5 * len(msgs)
            y = yi * copy_msg_rect.height + 20 
            copy_msg_rect.center = self.window.width//2, self.window.height//2 + y
            self.window.screen.blit(copy_msg_img, copy_msg_rect)