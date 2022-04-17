import pygame

class Settings:
    def __init__(self) -> None:
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.font_name = pygame.font.match_font('arial')
        self.font_size = 20
        self.font_color = (255, 255, 255)
        self.font_color_selected = (255, 0, 0)
        self.font_color_unselected = (255, 255, 255)
        self.font_color_disabled = (100, 100, 100)
        self.font_color_selected_disabled = (100, 100, 100)
        self.font_color_unselected_disabled = (100, 100, 100)
