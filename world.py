import pygame

import gl
import player
import camera

class World():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.world_background = pygame.image.load("assets/test.png").convert_alpha()

        self.camera = camera.PlayerCenterCamera(self.display_surface, self.world_background)
        self.player = player.Player()

        self.camera.add(self.player)

    def draw(self):
        self.camera.camera_draw(self.player)

    def update(self):
        self.camera.update()