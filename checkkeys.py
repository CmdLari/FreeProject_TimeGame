import pygame

class CheckKeys:
    def __init__(self) -> None:
        pass

    def check_button_presses(self):     
        """Check for pressed buttons"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()                     
            
            elif event.type == pygame.KEYDOWN:
                
                # Return to menu
                if event.key == pygame.K_r:
                    pygame.mixer.Sound.stop(self.menu.menusound)
                    self.gamestate = False
                    return self.gamestate
                elif event.key != pygame.K_r:
                    self.gamestate = True
                    return self.gamestate