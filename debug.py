import pygame

import gl

class DebugInterface():
    def __init__(self):
        self.active = False

        self.font = pygame.font.SysFont("Courier", 12)

        self.fps_text = None
        self.mouse_text = None
        self.player_pos_text = None
        self.global_offset_text = None
        self.global_mouse_text = None

        self.fps_text_offset = 0
        self.mouse_text_offset = 0
        self.player_pos_text_offset = 0
        self.global_offset_text_offset = 0
        self.global_mouse_text_offset = 0

        self.display_surface = pygame.display.get_surface()

    def get_fps(self, clock: pygame.time.Clock):
        string = "FPS: " + str(int(clock.get_fps()))
        text = self.font.render(string, True, gl.color.yellow)

        offset = int(gl.SCREEN_WIDTH - text.get_width() - 10)

        return text, offset

    def get_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        string = "Mouse: " + str(mouse_x) + " " + str(mouse_y)
        text = self.font.render(string, True, gl.color.yellow)

        offset = int(gl.SCREEN_WIDTH - text.get_width() - 10)

        return text, offset
    
    def get_player_pos(self, player: pygame.sprite.Sprite):
        string = "Player: " + str(round(player.pos.x)) + " " + str(round(player.pos.y))
        text = self.font.render(string, True, gl.color.yellow)

        offset = int(gl.SCREEN_WIDTH - text.get_width() - 10)

        return text, offset
    
    def get_global_offset(self):
        string = "Global Offset: " + str(gl.global_offset.x) + " " + str(gl.global_offset.y)
        text = self.font.render(string, True, gl.color.yellow)

        offset = int(gl.SCREEN_WIDTH - text.get_width() - 10)

        return text, offset
    
    def get_global_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        string = "Global Mouse: " + str(mouse_x + gl.global_offset.x) + " " + str(mouse_y + gl.global_offset.y)
        text = self.font.render(string, True, gl.color.yellow)

        offset = int(gl.SCREEN_WIDTH - text.get_width() - 10)

        return text, offset
    
    def toggle_active(self):
        if self.active:
            self.active = False
        else:
            self.active = True

    def draw(self):
        self.display_surface.blit(self.fps_text, (self.fps_text_offset, 12))
        self.display_surface.blit(self.mouse_text, (self.mouse_text_offset, 24))
        self.display_surface.blit(self.player_pos_text, (self.player_pos_text_offset, 36))
        self.display_surface.blit(self.global_offset_text, (self.global_offset_text_offset, 48))
        self.display_surface.blit(self.global_mouse_text, (self.global_mouse_text_offset, 60))

    def update(self, clock: pygame.time.Clock, player: pygame.sprite.Sprite):
        self.fps_text, self.fps_text_offset = self.get_fps(clock)
        self.mouse_text, self.mouse_text_offset = self.get_mouse()
        self.player_pos_text, self.player_pos_text_offset = self.get_player_pos(player)
        self.global_offset_text, self.global_offset_text_offset = self.get_global_offset()
        self.global_mouse_text, self.global_mouse_text_offset = self.get_global_mouse()