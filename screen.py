# Imports
import pygame

class Screen:
    """Creates the game's window"""
    def __init__(self):

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height
        pygame.display.set_caption("Going Home")