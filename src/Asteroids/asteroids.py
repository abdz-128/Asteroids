import math
import random

import pygame

from src.asset_path import paths

class Asteroids(object):
    def __init__(self, rank, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.rank = rank
        if self.rank == 1:
            self.img = pygame.image.load(paths['asteroid_small'])
        elif self.rank == 2:
            self.img = pygame.image.load(paths['asteroid_medium'])
        elif self.rank == 3:
            self.img = pygame.image.load(paths['asteroid_large'])
        self.width, self.height = 50 * rank, 50 * rank
        self.ranPoint = random.choice(
            [
                (random.randrange(0, SCREEN_WIDTH - self.width),
                 random.choice([-1*self.height - 5, SCREEN_HEIGHT + 5])),
                (random.choice([-1*self.width - 5, SCREEN_WIDTH + 220]),
                 random.randrange(0, SCREEN_HEIGHT + 50 - self.height))
            ])
        self.x, self.y = self.ranPoint

        if self.x < SCREEN_WIDTH//2:
            self.x_dir = 1
        else:
            self.x_dir = -1

        if self.y < SCREEN_HEIGHT//2:
            self.y_dir = 1
        else:
            self.y_dir = -1

        self.x_velocity = self.x_dir * random.randint(1, 3)
        self.y_velocity = self.y_dir * random.randint(1, 3)

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


