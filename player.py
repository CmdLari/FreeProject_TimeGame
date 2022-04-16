import pygame

class Player:

    def __init__(self) -> None:
        """ Initializes the player. """
        self.name = "Player"
        self.health = 100
        self.max_health = 100
        self.damage = 10
        self.defense = 10
        self.speed = 10
        self.level = 1
        self.love = 0
        self.rationality = 0
        self.sanity = 0
        self.experience = 0
        self.experience_to_next_level = 100
        self.experience_to_next_level_multiplier = 1.5
        self.inventory = {"Slot 1": "Empty", "Slot 2": "Empty", "Slot 3": "Empty", "Slot 4": "Empty", "Slot 5": "Empty", "Slot 6": "Empty", "Slot 7": "Empty", "Slot 8": "Empty", "Slot 9": "Empty", "Slot 10": "Empty"}
        self.player_image = pygame.image.load("_IMGS/player_down.png")


    def level_up(self):
        """ Increases player stats. """
        self.level += 1
        self.experience_to_next_level = int(self.experience_to_next_level * self.experience_to_next_level_multiplier)
        self.health = self.max_health
        self.damage += 1
        self.defense += 1
        self.speed += 1