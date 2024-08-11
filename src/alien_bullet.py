import pygame
import math
from config import *


class AlienBullet:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.w = 4
        self.h = 4
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        dx, dy = player.x - self.x, player.y - self.y
        dist = math.hypot(dx, dy)
        self.xv = (dx / dist) * 5
        self.yv = (dy / dist) * 5

    def draw(self, win):
        pygame.draw.rect(win, WHITE, self.rect)

    def move(self):
        self.x += self.xv
        self.y += self.yv
        self.rect.x = self.x
        self.rect.y = self.y