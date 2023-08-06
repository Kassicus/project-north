import pygame

import gl

class OakTree(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, world: object):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.world_ref = world

        self.health = 2

        self.image = pygame.Surface([30, 240])
        self.image.fill(gl.color.green)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        if self.health <= 0:
            self.destroy()

    def destroy(self):
        child = FelledOakTree(self.pos.x, self.pos.y + self.rect.height / 2, self.world_ref)
        self.world_ref.camera.add(child)
        self.world_ref.tree_container.add(child)
        self.kill()

class FelledOakTree(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, world: object):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.world_ref = world

        self.image = pygame.Surface([240, 30])
        self.image.fill(gl.color.cyan)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        pass