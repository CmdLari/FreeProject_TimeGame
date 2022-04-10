# Import Libraries
import pygame

# Import own files

UP, DOWN, LEFT, RIGHT = range(4)

class Player:
    '''Player Settings'''

    def __init__(self):
        '''intitialize player settings'''

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height
        pygame.display.set_caption("Time Game")

        # In which direction is the player walking
        self.direction = UP

        # Player sprite 
        self.playerimg_up = pygame.image.load('_IMGS/player_up.png')
        self.playerimg_right = pygame.image.load('_IMGS/player_right.png')
        self.playerimg_down = pygame.image.load('_IMGS/player_down.png')
        self.playerimg_left = pygame.image.load('_IMGS/player_left.png')

        # Player sprite position
        self.player_rect_x = self.screen.get_rect().width//2 - self.playerimg_up.get_rect().width//2 
        self.player_rect_y = self.screen.get_rect().height//2 - self.playerimg_up.get_rect().height//2

        # Player Stats
        self.sanity = 50
        self.love = 0
        self.rationality = 0
        
        # -- Player lvl
        self.playerlvl = 1

    def playerblit(self):
        '''Draw player to screen'''

        if self.direction == UP:
            self.screen.blit(self.playerimg_up, (self.player_rect_x, self.player_rect_y))
        elif self.direction == DOWN:
            self.screen.blit(self.playerimg_down, (self.player_rect_x, self.player_rect_y))
        elif self.direction == LEFT:
            self.screen.blit(self.playerimg_left, (self.player_rect_x, self.player_rect_y))
        elif self.direction == RIGHT:
            self.screen.blit(self.playerimg_right, (self.player_rect_x, self.player_rect_y))
