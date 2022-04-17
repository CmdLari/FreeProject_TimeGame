import pygame

class Window:
    """ Represents the pygame window. """

    def __init__(self):
        """
        Initializes the window.
        """
        self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height
        pygame.display.set_caption("Going Home")


    def blit_img(self, img: pygame.Surface, x: int, y: int):
        """
        Blits an image on the window.
            
        Args:
            img: The image to blit
            x: The x coordinate of the image
            y: The y coordinate of the image
        """
        # Placement adjustments
        self.x_adj = self.width//2 - img.get_rect().width//2 + x
        self.y_adj = self.height//2 - img.get_rect().height//2 + y
        self.screen.blit(img, (self.x_adj, self.y_adj))