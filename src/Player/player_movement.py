# Movement of the player
def player_movement(pygame, player, player_bullets):
    for b in player_bullets:
        b.shoot()
        if b.y < 0:
            player_bullets.remove(b)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.turn_left()
    if keys[pygame.K_RIGHT]:
        player.turn_right()
    if keys[pygame.K_UP]:
        player.move_forward()
    if keys[pygame.K_DOWN]:
        player.move_backward()

