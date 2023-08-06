import pygame

import gl

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(int(gl.SCREEN_WIDTH / 2), int(gl.SCREEN_HEIGHT / 2))
        self.vel = pygame.math.Vector2()
        self.speed = 200

        self.image = pygame.Surface([40, 40])
        self.image.fill(gl.color.white)

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.pos += self.vel * gl.delta_time
        self.pos = round(self.pos)
        self.rect.center = self.pos

        self.move()

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vel.x = -self.speed
        elif keys[pygame.K_d]:
            self.vel.x = self.speed
        else:
            self.vel.x = 0

        if keys[pygame.K_w]:
            self.vel.y = -self.speed
        elif keys[pygame.K_s]:
            self.vel.y = self.speed
        else:
            self.vel.y = 0