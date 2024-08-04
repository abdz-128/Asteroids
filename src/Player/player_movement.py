from src.Asteroids.asteroids import Asteroids

# Movement of the player
def player_movement(pygame, player, player_bullets, asteroids):
    for b in player_bullets:
        b.shoot()
        if b.y < 0:
            player_bullets.remove(b)

    for a in asteroids:
        a.x += a.x_velocity
        a.y += a.y_velocity

        # Bullet collision
        for b in player_bullets:
            if a.x <= b.x <= a.x + a.width or a.x <= b.x + b.width <= a.x + a.width:
                if a.y <= b.y <= a.y + a.height or a.y + a.height <= b.y + b.height <= a.y + a.height:
                    if a.rank == 3:
                        new_asteroid_1 = Asteroids(2, 650, 900)
                        new_asteroid_2 = Asteroids(2, 650, 900)
                        new_asteroid_1.x, new_asteroid_1.y = a.x, a.y
                        new_asteroid_2.x, new_asteroid_2.y = a.x, a.y
                        asteroids.append(new_asteroid_1)
                        asteroids.append(new_asteroid_2)
                    elif a.rank == 2:
                        new_asteroid_1 = Asteroids(1, 650, 900)
                        new_asteroid_2 = Asteroids(1, 650, 900)
                        new_asteroid_1.x, new_asteroid_1.y = a.x, a.y
                        new_asteroid_2.x, new_asteroid_2.y = a.x, a.y
                        asteroids.append(new_asteroid_1)
                        asteroids.append(new_asteroid_2)
                    asteroids.pop(asteroids.index(a))
                    player_bullets.pop(player_bullets.index(b))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.turn_left()
    if keys[pygame.K_RIGHT]:
        player.turn_right()
    if keys[pygame.K_UP]:
        player.move_forward()
    if keys[pygame.K_DOWN]:
        player.move_backward()

