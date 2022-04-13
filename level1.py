# Import Libraries
import imp
from time import sleep
import pygame
import json

# Import own files
from background import Background
from player import Player
from utils import Utils
from inventory import Inventory

class Level1:
    '''Manages the 1st level'''

    def __init__(self):
        self.bg = Background()
        self.player = Player()
        self.inventory = Inventory()

        # Movement Variables
        player_state_file = open("playerstate.json")
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
        self.playerstats_file = "playerstate.json"

        self.player_lvl = json_data["player_level"]
        self.sanity = json_data["player_sanity"]
        self.love = json_data["player_love"]
        self.rationality = json_data["player_rationality"]
        self.health = json_data["player_health"]

        # Text Vars
        self.textcolour = (200, 252, 255)
        self.textfont = pygame.font.SysFont(None, 30)
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
        player_state_file = open("playerstate.json")
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
            self.ship_msg = " This is what little debris remains of a crashed ship. Did I arrive in this? Maybe there are some clues left nearby? I should take a look around! "
            self.ship_msg_img = self.textfont.render(self.ship_msg, True, self.textcolour, self.textbg)
            self.ship_msg_img_rect = self.ship_msg_img.get_rect()
            self.ship_msg_img_rect.center = self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height/2+self.player.playerimg_up.get_rect().height
            self.bg.screen.blit(self.ship_msg_img, self.ship_msg_img_rect)

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

        self.berries1_x = self.placement_adj_x + 3556 + self.map_x #4517
        self.berries1_y = self.placement_adj_y + 1941 + self.map_y #714

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

        # Berries 3

        # Berries 4

        # Berries 5

        # Berries 6

        # Berries 7

        # Berries 8

        # Berries 9

        # Berries 10

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
                if self.inv1 == " ":
                    self.inv1 = " Analyzer "
                    Utils.write_to_playerstate("inv_1", self.inv1, self.playerstats_file)                    
                elif self.inv2 == " ":
                    self.inv2 = " Analyzer "
                    Utils.write_to_playerstate("inv_2", self.inv2, self.playerstats_file)                                        
                elif self.inv3 == " ":
                    self.inv3 = " Analyzer "
                    Utils.write_to_playerstate("inv_3", self.inv3, self.playerstats_file)                                        
                elif self.inv4 == " ":
                    self.inv4 = " Analyzer "
                    Utils.write_to_playerstate("inv_4", self.inv4, self.playerstats_file)                                        
                elif self.inv5 == " ":
                    self.inv5 = " Analyzer "
                    Utils.write_to_playerstate("inv_5", self.inv5, self.playerstats_file)                                        
                elif self.inv6 == " ":
                    self.inv6 = " Analyzer "
                    Utils.write_to_playerstate("inv_6", self.inv6, self.playerstats_file)                                        
                elif self.inv7 == " ":
                    self.inv7 = " Analyzer "
                    Utils.write_to_playerstate("inv_7", self.inv7, self.playerstats_file)                                        
                elif self.inv8 == " ":
                    self.inv8 = " Analyzer "
                    Utils.write_to_playerstate("inv_8", self.inv8, self.playerstats_file)                                        
                elif self.inv9 == " ":
                    self.inv9 = " Analyzer "
                    Utils.write_to_playerstate("inv_9", self.inv9, self.playerstats_file)                                        
                elif self.inv10 == " ":
                    self.inv10 = " Analyzer "
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

        # Memory 2

        # Memory 3

        # Memory 4

        # Memory 5

        # Memory 6

        # Memory 7

        # Memory 8

        # Memory 9

        # Memory 10


            




