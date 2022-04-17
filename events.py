import pygame
import sys
from camera_group import CameraGroup

from player import Player

class Events:
    def __init__(self):
        pass

    def check_events(self, player, camera_group):
        '''Checks for key and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event, player, camera_group)
            elif event.type == pygame.MOUSEWHEEL:
                camera_group.zoom_scale += event.y * 0.03

    def keydown_events(self, event, player: Player, camera_group: CameraGroup):
        '''Handles Keydown events'''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.direction.y = -1
            player.rect.center += player.direction * player.speed
            player.image = pygame.image.load("_IMGS/player_up.png")
        elif keys[pygame.K_DOWN]:
            player.direction.y = 1
            player.rect.center += player.direction * player.speed
            player.image = pygame.image.load("_IMGS/player_down.png")
        else:
            player.direction.y =  0    
        if keys[pygame.K_RIGHT]:
            player.direction.x = 1
            player.rect.center += player.direction * player.speed
            player.image = pygame.image.load("_IMGS/player_right.png")
        elif keys[pygame.K_LEFT]:
            player.direction.x = -1
            player.rect.center += player.direction * player.speed
            player.image = pygame.image.load("_IMGS/player_left.png")
        else:
            player.direction.x = 0
            player.rect.center += player.direction * player.speed
                # Quit
        if event.key == pygame.K_ESCAPE:
            sys.exit()