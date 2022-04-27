import pygame

from movement import Movement
from player import Player
from sprite import Sprite

class Level1:
    """Describes level 1"""
    
    def __init__(self, screen, texts):
        """Handles Lvl1"""
        # Initialize
        self.screen = screen
        self.texts = texts
        self.movement = Movement(screen)
        self.player = Player(screen)
        self.sprite = Sprite(screen, texts)

        # Load music
        self.levelmusic = pygame.mixer.Sound("_assets/MUS/goinghome_lvl1.mp3")

        # Load images
        self.backgroundimg = pygame.image.load("_assets/IMGS/lvl1/lvl1_bg.jpg")
        self.ship = pygame.image.load("_assets/IMGs/lvl1/ship.png")   
        self.dino_a = pygame.image.load("_assets/IMGs/lvl1/dinoa.png")   
        self.dino_b = pygame.image.load("_assets/IMGs/lvl1/dinoa.png")        
        self.dino_c = pygame.image.load("_assets/IMGs/lvl1/dinoa.png")

        # Describe player
        self.level = self.player.level
        self.health = self.player.health
        self.sanity = self.player.sanity
        self.rationality = self.player.rationality
        self.love = self.player.love
        self.Inv1 = self.player.Inv1
        self.Inv2 = self.player.Inv2
        self.Inv3 = self.player.Inv3
        self.Inv4 = self.player.Inv4
        self.Inv5 = self.player.Inv5
        self.Inv6 = self.player.Inv6
        self.Inv7 = self.player.Inv7
        self.Inv8 = self.player.Inv8
        self.Inv9 = self.player.Inv9
        self.Inv10 = self.player.Inv10 

    def lvl_1(self):
        """Draws lvl1"""

        self.movement.movement()

        # Check for movement
        mapx, mapy = self.movement.get_position()

        # Blit map to screen
        self.backgroundrect = self.backgroundimg.get_rect()   
        self.backgroundrect.center = self.screen.width/2 + mapx, self.screen.height/2 + mapy
        self.screen.screen.blit(self.backgroundimg, self.backgroundrect)

        # Blit Ship to screen
        msgs = ["This debris is all what remains of a vessel.","Did I arrive in this?", "Maybe I should look for any intact items!"]
        self.sprite.draw_sprite(self.ship, mapx, mapy, 210, -200, msgs)

        # Blit Dinos to screen
        msgs_dino = ["This dinosaur seems aggressive!","I can't defend myself...", "I need to flee!"]
        self.sprite.draw_animated_sprite(self.dino_a, mapx, mapy, -3052, -1058, msgs_dino)
        self.sprite.draw_animated_sprite(self.dino_c, mapx, mapy, -878, -1541, msgs_dino)
        self.sprite.draw_animated_sprite(self.dino_b, mapx, mapy, -817, -305, msgs_dino)
        self.sprite.draw_animated_sprite(self.dino_b, mapx, mapy, 1765, -1312, msgs_dino)
        self.sprite.draw_animated_sprite(self.dino_c, mapx, mapy, 2283, 288, msgs_dino)
        self.sprite.draw_animated_sprite(self.dino_b, mapx, mapy, 1763, 1312, msgs_dino)
        self.sprite.draw_animated_sprite(self.dino_c, mapx, mapy, -2386, 328, msgs_dino)
        self.sprite.draw_animated_sprite(self.dino_a, mapx, mapy, 2883, -660, msgs_dino)
        self.sprite.draw_animated_sprite(self.dino_a, mapx, mapy, -387, 994, msgs_dino)
        self.sprite.draw_animated_sprite(self.dino_a, mapx, mapy, -2931, 1288, msgs_dino)

        # Blit player to screen
        self.player.draw_player()
