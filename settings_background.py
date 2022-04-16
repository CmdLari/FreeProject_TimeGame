import pygame

class Background:
    '''Handles the game's background'''

    def __init__(self):

        pygame.init()

    def create_window(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height
        pygame.display.set_caption("Going Home")

    def blit_img(self, img, x, y):
        '''Blit imgs to screen'''

        # Placement adjustments
        self.x_adj = self.width//2 - img.get_rect().width//2 + x
        self.y_adj = self.height//2 - img.get_rect().height//2 + y
        self.screen.blit(img, (self.x_adj, self.y_adj))
