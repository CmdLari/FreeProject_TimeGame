# Import Libraries
import pygame

class UserInput:
    '''Handles any input by user'''

    def __init__(self):
        '''Handle vars here'''
        
        # Text Vars
        self.textcolour = (200, 252, 255)
        self.textfont = pygame.font.SysFont(None, 20)
        self.textbg = (31, 13, 0)
        self.clock = pygame.time.Clock()
        self.input_box = pygame.Rect(100, 100, 140, 32)
        self.text = " "
        self.active = False
        self.done = False

    def input_box(self):
        '''Handles the drawing of an input box'''

        while not done:
            



    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)
