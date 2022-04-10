# Import Libraries
import pygame
import json
import sys
from time import sleep

# Import own files
from settings import Settings
from background import Background
from player import LEFT, RIGHT, UP, DOWN, Player
from level1 import Level1

# This is a change

class Timegame:
    '''Manages the game'''

    def __init__(self):
        '''Initialize game, create resources'''
        pygame.init()

        # rename imported files
        self.settings = Settings()
        self.bg = Background()
        self.player = Player()
        self.lvl1 = Level1()

        # Initialize screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height
              
    def run_game(self):
        '''Main loop for the game'''

        pygame.key.set_repeat(int(10))

        self.game_run_active = False 

        if self.game_run_active == False:
            self.menusound = pygame.mixer.Sound('_MUS/timegame_menu.mp3')
            self.menusound.set_volume(0.5)
            pygame.mixer.Sound.play(self.menusound, loops=-1)

        while True:

            self.bg.menu_screen()
            self.draw_menu_buttons()
            self.draw_mouse()
            self.check_menu_buttons()

            if self.game_run_active == True:
                pygame.mouse.set_visible(False)
                self.check_player_lvl()
                self.bg.background()
                self.check_events()
                self.draw_lvl()
                self.drawplayer()
                self.bg.screentext()

            pygame.display.flip()

    def draw_mouse(self):
        '''Draw mouse to screen'''
        pygame.mouse.set_visible(False)

        self.mouse_img = pygame.image.load('_IMGS/mouse.png')
        self.mouse_pos = pygame.mouse.get_pos()
        self.screen.blit(self.mouse_img, self.mouse_pos)
        self.mouse_rect = self.mouse_img.get_rect()

    def check_menu_buttons(self):
        '''Checks for clicks on menu buttons'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.ng_rect.collidepoint(pygame.mouse.get_pos()):
                    self.game_run_active = True
                    if self.player.playerlvl ==1:
                        self.lvl1sound = pygame.mixer.Sound('_MUS/timegame_lvl1.mp3')
                        pygame.mixer.Sound.play(self.lvl1sound, loops=-1)
                elif self.quit_rect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()

    def check_events(self):
        '''Checks for key and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event):
        '''Respond to keypresses'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if event.type == pygame.KEYDOWN:

            # Quit
            if event.key == pygame.K_ESCAPE:
                sys.exit()

            # Movement #5
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.player.direction = LEFT
                if self.bg.bg_rect_x <= self.bg.screen.get_rect().x:
                    self.bg.ix +=5
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT: 
                self.player.direction = RIGHT
                if self.bg.bg_rect_x >= self.bg.screen.get_rect().x - self.bg.screen.get_rect().width*3:
                    self.bg.ix -=5
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                self.player.direction = UP
                if self.bg.bg_rect_y <= self.bg.screen.get_rect().y:
                    self.bg.iy +=5 
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.player.direction = DOWN
                if self.bg.bg_rect_y >= self.bg.screen.get_rect().y - self.bg.screen.get_rect().height*3:
                    self.bg.iy -=5

            # Return to menu
            elif event.key == pygame.K_r:
                self.game_run_active = False
                pygame.mixer.Sound.stop(self.lvl1sound)
                self.menusound = pygame.mixer.Sound('_MUS/timegame_menu.mp3')
                pygame.mixer.Sound.play(self.menusound, loops=-1)

            # Info-Screen
            elif event.key == pygame.K_h:
                self.bg.info_screen()

            # Journal
            elif event.key == pygame.K_j:
                self.bg.journal()


    def draw_menu_buttons(self):
        '''Initialize menu buttons'''
        # Continue
        self.cont_button = pygame.image.load("_IMGS/continue.png")
        self.cont_rect_w = self.cont_button.get_rect().width
        self.cont_rect_h = self.cont_button.get_rect().height
        self.bg.screen.blit(self.cont_button, (self.bg.width//2-self.cont_rect_w//2, self.bg.height//2-self.cont_rect_h//2))

        # New Game
        self.ng_button = pygame.image.load("_IMGS/new_game.png")
        self.ng_w = self.ng_button.get_rect().width
        self.ng_h = self.ng_button.get_rect().height
        self.ng_rect = pygame.Rect((self.bg.width//2-self.ng_w//2, self.bg.height//2-self.ng_h//2 - self.cont_rect_h - 20),(self.ng_w, self.ng_h))
        self.bg.screen.blit(self.ng_button, (self.bg.width//2-self.ng_w//2, self.bg.height//2-self.ng_h//2 - self.cont_rect_h - 20))

        # Quit
        self.quit_button = pygame.image.load("_IMGS/quit.png")
        self.quit_w = self.quit_button.get_rect().width
        self.quit_h = self.quit_button.get_rect().height
        self.quit_rect = pygame.Rect((self.bg.width//2-self.quit_w//2, self.bg.height//2-self.quit_h//2 + self.cont_rect_h + 20),(self.quit_w, self.quit_h))
        self.bg.screen.blit(self.quit_button, (self.bg.width//2-self.quit_w//2, self.bg.height//2-self.quit_h//2 + self.cont_rect_h + 20))

    def drawplayer(self):
        '''Draws the player to the map'''
        self.player.playerblit()
        

    def check_player_lvl(self):
        '''Checks for player level and sets map'''
        if self.player.playerlvl == 1:
            self.bglvl1 = pygame.image.load('_IMGS/_lvl1/map_lvl1.png')
            self.bg.bg = self.bglvl1
            pygame.mixer.Sound.stop(self.menusound)

    def draw_lvl(self):
        '''Initializes lvl assets'''
        if self.player.playerlvl == 1:
            self.lvl1.backgroundlvl1_assets()

if __name__ == '__main__':
    # Make a game instance and run the game
    tg = Timegame()
    tg.run_game()