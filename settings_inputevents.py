import pygame
import sys

class Inputevents:
    '''Manages all key events'''

    def __init__(self):

        pygame.init()

    def check_keyevents(self):
        '''Checks for key and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)

    def keydown_events(self, event):
        '''Handles Keydown events'''

        # Quit
        if event.key == pygame.K_ESCAPE:
            sys.exit()