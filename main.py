import pygame

import gl
import world
import debug

pygame.init()

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([gl.SCREEN_WIDTH, gl.SCREEN_HEIGHT])
        pygame.display.set_caption("Project North")

        self.running = True
        self.clock = pygame.time.Clock()

        self.world = world.World()

        self.debug_interface = debug.DebugInterface()

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    self.debug_interface.toggle_active()

    def draw(self):
        self.screen.fill(gl.color.black)

        self.world.draw()

        if self.debug_interface.active:
            self.debug_interface.draw()

    def update(self):
        self.world.update()

        self.debug_interface.update(self.clock, self.world.player)

        pygame.display.update()
        gl.delta_time = self.clock.tick(gl.framerate) / 1000

if __name__ == '__main__':
    game = Game()
    game.start()
    pygame.quit()