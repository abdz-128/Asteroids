import pygame

# Screen settings
SW = 900
SH = 650

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game settings
FPS = 60
LIVES = 3

# Asset paths
BG_IMAGE = 'assets/images/starbg.png'
ALIEN_IMAGE = 'assets/images/alienShip.png'
PLAYER_IMAGE = 'assets/images/spaceRocket.png'
STAR_IMAGE = 'assets/images/star.png'
ASTEROID_IMAGES = {
    1: 'assets/images/asteroid50.png',
    2: 'assets/images/asteroid100.png',
    3: 'assets/images/asteroid150.png'
}

# Sound settings
SHOOT_SOUND = 'assets/sounds/shoot.wav'
BANG_LARGE_SOUND = 'assets/sounds/bangLarge.wav'
BANG_SMALL_SOUND = 'assets/sounds/bangSmall.wav'
SOUND_VOLUME = 0.25

# Font settings
FONT = 'comicsans'
FONT_SIZE = 30

# Initialize Pygame display
pygame.display.set_caption('Asteroids')
WIN = pygame.display.set_mode((SW, SH))