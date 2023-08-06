import pygame

class Colors():
    def __init__(self):
        self.black = pygame.Color(0, 0, 0, 255)
        self.white = pygame.Color(255, 255, 255, 255)
        self.red = pygame.Color(255, 0, 0, 255)
        self.green = pygame.Color(0, 255, 0, 255)
        self.blue = pygame.Color(0, 0, 255, 255)
        self.cyan = pygame.Color(0, 255, 255, 255)
        self.magenta = pygame.Color(255, 0, 255, 255)
        self.yellow = pygame.Color(255, 255, 0, 255)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

color = Colors()

delta_time = 0
framerate = 120

events = None

global_offset = pygame.math.Vector2()