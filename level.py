from window import Window
import pygame

class Level:

    def __init__(self) -> None:
        """ Initializes the level. """
        self.level_number = 0
        self.level_name = "Level_" + str(self.level_number)
        self.level_description = "Description"
        self.level_map = "Map"
        self.level_background = "Background"
        self.level_sound = "Soundtrack"

    def load_level(self, level: int, window: Window) -> None:
        """Loads specified level to the window

        :param int level: The level to load
        :param Window window: The window to load the level to
        """
        if level == 1:
            self.level_background = pygame.image.load("_IMGS/_Lvl1/map_lvl1.png")
            self.level_sound = pygame.mixer.Sound('_MUS/Timegame_lvl1.mp3')
            self.play_sound()
            window.blit_img(self.level_background, 0, 0)


    def save_level(self, level_number: int) -> None:
        """ Saves the level to a file. """
        raise NotImplementedError

    def play_sound(self) -> None:
        """ Plays the level's sound."""
        self.level_sound.set_volume(0.1)
        pygame.mixer.Sound.play(self.level_sound, loops=-1)