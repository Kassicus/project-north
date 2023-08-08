import pygame

import gl
import loader

class UIInventory():
    def __init__(self, x: int, y: int, world: object):
        self.pos = pygame.math.Vector2(x, y)

        self.slots = pygame.sprite.Group()

        self.left_slot = LargeSlot(self.pos.x, self.pos.y, world)
        self.middle_slot = MediumSlot(self.pos.x + 100, self.pos.y, world)
        self.right_slot = SmallSlot(self.pos.x + 200, self.pos.y, world)

        self.slots.add(self.left_slot, self.middle_slot, self.right_slot)

    def has_space(self):
        if self.left_slot.item == None or self.middle_slot.item == None or self.right_slot.item == None:
            return True
        else:
            return False
        
    def add(self, item_name, item_count, item_ref):
        added = False

        for slot in self.slots:
            if added == False:
                if slot.item == item_name:
                    slot.count += 1
                    item_ref.kill()
                    added = True
                elif slot.item == None:
                    slot.item = item_name
                    slot.count = item_count
                    item_ref.kill()
                    added = True
                else:
                    print("Cannot be picked up")

    def draw(self, surface):
        self.slots.draw(surface)

    def update(self):
        self.slots.update()

class BaseSlot(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, world: object):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.display_surface = pygame.display.get_surface()
        self.world_ref = world

        self.font = pygame.font.SysFont("Courier", 20)

        self.item = None
        self.item_image = None

        self.max_items = 0
        self.max_weight = 0
        self.count = 0

        self.image = pygame.Surface([width, height])
        self.image.fill(gl.color.white)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        self.check_highlight()
        self.display_item()

    def check_highlight(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if self.pos.x < mouse_x < self.pos.x + self.rect.width:
            if self.pos.y < mouse_y < self.pos.y + self.rect.height:
                pygame.draw.rect(self.display_surface, gl.color.magenta, (self.pos.x, self.pos.y, self.rect.width, self.rect.height))

    def display_item(self):
        if self.item != None:
            self.item_image = loader.items[self.item]
            count = self.font.render(str(self.count), True, gl.color.black)

            self.display_surface.blit(self.item_image, (self.rect.centerx - self.item_image.get_width() / 2, self.rect.centery - self.item_image.get_height() / 2))
            self.display_surface.blit(count, (self.rect.right - count.get_width() - 5, self.rect.top + 5))

class TinySlot(BaseSlot):
    def __init__(self, x: int, y: int, world: object):
        super().__init__(x, y, 30, 30, world)

        self.max_items = 3
        self.max_weight = 1

class SmallSlot(BaseSlot):
    def __init__(self, x: int, y: int, world: object):
        super().__init__(x, y, 40, 40, world)

        self.max_items = 5
        self.max_weight = 3

class MediumSlot(BaseSlot):
    def __init__(self, x: int, y: int, world: object):
        super().__init__(x, y, 65, 65, world)

        self.max_items = 7
        self.max_weight = 5

class LargeSlot(BaseSlot):
    def __init__(self, x: int, y: int, world: object):
        super().__init__(x, y, 85, 85, world)

        self.max_items = 9
        self.max_weight = 15
