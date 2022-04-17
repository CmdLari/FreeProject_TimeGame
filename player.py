import pygame
import sys

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, group) -> None:
        """ Initializes the player. """
        super().__init__(group)
        self.image = pygame.image.load("_IMGS/player_down.png")
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 100

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

    def check_keyevents(self):
        '''Checks for key and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)

    def keydown_events(self, event):
        '''Handles Keydown events'''

        keys = pygame.key.get_pressed()


        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.rect.center += self.direction * self.speed
            self.image = pygame.image.load("_IMGS/player_up.png")
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.rect.center += self.direction * self.speed
            self.image = pygame.image.load("_IMGS/player_down.png")
        else:
            self.direction.y =  0    
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.rect.center += self.direction * self.speed
            self.image = pygame.image.load("_IMGS/player_right.png")
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.rect.center += self.direction * self.speed
            self.image = pygame.image.load("_IMGS/player_left.png")
        else:
            self.direction.x = 0
            self.rect.center += self.direction * self.speed
            

        # Quit
        if event.key == pygame.K_ESCAPE:
            sys.exit()



    def input(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self) -> None:
        self.input()
        self.rect.center += self.direction * self.speed


    def level_up(self) -> None:
        """ Increases player stats. """
        self.level += 1
        self.experience_to_next_level = int(self.experience_to_next_level * self.experience_to_next_level_multiplier)
        self.health = self.max_health
        self.damage += 1
        self.defense += 1
        self.speed += 1