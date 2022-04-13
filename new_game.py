# Import Libraries
import imp
import pygame
import json

# Import own files
from utils import Utils

class NewGame:
    '''Resets the game'''

    def __init__(self):
        self.playerstats_file = "playerstate.json"
        player_state_file = open("playerstate.json")
        json_data = json.load(player_state_file)

        self.mov_x = json_data["mov_x"]
        self.mov_y = json_data["mov_y"]
        self.map_x = json_data["map_x"]
        self.map_y = json_data["map_y"]   

        self.player_lvl = json_data["player_level"]

        self.sanity = json_data["player_sanity"]
        self.love = json_data["player_love"]
        self.rationality = json_data["player_rationality"]
        self.health = json_data["player_health"]         

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

        self.berries1 = json_data["berries1_state"]       
        self.berries2 = json_data["berries1_state"]
        self.berries3 = json_data["berries1_state"]
        self.berries4 = json_data["berries1_state"]
        self.berries5 = json_data["berries1_state"]
        self.berries6 = json_data["berries1_state"]
        self.berries7 = json_data["berries1_state"]
        self.berries8 = json_data["berries1_state"]
        self.berries9 = json_data["berries1_state"]
        self.berries10 = json_data["berries1_state"]

    def restart(self):
        '''Resets ALL values for the game'''
        # Level    
        self.player_lvl = 1
        Utils.write_to_playerstate("player_level", self.player_lvl, self.playerstats_file)

        # Stats
        self.sanity = 50
        Utils.write_to_playerstate("player_sanity", self.sanity, self.playerstats_file)
        self.love = 0
        Utils.write_to_playerstate("player_love", self.love, self.playerstats_file)
        self.rationality = 0
        Utils.write_to_playerstate("player_rationality", self.rationality, self.playerstats_file)
        self.health = 20
        Utils.write_to_playerstate("player_health", self.health, self.playerstats_file)
        
        # Map placement
        self.mov_x = 0
        Utils.write_to_playerstate("mov_x", self.mov_x, self.playerstats_file)
        self.mov_y = 0
        Utils.write_to_playerstate("mov_y", self.mov_y, self.playerstats_file)                    
        self.map_x = 0
        Utils.write_to_playerstate("map_x", self.map_x, self.playerstats_file)                    
        self.map_y = 0
        Utils.write_to_playerstate("map_y", self.map_y, self.playerstats_file)     

        # Inventory
        self.inv1 = "-"
        Utils.write_to_playerstate("inv_1", self.inv1, self.playerstats_file)             
        self.inv2 = "-"
        Utils.write_to_playerstate("inv_2", self.inv2, self.playerstats_file)     
        self.inv3 = "-"
        Utils.write_to_playerstate("inv_3", self.inv3, self.playerstats_file)     
        self.inv4 = "-"
        Utils.write_to_playerstate("inv_4", self.inv4, self.playerstats_file)     
        self.inv5 = "-"
        Utils.write_to_playerstate("inv_5", self.inv5, self.playerstats_file)     
        self.inv6 = "-"
        Utils.write_to_playerstate("inv_6", self.inv6, self.playerstats_file)     
        self.inv7 = "-"
        Utils.write_to_playerstate("inv_7", self.inv7, self.playerstats_file)     
        self.inv8 = "-"
        Utils.write_to_playerstate("inv_8", self.inv8, self.playerstats_file)     
        self.inv9 = "-"
        Utils.write_to_playerstate("inv_9", self.inv9, self.playerstats_file)     
        self.inv10 = "-"
        Utils.write_to_playerstate("inv_10", self.inv10, self.playerstats_file)     

        # Lvl 1
        # --Berries
        self.berries1 = 2
        Utils.write_to_playerstate("berries1_state", self.berries1, self.playerstats_file)             
        self.berries2 = 2
        Utils.write_to_playerstate("berries2_state", self.berries2, self.playerstats_file)             
        self.berries3 = 2
        Utils.write_to_playerstate("berries3_state", self.berries3, self.playerstats_file)             
        self.berries4 = 2
        Utils.write_to_playerstate("berries4_state", self.berries4, self.playerstats_file)             
        self.berries5 = 2
        Utils.write_to_playerstate("berries5_state", self.berries5, self.playerstats_file)             
        self.berries6 = 2
        Utils.write_to_playerstate("berries6_state", self.berries6, self.playerstats_file)             
        self.berries7 = 2
        Utils.write_to_playerstate("berries7_state", self.berries7, self.playerstats_file)             
        self.berries8 = 2
        Utils.write_to_playerstate("berries8_state", self.berries8, self.playerstats_file)             
        self.berries9 = 2
        Utils.write_to_playerstate("berries9_state", self.berries9, self.playerstats_file)             
        self.berries10 = 2
        Utils.write_to_playerstate("berries10_state", self.berries10, self.playerstats_file)  

        # --Items
        self.analyzerstate = 1
        Utils.write_to_playerstate("item_analyzer", self.analyzerstate, self.playerstats_file)          