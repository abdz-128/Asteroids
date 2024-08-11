import pygame
import random
from config import *


class Star:
    def __init__(self):
        self.img = pygame.image.load(STAR_IMAGE)
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.ranPoint = random.choice([
            (random.randrange(0, SW - self.w), random.choice([-1 * self.h - 5, SH + 5])),
            (random.choice([-1 * self.w - 5, SW + 5]), random.randrange(0, SH - self.h))
        ])
        self.x, self.y = self.ranPoint
        self.xdir = 1 if self.x < SW // 2 else -1
        self.ydir = 1 if self.y < SH // 2 else -1
        self.xv = self.xdir * 2
        self.yv = self.ydir * 2
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def move(self):
        self.x += self.xv
        self.y += self.yv
        self.rect.x = self.x
        self.rect.y = self.y

    def is_off_screen(self):
        return (self.x < -100 - self.w or self.x > SW + 100 or
                self.y > SH + 100 or self.y < -100 - self.h)