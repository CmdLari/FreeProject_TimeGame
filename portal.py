import pygame
from player import Player
from text import Text
from window import Window

class Portal(pygame.sprite.Sprite):
    """ Represents a portal."""

    def __init__(self, pos, group) -> None:
        """ Initializes portal. """
        super().__init__(group)
        self.image = pygame.image.load("assets/_IMGS/portal.png").convert_alpha()
        self.rect = self.image.get_rect(topleft= pos)

    def check_collision(self, player: Player, window: Window):
        """ Checks if the player collides with the portal """
        if self.rect.collidepoint(player.rect.x, player.rect.y):
            self.portal_message(window)
            
    def portal_message (self, window: Window):
        """" Portal asks if the player wants to continue """
        text = Text(window)
        
        portal_msg = ["This seems to lead me forwards and back to my time.",
            "Do I already want to enter? [Y/N]"]

        text.copy_text(portal_msg)




