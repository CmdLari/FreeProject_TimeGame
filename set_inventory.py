# Import Libraries
import imp
from re import X
from time import sleep
from tkinter import Y
import pygame
import json

# Import own files
from vis_background import Background
from set_player import Player
from ut_utils import Utils

class Inventory:
    '''Manages the 1st level'''

    def __init__(self):
        self.bg = Background()
        self.player = Player()

        player_state_file = open("0-playerstate.json")
        json_data = json.load(player_state_file)

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

        # Text Vars
        self.textcolour = (0, 255, 240)
        self.textfont = pygame.font.Font("0-font_press_start2p.ttf", 15)
        self.textfont_inv = pygame.font.Font("0-font_press_start2p.ttf", 10)
        self.textfont_invinf = pygame.font.Font("0-font_share_tech_mono.ttf", 25)
        self.textbg = (20, 0, 40)

        # Inventory msg
        self.invpos_key = 0

    def inventorytext(self):
        '''Blits inventory to screen'''
        for item in self.inventorylist:
            self.item_msg = item
            self.item_msg_img_rect = self.item_msg_img.get_rect()
            self.y = 40
            self.item_msg_img_rect.x = 40
            self.item_msg_img_rect.y = self.y
            self.bg.screen.blit(self.item_msg_img, self.item_msg_img_rect)
            self.y += 60

    def kickinventory(self):
        '''Kicks something from the inventory'''
        self.kickmsg = " Do you want to drop an item? Y/N"
        self.kickmsg_img = self.textfont.render(self.kickmsg, True, self.textcolour, self.textbg)
        self.kickmsg_img_rect = self.kickmsg_img.get_rect()
        self.kickmsg_img_rect.center = self.bg.screen.get_rect().center
        self.bg.screen.blit(self.kickmsg_img, self.kickmsg_img_rect)
        self.kickmsginput = input()
        if self.kickmsginput == Y:
            self.kickmsg = " Do you want to drop an item? Y/N"
            self.kickmsg_img = self.textfont.render(self.kickmsg, True, self.textcolour, self.textbg)
            self.kickmsg_img_rect = self.kickmsg_img.get_rect()
            self.kickmsg_img_rect.center = self.bg.screen.get_rect().center
            self.bg.screen.blit(self.kickmsg_img, self.kickmsg_img_rect)

    def inventory_msg(self):
        '''Draws info about Inventory to screen'''
        self.invpos = int(self.invpos_key)
        self.inv_msg = self.inventorylist[self.invpos]
     
        if self.inventorylist[self.invpos] == "Analyzer":
            self.inv_inf_msg = "This will help you find viable nourishment"
        else:
            self.inv_inf_msg = " There is nothing in your inventory "

        self.inv_msg_img = self.textfont.render(self.inv_msg, True, self.textcolour, self.textbg)
        self.inv_msg_img_rect = self.inv_msg_img.get_rect()
        self.inv_msg_img_rect.center = self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2 + self.player.playerimg_up.get_rect().height   

        self.inv_inf_msg_img = self.textfont_invinf.render(self.inv_inf_msg, True, self.textcolour, self.textbg)
        self.inv_inf_msg_img_rect = self.inv_inf_msg_img.get_rect()
        self.inv_inf_msg_img_rect.center = self.bg.screen.get_rect().width//2, self.bg.screen.get_rect().height//2 + self.player.playerimg_up.get_rect().height + self.inv_msg_img_rect.height +10       

        self.bg.screen.blit(self.inv_msg_img, self.inv_msg_img_rect)
        self.bg.screen.blit(self.inv_inf_msg_img, self.inv_inf_msg_img_rect)

        print(self.inv_msg)
        print(self.invpos)
        print(self.inv_inf_msg)

