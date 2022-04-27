# Imports
import pygame
import sys

from saves import Saves

class Menu:
    """Creates the menu"""
    def __init__(self, screen):
        """Initializes the menu"""
        self.screen = screen

        # Initialize saving
        self.saves = Saves()

        self.gamestate = False
        self.menusound = pygame.mixer.Sound("_assets/MUS/goinghome_menu.mp3")
        pygame.mixer.Sound.play(self.menusound, loops= -1)

    def draw_menu(self):
        # BG
        menu_bg = pygame.image.load("_assets/IMGS/menu/menu_background.png")
        self.screen.screen.blit(menu_bg, (0, 0))

        # Buttons
        # --New Game
        new_game = pygame.image.load("_assets/IMGS/menu/menu_button_new_game.png")
        new_game_rect = new_game.get_rect()
        new_game_rect.center = self.screen.width/2 - new_game_rect.width/2, self.screen.height/2 - new_game_rect.height/2 - new_game_rect.height -20
        self.new_game_nrect = new_game_rect
        self.screen.screen.blit(new_game, new_game_rect.center)

        # --Continue
        cont = pygame.image.load("_assets/IMGS/menu/menu_button_continue.png")
        cont_rect = cont.get_rect()
        cont_rect.center = self.screen.width/2 - cont_rect.width/2, self.screen.height/2 - cont_rect.height/2
        self.cont_nrect = cont_rect
        self.screen.screen.blit(cont, cont_rect.center)

        # --Quit
        quit = pygame.image.load("_assets/IMGS/menu/menu_button_quit.png")
        quit_rect = quit.get_rect()
        quit_rect.center = self.screen.width/2 - quit_rect.width/2, self.screen.height/2 - quit_rect.height/2 + quit_rect.height +20
        self.quit_nrect = quit_rect
        self.screen.screen.blit(quit, quit_rect.center)

        # Mouse
        mouse = pygame.image.load("_assets/IMGS/menu/menu_mouse.png")
        mouse_rect = mouse.get_rect()
        mouse_rect.center = pygame.mouse.get_pos()
        self.screen.screen.blit(mouse, mouse_rect.center)

        self.check_mouseclicks()

    def check_mouseclicks(self):
        """Checks if buttons are clicked"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.new_game_nrect.collidepoint(pygame.mouse.get_pos()):
                    level = 1
                    health = 20
                    sanity = 20
                    rationality = 0
                    love = 0
                    Inv1 = "-"
                    Inv2 = "-"
                    Inv3 = "-"
                    Inv4 = "-"
                    Inv5 = "-"
                    Inv6 = "-"
                    Inv7 = "-"
                    Inv8 = "-"
                    Inv9 = "-"
                    Inv10 = "-"
                    self.saves.write_to_save("level", level, "player.json")
                    self.saves.write_to_save("health", health, "player.json")
                    self.saves.write_to_save("sanity", sanity, "player.json")
                    self.saves.write_to_save("rationality", rationality, "player.json")
                    self.saves.write_to_save("love", love, "player.json")
                    self.saves.write_to_save("Inv1", Inv1, "player.json")
                    self.saves.write_to_save("Inv2", Inv2, "player.json")
                    self.saves.write_to_save("Inv3", Inv3, "player.json")
                    self.saves.write_to_save("Inv4", Inv4, "player.json")
                    self.saves.write_to_save("Inv5", Inv5, "player.json")
                    self.saves.write_to_save("Inv6", Inv6, "player.json")
                    self.saves.write_to_save("Inv7", Inv7, "player.json")
                    self.saves.write_to_save("Inv8", Inv8, "player.json")
                    self.saves.write_to_save("Inv9", Inv9, "player.json")
                    self.saves.write_to_save("Inv10", Inv10, "player.json")
                    if self.saves.read_from_save("level", "player.json") == 1:
                        self.gamestate = True
                        return self.gamestate
                elif self.cont_nrect.collidepoint(pygame.mouse.get_pos()):
                    self.gamestate = True
                    return self.gamestate
                elif self.quit_nrect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
