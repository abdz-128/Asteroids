import random
import pygame

from src.asset_path import paths
from src.Player.player import Player, Bullet
from src.Asteroids.asteroids import Asteroids
from src.Player.player_movement import player_movement

pygame.init()

# Screen dimensions
SCREEN_HEIGHT, SCREEN_WIDTH = 900, 650
SCREEN = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption('Asteroids: Remastered')
clock = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load(paths['background']), (SCREEN_HEIGHT, SCREEN_WIDTH))
gameover = False
lives = 3


# Redraw function
def redraw_game_window(player, player_bullets, asteroids):
    SCREEN.blit(background, (0, 0))
    font = pygame.font.SysFont('comicsans', 30)
    lives_text = font.render(f'Lives: {lives}', 1, (255, 255, 255))
    play_again = font.render('Press any key to play again', 1, (255, 255, 255))

    player.draw(SCREEN)
    for a in asteroids:
        a.draw(SCREEN)
    for b in player_bullets:
        b.draw(SCREEN)
    if gameover:
        SCREEN.blit(play_again, (SCREEN_HEIGHT // 2 - play_again.get_width() // 2, SCREEN_WIDTH // 2 - play_again.get_height() // 2))
    SCREEN.blit(lives_text, (10, 10))
    pygame.display.update()


# Main function
def main():
    global gameover
    global lives
    player = Player(SCREEN_HEIGHT, SCREEN_WIDTH)
    player_bullets = []
    asteroids = []
    counts = 0

    running = True

    while running:
        clock.tick(60)
        counts += 1

        if not gameover:
            if counts % 50 == 0:
                ran = random.choice([1, 1, 1, 2, 2, 3])
                asteroids.append(Asteroids(ran, SCREEN_WIDTH, SCREEN_HEIGHT))

            player.update_location(SCREEN_WIDTH, SCREEN_HEIGHT)
            gameover, lives = player_movement(pygame, player, player_bullets, asteroids, lives)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not gameover:
                        player_bullets.append(Bullet(player))
                    else:
                        gameover = False
                        lives = 3
                        asteroids.clear()

        redraw_game_window(player, player_bullets, asteroids)
    pygame.quit()

if __name__ == '__main__':
    main()
