import pygame
from level import Level

from player import Player

class CameraGroup(pygame.sprite.Group):

    def __init__(self) -> None:
        """ Initializes the camera group. """
        super().__init__()
        self.display_surface = pygame.display.get_surface()
		
        # camera offset 
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2


        # box setup
        self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surface.get_size()[0]  - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surface.get_size()[1]  - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l,t,w,h)

        # ground
        self.ground_surf = pygame.image.load('assets/_IMGS/portal.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))

        # camera speed
        self.keyboard_speed = 5
        self.mouse_speed = 0.2

        # zoom 
        self.zoom_scale = 1
        self.internal_surf_size = (7751,4360)
        self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(center = (self.half_w,self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h


    def center_target_camera(self, target: pygame.math.Vector2):
        """ Centers the camera on a target

        Args:
            target (pygame.math.Vector2): Target to center camera on.
        """
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h


    def custom_draw(self, player: Player, level: Level) -> None:
        """Draws player and level to internal surface and blits it to display surface with offset and zoom scale.

        Args:
            player (Player): Player to draw.
            level (Level): Level to draw.
        """
        # Camera is focussed on the player
        self.center_target_camera(player)

        # Camerais controlled by mouse
        #self.mouse_control()

        # Camera is controlled by keyboard
        #self.zoom_keyboard_control()

        self.internal_surf.blit(level.level_background, (0,0)) # internal background

		# ground 
        ground_offset = self.ground_rect.topleft - self.offset + self.internal_offset
        self.internal_surf.blit(self.ground_surf,ground_offset)

        # active elements
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
            self.internal_surf.blit(sprite.image,offset_pos)
        scaled_surf = pygame.transform.scale(self.internal_surf,self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center = (self.half_w,self.half_h))    
        self.display_surface.blit(scaled_surf,scaled_rect)