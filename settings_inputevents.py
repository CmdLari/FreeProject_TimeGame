import pygame
import sys

class Inputevents:
    '''Manages all key events'''

    def __init__(self):
        pass

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
            print("up")
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y =  0    
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        # Quit
        if event.key == pygame.K_ESCAPE:
            sys.exit()