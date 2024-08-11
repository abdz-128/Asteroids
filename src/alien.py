import pygame
import random
from config import *


class Alien:
    def __init__(self):
        self.img = pygame.image.load(ALIEN_IMAGE)
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
        return (self.x > SW + 150 or self.x + self.w < -100 or
                self.y > SH + 150 or self.y + self.h < -100)