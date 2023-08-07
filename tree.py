import pygame
from random import randint

import gl

class Tree(pygame.sprite.Sprite):
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
        child = FelledTree(self.pos.x, self.pos.y + self.rect.height / 2, self.world_ref)
        self.world_ref.camera.add(child)
        self.world_ref.felled_tree_container.add(child)
        self.kill()

class FelledTree(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, world: object):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.world_ref = world

        self.health = 1

        self.image = pygame.Surface([240, 30])
        self.image.fill(gl.color.cyan)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        if self.health <= 0:
            self.destroy(randint(2, 5))

    def destroy(self, children: int):
        for x in range(children):
            child = RawLog(randint(self.pos.x - 15, self.pos.x + self.rect.width + 15), randint(self.pos.y - 15, self.pos.y + self.rect.height + 15), self.world_ref)
            self.world_ref.camera.add(child)
            self.world_ref.log_container.add(child)
            
        self.kill()

class RawLog(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, world: object):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.world_ref = world

        self.image = pygame.Surface([60, 30])
        self.image.fill(gl.color.red)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos() + gl.global_offset

        if self.rect.left < mouse_x < self.rect.right:
            if self.rect.top < mouse_y < self.rect.bottom:
                if pygame.mouse.get_pressed()[0]:
                    self.destroy()

    def destroy(self):    
        self.world_ref.player_inventory.add("raw_log", 1, self)