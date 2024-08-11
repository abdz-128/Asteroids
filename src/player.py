import pygame
import math
from config import *


class Player:
    def __init__(self):
        self.img = pygame.image.load(PLAYER_IMAGE)
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = SW // 2
        self.y = SH // 2
        self.angle = 0
        self.rotated_surf = pygame.transform.rotate(self.img, self.angle)
        self.rotated_rect = self.rotated_surf.get_rect()
        self.rotated_rect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def draw(self, win):
        win.blit(self.rotated_surf, self.rotated_rect)

    def turn_left(self):
        self.angle += 5
        self._recalculate()

    def turn_right(self):
        self.angle -= 5
        self._recalculate()

    def move_forward(self):
        self.x += self.cosine * 15
        self.y -= self.sine * 15
        self._recalculate()

    def _recalculate(self):
        self.rotated_surf = pygame.transform.rotate(self.img, self.angle)
        self.rotated_rect = self.rotated_surf.get_rect()
        self.rotated_rect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h // 2)

    def update_location(self):
        if self.x > SW + 50:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = SW
        elif self.y < -50:
            self.y = SH
        elif self.y > SH + 50:
            self.y = 0

    def collides_with(self, obj):
        return self.rotated_rect.colliderect(obj.rect)