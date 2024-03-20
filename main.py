import pygame

from src.Player.player import Player
from src.Player.player import Bullet
from src.Player.player_movement import player_movement

# Screen dimensions
SCREEN_HEIGHT, SCREEN_WIDTH = 900, 650
SCREEN = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption('Asteroids: Remastered')
clock = pygame.time.Clock()

# Image paths for each object
paths = {'background': 'assets/images/starbg.png',
         'alien_ship': 'assets/images/alienShip.png',
         'player_ship': 'assets/images/spaceRocket.png',
         'asteroid_large': 'assets/images/asteroid150.png',
         'asteroid_medium': 'assets/images/asteroid100.png',
         'asteroid_small': 'assets/images/asteroid50.png',
         'star': 'assets/images/star.png'}

background = pygame.transform.scale(pygame.image.load(paths['background']), (SCREEN_HEIGHT, SCREEN_WIDTH))
gameover = False

# Redraw function
def redraw_game_window(player, player_bullets):
    SCREEN.blit(background, (0, 0))
    player.draw(SCREEN)
    for b in player_bullets:
        b.draw(SCREEN)
    pygame.display.update()


# Main function
def main():
    global gameover
    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT, paths['player_ship'])
    player_bullets = []
    running = True

    while running:
        clock.tick(60)

        if not gameover:
            player.update_location(SCREEN_WIDTH, SCREEN_HEIGHT)
            player_movement(pygame, player, player_bullets)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not gameover:
                        player_bullets.append(Bullet(player))

        redraw_game_window(player, player_bullets)
    pygame.quit()

if __name__ == '__main__':
    main()
