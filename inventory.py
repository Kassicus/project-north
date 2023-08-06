import pygame

import gl
import loader

class UIInventory():
    def __init__(self, x: int, y: int, world: object):
        self.pos = pygame.math.Vector2(x, y)

        self.slots = pygame.sprite.Group()

        self.left_slot = UISlot(self.pos.x, self.pos.y, 75, 75, world)
        self.middle_slot = UISlot(self.pos.x + 100, self.pos.y, 75, 75, world)
        self.right_slot = UISlot(self.pos.x + 200, self.pos.y, 75, 75, world)

        self.slots.add(self.left_slot, self.middle_slot, self.right_slot)

    def has_space(self):
        if self.left_slot.item == None or self.middle_slot.item == None or self.right_slot.item == None:
            return True
        else:
            return False
        
    def add(self, item_name, item_count):
        if self.left_slot.item == None:
            self.left_slot.item = item_name
            self.left_slot.count = item_count
        elif self.middle_slot.item == None:
            self.middle_slot.item = item_name
            self.middle_slot.count = item_count
        elif self.right_slot.item == None:
            self.right_slot.item = item_name
            self.right_slot.count = item_count
    

    def draw(self, surface):
        self.slots.draw(surface)

    def update(self):
        self.slots.update()

class UISlot(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, world: object):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.display_surface = pygame.display.get_surface()

        self.item = None
        self.count = 0

        self.item_image = None

        self.world_ref = world

        self.image = pygame.Surface([width, height])
        self.image.fill(gl.color.white)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        self.check_highlight()
        self.display_item()

    def display_item(self):
        if self.item != None:
            self.item_image = self.world_ref.item_images[self.item]

            self.display_surface.blit(self.item_image, (self.pos.x, self.pos.y))

    def check_highlight(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if self.pos.x < mouse_x < self.pos.x + self.rect.width:
            if self.pos.y < mouse_y < self.pos.y + self.rect.height:
                pygame.draw.rect(self.display_surface, gl.color.magenta, (self.pos.x, self.pos.y, self.rect.width, self.rect.height))