import pygame

import gl
import player
import camera
import tree

class World():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.world_background = pygame.image.load("assets/test.png").convert_alpha()

        self.camera = camera.PlayerCenterCamera(self.display_surface, self.world_background)
        self.player = player.Player()

        self.collidables = pygame.sprite.Group()
        self.tree_container = pygame.sprite.Group()

        self.camera.add(self.player)

        self.tree_list = [[100, 400], [1200, 300]]

        self.create_trees(self.tree_list)

    def create_trees(self, tree_array: list):
        for point_array in range(len(tree_array)):
            t = tree.OakTree(tree_array[point_array][0], tree_array[point_array][1], self)
            self.camera.add(t)
            self.tree_container.add(t)
            self.collidables.add(t)

    def draw(self):
        self.camera.camera_draw(self.player)

    def update(self):
        self.camera.update()
        self.tree_container.update()

        for event in gl.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos() + gl.global_offset
                for tree in self.tree_container:
                    if tree.pos.x < mouse_x < tree.pos.x + tree.rect.width:
                        if tree.pos.y < mouse_y < tree.pos.y + tree.rect.height:
                            tree.health -= 1
