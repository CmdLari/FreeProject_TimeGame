import pygame

from level1 import Level1
from saves import Saves
from texts import Texts

class Level:
    """Loads level according to level"""

    def __init__(self, screen, menu):

        self.menu = menu
        self.saves = Saves()
        self.texts = Texts(screen)
        self.level1 = Level1(screen, self.texts)
     
    def start_level(self):
        """Chooses the level"""
        self.levelmusic = self.level1.levelmusic
        pygame.mixer.Sound.play(self.levelmusic, loops= -1)
        self.level = self.saves.read_from_save("level", "player.json")
        pygame.mixer.Sound.stop(self.menu.menusound)


        if self.level == 1:
            self.level1.lvl_1()
        elif self.level == 2:
            print("2")
        elif self.level == 3:
            print("2")
        elif self.level == 4:
            print("2")
        elif self.level == 5:
            print("2")                                    