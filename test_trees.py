import pygame

class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, group) -> None:
        super().__init__()
        self.image = pygame.image.load("_IMGS/portal.png").convert_alpha()
        self.rect = self.image.get_rect(topleft= pos)

        