import pygame
import random
from config import *
from src.player import Player
from src.bullet import Bullet
from src.asteroid import Asteroid
from src.star import Star
from src.alien import Alien
from src.alien_bullet import AlienBullet


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.reset_game()
        self.load_sounds()

    def reset_game(self):
        self.gameover = False
        self.lives = LIVES
        self.score = 0
        self.high_score = 0
        self.rapid_fire = False
        self.rf_start = -1
        self.is_sound_on = True
        self.player_bullets = []
        self.asteroids = []
        self.stars = []
        self.aliens = []
        self.alien_bullets = []
        self.count = 0

    def load_sounds(self):
        self.shoot_sound = pygame.mixer.Sound(SHOOT_SOUND)
        self.bang_large_sound = pygame.mixer.Sound(BANG_LARGE_SOUND)
        self.bang_small_sound = pygame.mixer.Sound(BANG_SMALL_SOUND)
        for sound in [self.shoot_sound, self.bang_large_sound, self.bang_small_sound]:
            sound.set_volume(SOUND_VOLUME)

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            self.count += 1

            if not self.gameover:
                self.spawn_objects()
                self.update_game_objects()
                self.check_collisions()

            running = self.handle_events()

            self.draw()

        pygame.quit()

    def spawn_objects(self):
        if self.count % 50 == 0:
            self.asteroids.append(Asteroid(random.choice([1, 1, 1, 2, 2, 3])))
        if self.count % 1000 == 0:
            self.stars.append(Star())
        if self.count % 750 == 0:
            self.aliens.append(Alien())

    def update_game_objects(self):
        self.player.update_location()
        for bullet in self.player_bullets:
            bullet.move()
            if bullet.check_off_screen():
                self.player_bullets.remove(bullet)

        for asteroid in self.asteroids:
            asteroid.move()

        for star in self.stars:
            star.move()
            if star.is_off_screen():
                self.stars.remove(star)

        for alien in self.aliens:
            alien.move()
            if alien.is_off_screen():
                self.aliens.remove(alien)
            if self.count % 60 == 0:
                self.alien_bullets.append(AlienBullet(alien.x + alien.w // 2, alien.y + alien.h // 2, self.player))

        for bullet in self.alien_bullets:
            bullet.move()

        if self.rf_start != -1 and self.count - self.rf_start > 500:
            self.rapid_fire = False
            self.rf_start = -1

    def check_collisions(self):
        self.check_player_asteroid_collision()
        self.check_bullet_asteroid_collision()
        self.check_bullet_alien_collision()
        self.check_alien_bullet_player_collision()
        self.check_bullet_star_collision()

    def check_player_asteroid_collision(self):
        for asteroid in self.asteroids:
            if self.player.collides_with(asteroid):
                self.lives -= 1
                self.asteroids.remove(asteroid)
                if self.is_sound_on:
                    self.bang_large_sound.play()
                if self.lives <= 0:
                    self.gameover = True
                break

    def check_bullet_asteroid_collision(self):
        for bullet in self.player_bullets:
            for asteroid in self.asteroids:
                if bullet.collides_with(asteroid):
                    self.handle_asteroid_destruction(asteroid)
                    self.player_bullets.remove(bullet)
                    break

    def handle_asteroid_destruction(self, asteroid):
        if asteroid.rank == 3:
            self.score += 10
            self.spawn_smaller_asteroids(asteroid, 2)
            if self.is_sound_on:
                self.bang_large_sound.play()
        elif asteroid.rank == 2:
            self.score += 20
            self.spawn_smaller_asteroids(asteroid, 1)
            if self.is_sound_on:
                self.bang_small_sound.play()
        else:
            self.score += 30
            if self.is_sound_on:
                self.bang_small_sound.play()
        self.asteroids.remove(asteroid)

    def spawn_smaller_asteroids(self, asteroid, new_rank):
        for _ in range(2):
            new_asteroid = Asteroid(new_rank)
            new_asteroid.x = asteroid.x
            new_asteroid.y = asteroid.y
            self.asteroids.append(new_asteroid)

    def check_bullet_alien_collision(self):
        for bullet in self.player_bullets:
            for alien in self.aliens:
                if bullet.collides_with(alien):
                    self.aliens.remove(alien)
                    self.player_bullets.remove(bullet)
                    if self.is_sound_on:
                        self.bang_large_sound.play()
                    self.score += 50
                    break

    def check_alien_bullet_player_collision(self):
        for bullet in self.alien_bullets:
            if self.player.collides_with(bullet):
                self.lives -= 1
                self.alien_bullets.remove(bullet)
                if self.lives <= 0:
                    self.gameover = True
                break

    def check_bullet_star_collision(self):
        for bullet in self.player_bullets:
            for star in self.stars:
                if bullet.collides_with(star):
                    self.rapid_fire = True
                    self.rf_start = self.count
                    self.stars.remove(star)
                    self.player_bullets.remove(bullet)
                    break

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.gameover:
                        if not self.rapid_fire:
                            self.player_bullets.append(Bullet(self.player))
                            if self.is_sound_on:
                                self.shoot_sound.play()
                elif event.key == pygame.K_m:
                    self.is_sound_on = not self.is_sound_on
                elif event.key == pygame.K_TAB:
                    if self.gameover:
                        self.reset_game()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.turn_left()
        if keys[pygame.K_RIGHT]:
            self.player.turn_right()
        if keys[pygame.K_UP]:
            self.player.move_forward()
        if keys[pygame.K_SPACE] and self.rapid_fire:
            self.player_bullets.append(Bullet(self.player))
            if self.is_sound_on:
                self.shoot_sound.play()

        return True

    def draw(self):
        # Clear the entire screen with a black rectangle
        WIN.fill((0, 0, 0))

        # Draw the background image
        bg_image = pygame.image.load(BG_IMAGE)
        bg_image = pygame.transform.scale(bg_image, (SW, SH))
        WIN.blit(bg_image, (0, 0))

        self.player.draw(WIN)
        for obj in self.asteroids + self.player_bullets + self.stars + self.aliens + self.alien_bullets:
            obj.draw(WIN)

        self.draw_ui()
        pygame.display.update()

    def draw_ui(self):
        font = pygame.font.SysFont(FONT, FONT_SIZE)
        lives_text = font.render(f'Lives: {self.lives}', True, WHITE)
        score_text = font.render(f'Score: {self.score}', True, WHITE)
        high_score_text = font.render(f'High Score: {self.high_score}', True, WHITE)

        WIN.blit(lives_text, (25, 25))
        WIN.blit(score_text, (SW - score_text.get_width() - 25, 25))
        WIN.blit(high_score_text, (SW - high_score_text.get_width() - 25, 35 + score_text.get_height()))

        if self.rapid_fire:
            pygame.draw.rect(WIN, BLACK, [SW // 2 - 51, 19, 102, 22])
            pygame.draw.rect(WIN, WHITE, [SW // 2 - 50, 20, 100 - 100 * (self.count - self.rf_start) / 500, 20])

        if self.gameover:
            play_again_text = font.render('Press Tab to Play Again', True, WHITE)
            WIN.blit(play_again_text,
                     (SW // 2 - play_again_text.get_width() // 2, SH // 2 - play_again_text.get_height() // 2))