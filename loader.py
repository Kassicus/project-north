import pygame

backgrounds = {}

items = {}

def load_images():
    global backgrounds
    global items

    backgrounds = {
        "test": pygame.image.load("assets/test.png").convert_alpha()
    }

    items = {
        "raw_log": pygame.image.load("assets/items/raw_log.png").convert_alpha()
    }