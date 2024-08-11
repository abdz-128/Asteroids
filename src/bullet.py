import pygame
from config import *


class Bullet:
    def __init__(self, player):
        self.point = player.head
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 20
        self.yv = self.s * 20

    def move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw(self, win):
        pygame.draw.rect(win, WHITE, [self.x, self.y, self.w, self.h])

    def check_off_screen(self):
        return self.x < -50 or self.x > SW or self.y > SH or self.y < -50

    def collides_with(self, obj):
        return pygame.Rect(self.x, self.y, self.w, self.h).colliderect(obj.rect)