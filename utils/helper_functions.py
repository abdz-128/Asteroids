import pygame


def load_image(path):
    return pygame.image.load(path)


def load_sound(path):
    return pygame.mixer.Sound(path)


def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))