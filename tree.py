import pygame

import gl

class OakTree(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, world: object):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.world_ref = world

        self.image = pygame.Surface([40, 240])
        self.image.fill(gl.color.green)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        pass
