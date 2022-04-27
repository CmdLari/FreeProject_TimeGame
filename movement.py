import sys
import pygame

class Movement:

    def __init__(self, screen):
        """Handles movement and displacement"""
        
        self.mapy = 0
        self.mapx = 0

        self.moving = 0

        self.playerimg_up = ["_assets/IMGS/player_up.png", "_assets/IMGS/player_upb.png"]
        self.playerimg_down = ["_assets/IMGS/player_down.png", "_assets/IMGS/player_downb.png"]
        self.playerimg_left = ["_assets/IMGS/player_left.png", "_assets/IMGS/player_leftb.png"]
        self.playerimg_right = ["_assets/IMGS/player_right.png", "_assets/IMGS/player_rightb.png"]             


        self.playerimg =  self.playerimg_up

    def movement(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if self.mapy <= 1590:
                        self.mapy += 5
                        self.playerimg = self.playerimg_up
                        return self.playerimg

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if self.mapy >= -1590:
                        self.mapy -= 5
                        self.playerimg = self.playerimg_down
                        return self.playerimg

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if self.mapx <= 2865:
                        self.mapx += 5
                        self.playerimg = self.playerimg_left
                        return self.playerimg

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if self.mapx >= -2865:
                        self.mapx -= 5     
                        self.playerimg = self.playerimg_right
                        return self.playerimg

                elif event.key == pygame.K_ESCAPE:
                    sys.exit()

                else:
                    self.playerimg = self.playerimg_up
                    return self.playerimg

    def get_position(self):
        return self.mapx, self.mapy
