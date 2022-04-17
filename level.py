from window import Window
import pygame

class Level:
    """ Represents a level. """

    def __init__(self) -> None:
        """ Initializes the level. """
        self.level_number = 0
        self.level_name = "Level_" + str(self.level_number)
        self.level_description = "Description"
        self.level_map = "Map"
        self.level_background = "Background"
        self.level_sound = pygame.mixer.Sound('assets/_MUS/Timegame_lvl1.mp3')
        self.play_sound = True

    def load_level(self, level: int, window: Window) -> None:
        """Loads specified level to the window

        Args:
            level: The level to load
            window: The window to load the level to
        """
        
        if self.play_sound:
            self.play_sound_level()
            self.play_sound = False
        if level == 1:
            self.level_background = pygame.image.load("assets/_IMGS/_Lvl1/level1_bg.png")
            #self.level_sound = pygame.mixer.Sound('_MUS/Timegame_lvl1.mp3')
            
            window.blit_img(self.level_background, 0, 0)


    def save_level(self, level_number: int) -> None:
        """ Saves the level to a file.

        :param int level_number: The current level number
        """
        raise NotImplementedError

    def play_sound_level(self) -> None:
        """ Plays the level's sound."""
        self.level_sound.set_volume(0.1)
        pygame.mixer.Sound.play(self.level_sound, loops=-1)