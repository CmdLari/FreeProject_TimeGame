import pygame
import sys

class Events:

    def __init__(self):
        pass

    def check_events(self, camera_group):
        """ Checks for events and calls the corresponding action.
        Args:
            camera_group (CameraGroup): The camera group.
        """
        # This seems to be only allowed to called once,
        # so don't use this in another place.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)
            elif event.type == pygame.MOUSEWHEEL:
                camera_group.zoom_scale += event.y * 0.03

    def keydown_events(self, event):
        """ Action based on the given event.

        Args:
            event (pygame.event): The triggered event
        """
        # Quit
        if event.key == pygame.K_ESCAPE:
            sys.exit()