# Imports
from movement import Movement
from animated_player import AnimatedPlayer
from saves import Saves

class Player:
    """Defines the player"""
    def __init__(self, screen):
        """Initializes player"""
        self.movement = Movement(screen)
        self.playerimg = self.movement.playerimg
        self.animated_player = AnimatedPlayer(screen, self.playerimg)
        self.saves = Saves()

        self.level = self.saves.read_from_save("level", "player.json")
        self.health = self.saves.read_from_save("health", "player.json")
        self.sanity = self.saves.read_from_save("sanity", "player.json")
        self.rationality = self.saves.read_from_save("rationality", "player.json")
        self.love = self.saves.read_from_save("love", "player.json")
        self.Inv1 = self.saves.read_from_save("Inv1", "player.json")
        self.Inv2 = self.saves.read_from_save("Inv2", "player.json")
        self.Inv3 = self.saves.read_from_save("Inv3", "player.json")
        self.Inv4 = self.saves.read_from_save("Inv4", "player.json")
        self.Inv5 = self.saves.read_from_save("Inv5", "player.json")
        self.Inv6 = self.saves.read_from_save("Inv6", "player.json")
        self.Inv7 = self.saves.read_from_save("Inv7", "player.json")
        self.Inv8 = self.saves.read_from_save("Inv8", "player.json")
        self.Inv9 = self.saves.read_from_save("Inv9", "player.json")
        self.Inv10 = self.saves.read_from_save("Inv10", "player.json")


    def draw_player(self):
        """Blits standart player to screen"""
    
        self.animated_player.update_player()
        
    def inventory(self):
        """Creates and handles the inventory"""
        self.inventory = []

