import pygame


class Player(pygame.sprite.Sprite):
    """ Represents the player. """

    def __init__(self, pos, group) -> None:
        """ Initializes player. 
        
        Args:
            pos (tuple): Player position.
            group (pygame.sprite.Group): Group to add player to.
        """
        super().__init__(group)
        self.image = pygame.image.load("assets/_IMGS/player_up.png")
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 100

        self.name = "Player"
        self.level = 1
        self.health = 100
        self.love = 0
        self.rationality = 0
        self.sanity = 0
        self.inventory = {"Slot 1": "Empty", "Slot 2": "Empty", "Slot 3": "Empty", "Slot 4": "Empty", "Slot 5": "Empty", "Slot 6": "Empty", "Slot 7": "Empty", "Slot 8": "Empty", "Slot 9": "Empty", "Slot 10": "Empty"}

    def input(self):
        """ Gets player input. """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.image = pygame.image.load("assets/_IMGS/player_up.png")
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.image = pygame.image.load("assets/_IMGS/player_down.png")
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.image = pygame.image.load("assets/_IMGS/player_right.png")
            self.direction.x = 1
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.image = pygame.image.load("assets/_IMGS/player_left.png")
            self.direction.x = -1
        else:
            self.direction.x = 0


    def update(self):
        """ Updates the player, based on input. """
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