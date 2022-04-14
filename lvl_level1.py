# Import Libraries
import imp
from time import sleep
import pygame
import json

# Import own files
from vis_background import Background
from set_player import Player
from ut_utils import Utils
from set_inventory import Inventory

class Level1:
    '''Manages the 1st level'''

    # Min | Start | Max Player stats
    # -- | 20 | 70 Health
    # -- | 50 | -- Sanity
    # -- | 00 | -- Love
    # -- | 00 | -- Rationality

    def __init__(self):
        self.bg = Background()
        self.player = Player()
        self.inventory = Inventory()

        # Movement Variables
        player_state_file = open("0-playerstate.json")
        json_data = json.load(player_state_file)
        self.mov_x = json_data["mov_x"]
        self.mov_y = json_data["mov_y"]
        self.map_x = json_data["map_x"]
        self.map_y = json_data["map_y"]            
      
        # Inventory
        self.inv1 = json_data["inv_1"]
        self.inv2 = json_data["inv_2"]
        self.inv3 = json_data["inv_3"]
        self.inv4 = json_data["inv_4"]
        self.inv5 = json_data["inv_5"]
        self.inv6 = json_data["inv_6"]
        self.inv7 = json_data["inv_7"]
        self.inv8 = json_data["inv_8"]
        self.inv9 = json_data["inv_9"]
        self.inv10 = json_data["inv_10"]

        self.inventorylist = [self.inv1, self.inv2, self.inv3, self.inv4, self.inv5, self.inv6, self.inv7, self.inv8, self.inv9, self.inv10]
        self.inventorylist_length = len(self.inventorylist)
        self.maxinv = 10

        # Player Stats
        self.playerstats_file = "0-playerstate.json"

        self.player_lvl = json_data["player_level"]
        self.sanity = json_data["player_sanity"]
        self.love = json_data["player_love"]
        self.rationality = json_data["player_rationality"]
        self.health = json_data["player_health"]

        # Text Vars
        self.textcolour = (200, 252, 255)
        self.textfont = pygame.font.Font("0-font_share_tech_mono.ttf", 25)
        self.textbg = (31, 13, 0)

         # Assets

        self.portal = pygame.image.load('_IMGS/_Lvl1/portallvl1.png')
        self.ship = pygame.image.load('_IMGS/spaceship.png')
        self.ship_state = True

        self.berries1 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries1b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries2 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries2b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries3 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries3b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries4 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries4b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries5 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries5b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries6 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries6b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries7 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries7b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries8 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries8b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries9 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries9b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')
        self.berries10 = pygame.image.load('_IMGS/_Lvl1/berries.png')
        self.berries10b = pygame.image.load('_IMGS/_Lvl1/berries_b.png')

        self.analyzer = pygame.image.load('_IMGS/_Lvl1/Item_Analyzer.png')
    
        # Variables to make sure assets have the upper left corner of the background as a basis

        self.placement_adj_x = self.bg.width//2 - self.bg.bg.get_rect().width//2
        self.placement_adj_y = self.bg.height//2 - self.bg.bg.get_rect().height//2

        self.ship_time = 600

    def backgroundlvl1_assets(self):
        '''Initializes lvl 1 map assets'''

        # Movement Variables
        player_state_file = open("0-playerstate.json")
        json_data = json.load(player_state_file)
        self.map_x = json_data["map_x"]
        self.map_y = json_data["map_y"]

        # Ship

        self.ship_x = self.placement_adj_x + 3707 + self.map_x
        self.ship_y = self.placement_adj_y + 1531 + self.map_y

        self.bg.screen.blit(self.ship, (self.ship_x, self.ship_y))

        self.ship_curr_rect = pygame.Rect(self.ship_x, self.ship_y, self.ship.get_rect().width, self.ship.get_rect().height)
        if self.ship_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.ship_state == True and self.ship_time >=0:
            self.ship_time -=1
            self.ship_msg1 = " This is what little debris remains of a crashed ship. "
            self.ship_msg1_img = self.textfont.render(self.ship_msg1, True, self.textcolour, self.textbg)
            self.ship_msg1_img_rect = self.ship_msg1_img.get_rect()
            self.ship_msg1_img_rect.center = self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height/2+self.player.playerimg_up.get_rect().height
            self.bg.screen.blit(self.ship_msg1_img, self.ship_msg1_img_rect)

            self.ship_msg2 = " Did I arrive in this? Maybe there are some clues left nearby? "
            self.ship_msg2_img = self.textfont.render(self.ship_msg2, True, self.textcolour, self.textbg)
            self.ship_msg2_img_rect = self.ship_msg2_img.get_rect()
            self.ship_msg2_img_rect.center = self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height/2+self.player.playerimg_up.get_rect().height + self.ship_msg2_img_rect.height + 10
            self.bg.screen.blit(self.ship_msg2_img, self.ship_msg2_img_rect)

            self.ship_msg3 = " I should take a look around! "
            self.ship_msg3_img = self.textfont.render(self.ship_msg3, True, self.textcolour, self.textbg)
            self.ship_msg3_img_rect = self.ship_msg3_img.get_rect()
            self.ship_msg3_img_rect.center = self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height/2+self.player.playerimg_up.get_rect().height + self.ship_msg3_img_rect.height*2 + 20
            self.bg.screen.blit(self.ship_msg3_img, self.ship_msg3_img_rect)

        # Portal
        self.portal_x = self.placement_adj_x + 3556 + self.map_x
        self.portal_y = self.placement_adj_y + 1941 + self.map_y
        self.portal_width = self.portal.get_rect().width
        self.portal_height = self.portal.get_rect().height
        
        self.bg.screen.blit(self.portal, (self.portal_x, self.portal_y))

        self.portal_curr_rect = pygame.Rect(self.portal_x, self.portal_y, self.portal_width , self.portal_height)
        if self.portal_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2):
            self.player_lvl = 1 #2
            Utils.write_to_playerstate("player_level", self.player_lvl,self.playerstats_file)  
            print("hi stupid")

        # Berries 1
        self.berries1_state = Utils.read_from_playerstate("berries1_state", self.playerstats_file)

        self.berries1_x = self.placement_adj_x + 2602 + self.map_x
        self.berries1_y = self.placement_adj_y + 1477 + self.map_y 

        if self.berries1_state == 1:
            self.bg.screen.blit(self.berries1, (self.berries1_x, self.berries1_y))
        else:
            self.bg.screen.blit(self.berries1b, (self.berries1_x, self.berries1_y))

        self.berries1_curr_rect = pygame.Rect(self.berries1_x, self.berries1_y, self.berries1.get_rect().width, self.berries1.get_rect().height)
        if self.berries1_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.berries1_state == 1 and self.analyzer_state == 2:
            self.health += 5
            Utils.write_to_playerstate("player_health", self.health, self.playerstats_file)
            self.berries1_state = 2
            Utils.write_to_playerstate("berries1_state", self.berries1_state, self.playerstats_file)

        # Berries 2
        self.berries2_state = Utils.read_from_playerstate("berries2_state", self.playerstats_file)

        self.berries2_x = self.placement_adj_x + 4517 + self.map_x
        self.berries2_y = self.placement_adj_y + 714 + self.map_y 

        if self.berries2_state == 1:
            self.bg.screen.blit(self.berries2, (self.berries2_x, self.berries2_y))
        else:
            self.bg.screen.blit(self.berries2b, (self.berries2_x, self.berries2_y))

        self.berries2_curr_rect = pygame.Rect(self.berries2_x, self.berries2_y, self.berries2.get_rect().width, self.berries2.get_rect().height)
        if self.berries2_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.berries2_state == 1 and self.analyzer_state == 2:
            self.health += 5
            Utils.write_to_playerstate("player_health", self.health, self.playerstats_file)
            self.berries2_state = 2
            Utils.write_to_playerstate("berries2_state", self.berries2_state, self.playerstats_file)

        # Berries 3
        self.berries3_state = Utils.read_from_playerstate("berries3_state", self.playerstats_file)

        self.berries3_x = self.placement_adj_x + 4921 + self.map_x
        self.berries3_y = self.placement_adj_y + 2860 + self.map_y 

        if self.berries3_state == 1:
            self.bg.screen.blit(self.berries3, (self.berries3_x, self.berries3_y))
        else:
            self.bg.screen.blit(self.berries3b, (self.berries3_x, self.berries3_y))

        self.berries3_curr_rect = pygame.Rect(self.berries3_x, self.berries3_y, self.berries3.get_rect().width, self.berries3.get_rect().height)
        if self.berries3_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.berries3_state == 1 and self.analyzer_state == 2:
            self.health += 5
            Utils.write_to_playerstate("player_health", self.health, self.playerstats_file)
            self.berries3_state = 2
            Utils.write_to_playerstate("berries3_state", self.berries3_state, self.playerstats_file)        

        # Berries 4
        self.berries4_state = Utils.read_from_playerstate("berries4_state", self.playerstats_file)

        self.berries4_x = self.placement_adj_x + 6652 + self.map_x
        self.berries4_y = self.placement_adj_y + 2099 + self.map_y 

        if self.berries4_state == 1:
            self.bg.screen.blit(self.berries4, (self.berries4_x, self.berries4_y))
        else:
            self.bg.screen.blit(self.berries4b, (self.berries4_x, self.berries4_y))

        self.berries4_curr_rect = pygame.Rect(self.berries4_x, self.berries4_y, self.berries4.get_rect().width, self.berries4.get_rect().height)
        if self.berries4_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.berries4_state == 1 and self.analyzer_state == 2:
            self.health += 5
            Utils.write_to_playerstate("player_health", self.health, self.playerstats_file)
            self.berries4_state = 2
            Utils.write_to_playerstate("berries4_state", self.berries4_state, self.playerstats_file)        

        # Berries 5
        self.berries5_state = Utils.read_from_playerstate("berries5_state", self.playerstats_file)

        self.berries5_x = self.placement_adj_x + 1792 + self.map_x
        self.berries5_y = self.placement_adj_y + 2408 + self.map_y 

        if self.berries5_state == 1:
            self.bg.screen.blit(self.berries5, (self.berries5_x, self.berries5_y))
        else:
            self.bg.screen.blit(self.berries5b, (self.berries5_x, self.berries5_y))

        self.berries5_curr_rect = pygame.Rect(self.berries5_x, self.berries5_y, self.berries5.get_rect().width, self.berries5.get_rect().height)
        if self.berries5_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.berries5_state == 1 and self.analyzer_state == 2:
            self.health += 5
            Utils.write_to_playerstate("player_health", self.health, self.playerstats_file)
            self.berries5_state = 2
            Utils.write_to_playerstate("berries5_state", self.berries5_state, self.playerstats_file)

        # Berries 6
        self.berries6_state = Utils.read_from_playerstate("berries6_state", self.playerstats_file)

        self.berries6_x = self.placement_adj_x + 1488 + self.map_x
        self.berries6_y = self.placement_adj_y + 963 + self.map_y 

        if self.berries6_state == 1:
            self.bg.screen.blit(self.berries6, (self.berries6_x, self.berries6_y))
        else:
            self.bg.screen.blit(self.berries6b, (self.berries6_x, self.berries6_y))

        self.berries6_curr_rect = pygame.Rect(self.berries6_x, self.berries6_y, self.berries6.get_rect().width, self.berries6.get_rect().height)
        if self.berries6_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.berries6_state == 1 and self.analyzer_state == 2:
            self.health += 5
            Utils.write_to_playerstate("player_health", self.health, self.playerstats_file)
            self.berries6_state = 2
            Utils.write_to_playerstate("berries6_state", self.berries6_state, self.playerstats_file)        

        # Berries 7
        self.berries7_state = Utils.read_from_playerstate("berries7_state", self.playerstats_file)

        self.berries7_x = self.placement_adj_x + 3181 + self.map_x
        self.berries7_y = self.placement_adj_y + 3607 + self.map_y 

        if self.berries7_state == 1:
            self.bg.screen.blit(self.berries7, (self.berries7_x, self.berries7_y))
        else:
            self.bg.screen.blit(self.berries7b, (self.berries7_x, self.berries7_y))

        self.berries7_curr_rect = pygame.Rect(self.berries7_x, self.berries7_y, self.berries7.get_rect().width, self.berries7.get_rect().height)
        if self.berries7_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.berries7_state == 1 and self.analyzer_state == 2:
            self.health += 5
            Utils.write_to_playerstate("player_health", self.health, self.playerstats_file)
            self.berries7_state = 2
            Utils.write_to_playerstate("berries7_state", self.berries7_state, self.playerstats_file)        

        # Berries 8
        self.berries8_state = Utils.read_from_playerstate("berries8_state", self.playerstats_file)

        self.berries8_x = self.placement_adj_x + 5836 + self.map_x
        self.berries8_y = self.placement_adj_y + 3545 + self.map_y 

        if self.berries8_state == 1:
            self.bg.screen.blit(self.berries8, (self.berries8_x, self.berries8_y))
        else:
            self.bg.screen.blit(self.berries8b, (self.berries8_x, self.berries8_y))

        self.berries8_curr_rect = pygame.Rect(self.berries8_x, self.berries8_y, self.berries8.get_rect().width, self.berries8.get_rect().height)
        if self.berries8_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.berries8_state == 1 and self.analyzer_state == 2:
            self.health += 5
            Utils.write_to_playerstate("player_health", self.health, self.playerstats_file)
            self.berries8_state = 2
            Utils.write_to_playerstate("berries8_state", self.berries8_state, self.playerstats_file)        

        # Berries 9
        self.berries9_state = Utils.read_from_playerstate("berries9_state", self.playerstats_file)

        self.berries9_x = self.placement_adj_x + 5392 + self.map_x
        self.berries9_y = self.placement_adj_y + 1809 + self.map_y 

        if self.berries9_state == 1:
            self.bg.screen.blit(self.berries9, (self.berries9_x, self.berries9_y))
        else:
            self.bg.screen.blit(self.berries9b, (self.berries9_x, self.berries9_y))

        self.berries9_curr_rect = pygame.Rect(self.berries9_x, self.berries9_y, self.berries9.get_rect().width, self.berries9.get_rect().height)
        if self.berries9_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.berries9_state == 1 and self.analyzer_state == 2:
            self.health += 5
            Utils.write_to_playerstate("player_health", self.health, self.playerstats_file)
            self.berries9_state = 2
            Utils.write_to_playerstate("berries9_state", self.berries9_state, self.playerstats_file)

        # Berries 10
        self.berries10_state = Utils.read_from_playerstate("berries10_state", self.playerstats_file)

        self.berries10_x = self.placement_adj_x + 2872 + self.map_x
        self.berries10_y = self.placement_adj_y + 2737 + self.map_y 

        if self.berries10_state == 1:
            self.bg.screen.blit(self.berries10, (self.berries10_x, self.berries10_y))
        else:
            self.bg.screen.blit(self.berries10b, (self.berries10_x, self.berries10_y))

        self.berries10_curr_rect = pygame.Rect(self.berries10_x, self.berries10_y, self.berries10.get_rect().width, self.berries10.get_rect().height)
        if self.berries10_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.berries10_state == 1 and self.analyzer_state == 2:
            self.health += 5
            Utils.write_to_playerstate("player_health", self.health, self.playerstats_file)
            self.berries10_state = 2
            Utils.write_to_playerstate("berries10_state", self.berries10_state, self.playerstats_file)

        # Dino 1

        # Dino 2

        # Dino 3

        # Dino 4

        # Dino 5 

        # Dino 6

        # Dino 7

        # Dino 8

        # Dino 9

        # Dino 10

        # Item 1: Analyzer
        self.analyzer_state = Utils.read_from_playerstate("item_analyzer", self.playerstats_file)

        self.analyzer_x = self.placement_adj_x + 3349 + self.map_x
        self.analyzer_y = self.placement_adj_y + 1383 + self.map_y

        if self.analyzer_state == 1:
            self.bg.screen.blit(self.analyzer, (self.analyzer_x, self.analyzer_y))

        self.analyzer_curr_rect = pygame.Rect(self.analyzer_x, self.analyzer_y, self.analyzer.get_rect().width, self.analyzer.get_rect().height)
        if self.analyzer_curr_rect.collidepoint(self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2) and self.analyzer_state == 1:
            if self.inventorylist_length <= self.maxinv:
                if self.inv1 == "-":
                    self.inv1 = "Analyzer"
                    Utils.write_to_playerstate("inv_1", self.inv1, self.playerstats_file)                    
                elif self.inv2 == "-":
                    self.inv2 = "Analyzer"
                    Utils.write_to_playerstate("inv_2", self.inv2, self.playerstats_file)                                        
                elif self.inv3 == "-":
                    self.inv3 = "Analyzer"
                    Utils.write_to_playerstate("inv_3", self.inv3, self.playerstats_file)                                        
                elif self.inv4 == "-":
                    self.inv4 = "Analyzer"
                    Utils.write_to_playerstate("inv_4", self.inv4, self.playerstats_file)                                        
                elif self.inv5 == "-":
                    self.inv5 = "Analyzer"
                    Utils.write_to_playerstate("inv_5", self.inv5, self.playerstats_file)                                        
                elif self.inv6 == "-":
                    self.inv6 = "Analyzer"
                    Utils.write_to_playerstate("inv_6", self.inv6, self.playerstats_file)                                        
                elif self.inv7 == "-":
                    self.inv7 = "Analyzer"
                    Utils.write_to_playerstate("inv_7", self.inv7, self.playerstats_file)                                        
                elif self.inv8 == "-":
                    self.inv8 = "Analyzer"
                    Utils.write_to_playerstate("inv_8", self.inv8, self.playerstats_file)                                        
                elif self.inv9 == "-":
                    self.inv9 = "Analyzer"
                    Utils.write_to_playerstate("inv_9", self.inv9, self.playerstats_file)                                        
                elif self.inv10 == "-":
                    self.inv10 = "Analyzer"
                    Utils.write_to_playerstate("inv_10", self.inv10, self.playerstats_file)
                self.berries1_state = 1                                     
                Utils.write_to_playerstate("berries1_state", self.berries1_state, self.playerstats_file)
                self.berries2_state = 1                                     
                Utils.write_to_playerstate("berries2_state", self.berries2_state, self.playerstats_file)
                self.berries3_state = 1                                     
                Utils.write_to_playerstate("berries3_state", self.berries3_state, self.playerstats_file)
                self.berries4_state = 1                                     
                Utils.write_to_playerstate("berries4_state", self.berries4_state, self.playerstats_file)
                self.berries5_state = 1                                     
                Utils.write_to_playerstate("berries5_state", self.berries5_state, self.playerstats_file)
                self.berries6_state = 1                                     
                Utils.write_to_playerstate("berries6_state", self.berries6_state, self.playerstats_file)
                self.berries7_state = 1                                     
                Utils.write_to_playerstate("berries7_state", self.berries7_state, self.playerstats_file)
                self.berries8_state = 1                                     
                Utils.write_to_playerstate("berries8_state", self.berries8_state, self.playerstats_file)
                self.berries9_state = 1                                     
                Utils.write_to_playerstate("berries9_state", self.berries9_state, self.playerstats_file)
                self.berries10_state = 1                                     
                Utils.write_to_playerstate("berries10_state", self.berries10_state, self.playerstats_file)
                self.analyzer_state = 2
                Utils.write_to_playerstate("item_analyzer", self.analyzer_state, self.playerstats_file)

                # Info-Msg
                self.anal_msg = " This is what little debris remains of a crashed ship. Did I arrive in this? Maybe there are some clues left nearby? I should take a look around! "
                self.anal_msg_img = self.textfont.render(self.anal_msg, True, self.textcolour, self.textbg)
                self.anal_msg_img_rect = self.anal_msg_img.get_rect()
                self.anal_msg_img_rect.center = self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height/2+self.player.playerimg_up.get_rect().height
                self.bg.screen.blit(self.anal_msg_img, self.anal_msg_img_rect)

        # Memory 2

        # Memory 3

        # Memory 4

        # Memory 5

        # Memory 6

        # Memory 7

        # Memory 8

        # Memory 9

        # Memory 10


            




