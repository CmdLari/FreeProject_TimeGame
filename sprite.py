import pygame

from movement import Movement

class Sprite():
    def __init__(self, screen, texts):

        self.screen = screen
        self.texts = texts
        self.movement = Movement(screen)

    def draw_sprite(self, img, mapx, mapy, posx, posy, msgs):

        self.image = img
        self.rect  = self.image.get_rect()

        self.posx = posx
        self.posy = posy

        # Positioning the sprite
        self.rect.center = self.screen.width/2 + mapx + posx, self.screen.height/2 + mapy + posy

        # Drawing the sprite
        self.screen.screen.blit(self.image, self.rect)

        # Collision damage
        if pygame.Rect.collidepoint(self.rect,(self.screen.width/2, self.screen.height/2)):
            
            self.texts.center_msgs(msgs)

    def draw_animated_sprite(self, img, mapx, mapy, posx, posy, msgs):

        self.image = img
        self.rect  = self.image.get_rect()

        self.posx = posx
        self.posy = posy

        # Positioning the sprite
        self.rect.center = self.screen.width/2 + mapx + posx, self.screen.height/2 + mapy + posy

        # Drawing the sprite
        self.screen.screen.blit(self.image, self.rect)

        # Collision damage
        if pygame.Rect.collidepoint(self.rect,(self.screen.width/2, self.screen.height/2)):
                        
            self.texts.center_msgs(msgs)

            # self.health -= 10
            # self.sanity -= 5
            # return self.health, self.sanity
    