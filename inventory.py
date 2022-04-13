# Import Libraries
import imp
from re import X
from time import sleep
from tkinter import Y
import pygame
import json

# Import own files
from background import Background
from player import Player
from utils import Utils

class Inventory:
    '''Manages the 1st level'''

    def __init__(self):
        self.bg = Background()
        self.player = Player()

        player_state_file = open("playerstate.json")
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
        self.textcolour = (200, 252, 255)
        self.textfont = pygame.font.SysFont(None, 20)
        self.textbg = (31, 13, 0)

    def add_item_to_inv(self):
        '''Adds item to inventory'''

    def inventorytext(self):
        '''Blits inventory to screen'''
        for item in self.inventorylist:
            self.item_msg = item
            self.item_msg_img = self.textfont.render(self.item_msg, True, self.textcolour, self.textbg)
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

