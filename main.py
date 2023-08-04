import pygame

import gl
import world

pygame.init()

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([gl.SCREEN_WIDTH, gl.SCREEN_HEIGHT])
        pygame.display.set_caption("Project North")

        self.running = True
        self.clock = pygame.time.Clock()

        self.world = world.World()

    def start(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def events(self):
        gl.events = pygame.event.get()

        for event in gl.events:
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill(gl.color.black)

        self.world.draw()

    def update(self):
        self.world.update()

        pygame.display.update()
        gl.delta_time = self.clock.tick(gl.framerate) / 1000

if __name__ == '__main__':
    game = Game()
    game.start()
    pygame.quit()