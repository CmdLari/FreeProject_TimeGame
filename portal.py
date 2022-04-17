import pygame

class Portal(pygame.sprite.Sprite):
    """ Represents a portal."""

    def __init__(self, pos, group) -> None:
        """ Initializes portal. """
        super().__init__(group)
        self.image = pygame.image.load("_IMGS/portal.png").convert_alpha()
        self.rect = self.image.get_rect(topleft= pos)