import math
import pygame

# Player class
class Player(object):
    def __init__(self, SCREEN_HEIGHT, SCREEN_WIDTH, paths):
        self.img = pygame.transform.scale(pygame.image.load(paths), (70, 70))
        self.player_width, self.player_height = self.img.get_width(), self.img.get_height()
        self.x, self.y = SCREEN_WIDTH//2, SCREEN_HEIGHT//2

        # Rotating the ship
        self.angle = 0
        self.rotated_surface = pygame.transform.rotate(self.img, self.angle)
        self.rotated_rect = self.rotated_surface.get_rect()
        self.rotated_rect.center = (self.x, self.y)

        # 90 degrees to make the ship face upwards (Fixes offset)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))

        # Head of the ship
        self.head_x = self.x + self.cosine * self.player_width//2
        self.head_y = self.y - self.sine * self.player_height//2
        self.head = (self.head_x, self.head_y)

    def draw(self, SCREEN):
        # SCREEN.blit(self.img, [self.x, self.y, self.player_width, self.player_height])
        SCREEN.blit(self.rotated_surface, self.rotated_rect)

    def turn_left(self):
        # Rotates the ship to the left
        self.angle += 5
        self.rotated_surface = pygame.transform.rotate(self.img, self.angle)
        self.rotated_rect = self.rotated_surface.get_rect()
        self.rotated_rect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))

        # Head of the ship
        self.head_x = self.x + self.cosine * self.player_width//2
        self.head_y = self.y - self.sine * self.player_height//2
        self.head = (self.head_x, self.head_y)

    def turn_right(self):
        # Rotates the ship to the right
        self.angle -= 5
        self.rotated_surface = pygame.transform.rotate(self.img, self.angle)
        self.rotated_rect = self.rotated_surface.get_rect()
        self.rotated_rect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))

        # Head of the ship
        self.head_x = self.x + self.cosine * self.player_width//2
        self.head_y = self.y - self.sine * self.player_height//2
        self.head = (self.head_x, self.head_y)

    def move_forward(self):
        # Moves the ship forward
        self.x += self.cosine * 5
        self.y -= self.sine * 5

        # Rotates the ship to the direction it is moving
        self.rotated_surface = pygame.transform.rotate(self.img, self.angle)
        self.rotated_rect = self.rotated_surface.get_rect()
        self.rotated_rect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))

        # Head of the ship
        self.head_x = self.x + self.cosine * self.player_width // 2
        self.head_y = self.y - self.sine * self.player_height // 2
        self.head = (self.head_x, self.head_y)

    def move_backward(self):
        # Moves the ship backwards
        self.x -= self.cosine * 5
        self.y += self.sine * 5

        # Rotates the ship to the direction it is moving
        self.rotated_surface = pygame.transform.rotate(self.img, self.angle)
        self.rotated_rect = self.rotated_surface.get_rect()
        self.rotated_rect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))

        # Head of the ship
        self.head_x = self.x + self.cosine * self.player_width // 2
        self.head_y = self.y - self.sine * self.player_height // 2
        self.head = (self.head_x, self.head_y)

    def update_location(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        if self.x > SCREEN_WIDTH + 250:
            self.x = -50
        elif self.x < 0 - self.player_width:
            self.x = SCREEN_WIDTH + 250
        elif self.y < -50:
            self.y = SCREEN_HEIGHT
        elif self.y > SCREEN_HEIGHT + 50:
            self.y = 0


# Bullet class
class Bullet(object):
    def __init__(self, player):
        self.point = player.head
        self.x, self.y = self.point
        self.bullet_width, self.bullet_height = 4, 4
        self.cosine, self.sine = player.cosine, player.sine
        self.speed_x, self.speed_y = self.cosine * 10, -self.sine * 10

    def shoot(self):
        self.x += self.speed_x
        self.y += self.speed_y


    # def check_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT):
    #     if self.x < -200 or self.x > SCREEN_WIDTH or self.y > SCREEN_HEIGHT or self.y > -200:
    #         return True
    #     return False

    def draw(self, SCREEN):
        pygame.draw.rect(SCREEN, 'white', [self.x, self.y, self.bullet_width, self.bullet_height])
