import pygame
from typing import List

class Texts:
    """Helps rendering texts to screen"""
    def __init__(self, screen):
        self.screen = screen



    def center_msgs(self, msgs: List):
        """Draws several lines centered to the screen (beneath player)"""
        
        copy_colour = (239, 255, 135)
        copy_font = pygame.font.Font("_assets/FONTS/share_tech_mono.ttf", 25)
        copy_bg = (9, 0, 21)

        for i, msg in enumerate(msgs):
            copy_msg_img = copy_font.render(msg, True, copy_colour, copy_bg)
            copy_msg_rect = copy_msg_img.get_rect()
            yi = i - 0.5 * len(msgs)
            y = yi * copy_msg_rect.height + 20 
            copy_msg_rect.center = self.screen.width//2, self.screen.height//2 + y + 120
            self.screen.screen.blit(copy_msg_img, copy_msg_rect)