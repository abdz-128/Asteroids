import math
import pygame
import random


# Asteroid Class
class Asteroid(object):
    def __init__(self, rank, SCREEN_WIDTH, SCREEN_HEIGHT, paths):
        self.rank = rank
        if self.rank == 1:
            img_path = paths['asteroid_small']
        elif self.rank == 2:
            img_path = paths['asteroid_medium']
        else:
            img_path = paths['asteroid_large']

        # Load the image
        self.img = pygame.image.load(img_path)

        # Optionally, scale the image here if needed
        # self.img = pygame.transform.scale(self.img, (desired_width, desired_height))

        self.asteroid_width, self.asteroid_height = 50 * rank, 50 * rank
        self.ranPoint = random.choice(
            [
                (random.randrange(0, SCREEN_WIDTH - self.asteroid_width),
                 random.choice([-1 * self.asteroid_height - 5, SCREEN_HEIGHT + 5])),
                (random.choice([-1 * self.asteroid_width - 5, SCREEN_WIDTH + 5]),
                 random.randrange(0, SCREEN_HEIGHT - self.asteroid_height))
            ]
        )
        self.x, self.y = self.ranPoint
        self.x_dir = 1 if self.x < SCREEN_WIDTH // 2 else -1
        self.y_dir = 1 if self.y < SCREEN_HEIGHT // 2 else -1
        self.x_speed, self.y_speed = (self.x_dir * random.randrange(0, 2),
                                      self.y_dir * random.randrange(0, 2))

    # Movement of the asteroids
    def asteroids_movement(self, asteroids):
        for a in asteroids:
            a.x += a.x_speed
            a.y += a.y_speed

    # Update the location of the asteroid
    def draw(self, SCREEN):
        SCREEN.blit(self.img, (self.x, self.y))
