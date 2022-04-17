from window import Window
import pygame
from portal import Portal

class Level:
    """ Represents a level. """

    def __init__(self, level_background) -> None:
        """ Initializes the level. """
        self.level_number = 0
        self.level_name = "Level_" + str(self.level_number)
        self.level_description = "Description"
        self.level_map = "Map"
        self.level_background = pygame.image.load(level_background)
        self.level_sound = pygame.mixer.Sound('assets/_MUS/Timegame_lvl1.mp3')
        self.play_sound = True

    def load_level(self, level: int, camera_group ) -> None:
        """Loads specified level to the window

        Args:
            level: The level to load
            window: The window to load the level to
        """
        internal_surf = camera_group.internal_surf

        if self.play_sound:
            self.play_sound_level()
            self.play_sound = False
        if level == 1:

            internal_surf.blit(self.level_background, (0, 0))


    def save_level(self, level_number: int) -> None:
        """ Saves the level to a file.

        :param int level_number: The current level number
        """
        raise NotImplementedError

    def play_sound_level(self) -> None:
        """ Plays the level's sound."""
        self.level_sound.set_volume(0.1)
        pygame.mixer.Sound.play(self.level_sound, loops=-1)

    def place_portal(self, camera_group):
        """ Places portal at determined coordinates"""
        Portal((20, 20), camera_group)