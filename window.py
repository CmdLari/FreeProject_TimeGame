import pygame

class Window:
    '''Handles the game's window'''

    def __init__(self):
        '''Create the game window'''
        self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height
        pygame.display.set_caption("Going Home")


    def blit_img(self, img: pygame.Surface, x: int, y: int):
        '''Blit imgs to screen'''

        # Placement adjustments
        self.x_adj = self.width//2 - img.get_rect().width//2 + x
        self.y_adj = self.height//2 - img.get_rect().height//2 + y
        self.screen.blit(img, (self.x_adj, self.y_adj))