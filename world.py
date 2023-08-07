import pygame

import gl
import player
import camera
import tree
import inventory
import loader

class World():
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.camera = camera.PlayerCenterCamera(self.display_surface, loader.backgrounds["test"])
        self.player = player.Player()
        self.player_inventory = inventory.UIInventory(363, 900, self)

        self.collidables = pygame.sprite.Group()
        self.tree_container = pygame.sprite.Group()
        self.felled_tree_container = pygame.sprite.Group()
        self.log_container = pygame.sprite.Group()

        self.camera.add(self.player)

        self.tree_list = [[100, 400], [1200, 300]]

        self.create_trees(self.tree_list)

    def create_trees(self, tree_array: list):
        for point_array in range(len(tree_array)):
            t = tree.Tree(tree_array[point_array][0], tree_array[point_array][1], self)
            self.camera.add(t)
            self.tree_container.add(t)
            self.collidables.add(t)

    def check_trees_hit(self):
        mouse_x, mouse_y = pygame.mouse.get_pos() + gl.global_offset
        for tree in self.tree_container:
            if tree.rect.left < mouse_x < tree.rect.right:
                if tree.rect.top < mouse_y < tree.rect.bottom:
                    tree.health -= 1

    def check_felled_trees_hit(self):
        mouse_x, mouse_y = pygame.mouse.get_pos() + gl.global_offset
        for felled_tree in self.felled_tree_container:
            if felled_tree.rect.left < mouse_x < felled_tree.rect.right:
                if felled_tree.rect.top < mouse_y < felled_tree.rect.bottom:
                    felled_tree.health -= 1

    def draw(self):
        self.camera.camera_draw(self.player)
        self.player_inventory.draw(self.display_surface)

    def update(self):
        self.camera.update()
        self.player_inventory.update()
        self.tree_container.update()
        self.felled_tree_container.update()
        self.log_container.update()

        for event in gl.events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.check_trees_hit()
                    self.check_felled_trees_hit()
