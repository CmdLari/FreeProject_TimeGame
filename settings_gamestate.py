import sys
import pygame
import json

class Gamestate:
    '''Handles the game's current state and displaying'''

    def __init__(self, settings_background, screen_menu, utility_saves):
        self.level = 0
        
        # Attributes to be passed
        self.settings_background = settings_background
        self.screen_menu = screen_menu
        self.utility_saves = utility_saves

        self.savefile = open("0_save.json")
        self.json_data = json.load(self.savefile)

    def setup_screen(self):
        if self.level == 0:
            self.screen_menu.show_menu(self.settings_background, self.utility_saves)
        elif self.level == 1:
            print("Hi")

    def load_game(self):
        self.level = self.json_data["level"]
        print(self.level)

    

    # def handle_music(self):