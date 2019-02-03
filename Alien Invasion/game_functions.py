import sys
import pygame
from random import randint
from bullet import Bullet
from alien import Alien
from star import Star
from raindrop import Raindrop
from time import sleep

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 14-4 implementation
            # Write the high score to file before exit
            write_high_score(stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Respond to keypresses.
    if event.key == pygame.K_RIGHT:
        # Set the movement flags moving_right to true when the right key is press
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Set the movement flags moving_left to true when the left key is press
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # Set the movement flags moving_up to true when the up key is press
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Set the movement flags moving_down to true when the down key is press
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Create a bullet and add it to the bullets group
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        # 14-4 implementation
        # Exit the screen with Q is press
        # Write the high score to file before exit
        write_high_score(stats)
        sys.exit()
    # 14-1 implementation
    elif event.key == pygame.K_p:
        # Start the game with P is press
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_keyup_events(event, ship):
    # Respond to key releases.
    if event.key == pygame.K_RIGHT:
        # Set the movement flags moving_right to false when the right key is release
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Set the movement flags moving_left to false when the left key is release
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        # 12-3 implementation
        # Set the movement flags moving_up to false when the up key is release
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        # 12-3 implementation
        # Set the movement flags moving_down to false when the down key is release
        ship.moving_down = False

def update_screen(ai_settings, screen, stats, sb, ship, aliens, character, bullets, stars, raindrops, play_button):
    # Update image on the screen and flip to the new screen
    # Redraw the screen for every pass through the loop
    screen.fill(ai_settings.bg_color)
    character.blitme()
    raindrops.draw(screen)
    stars.draw(screen)
    aliens.draw(screen)
    ship.blitme()

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    # Draw the score information
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Update position of bullets and get rid of old bullets
    # Update bullet positions
    bullets.update()

    # Delete the bullets that have gone out of the screen
    for bullet in bullets.copy():
        if bullet.rect.centerx > ai_settings.screen_width:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Check for any bullets that have hit aliens
    # Get rid of the bullets and the aliens that collided, and score to your total score
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        # 14-6 implement sound effect for explosion when the aliens is hit
        ai_settings.explosion_sound.play()
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    
    # 14-5 implementation
    # If the entire fleet is destroyed, start a new level.
    if len(aliens) == 0:
        start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets)

# 14-5 implementation
def start_new_level(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Destroy existing bullets, speed up game
    bullets.empty()
    ai_settings.increase_speed()

    # Increase level
    stats.level += 1
    sb.prep_level()

    # Create new fleet
    create_fleet(ai_settings, screen, ship, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    # Fire a bullet if limit not reached yet.
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        # 14-6 implement sound effect for bullet when it is shoot
        ai_settings.shooting_sound.play()

def get_number_items_y(ai_settings, item_height):
    # Determine the number of items that fit in a column
    available_space_y = ai_settings.screen_height - 2 * item_height
    number_item_y = int(available_space_y / (2 * item_height))
    return number_item_y

def get_number_column(ai_settings, ship_width, item_width):
    # Determine the number of rows of items that fit on the screen
    available_space_x = (ai_settings.screen_width - (6 * item_width) - ship_width)
    number_column = int(available_space_x / (2 * item_width))
    return number_column

def create_item(item, items, item_number, column_number, rand_num):
    # Create an item and place it in the column
    # Use a random number to randomize the item position
    item_height = item.rect.height
    item.y = item_height + 2 * item_height * item_number + rand_num
    item.rect.y = item.y
    item.rect.x = 6 * item.rect.width + 2 * item.rect.width * column_number + rand_num
    items.add(item)
    
def create_fleet(ai_settings, screen, ship, aliens):
    # Create a full fleet of aliens
    # Create a alien and find the number of aliens in a column
    alien = Alien(ai_settings, screen)
    number_aliens_y = get_number_items_y(ai_settings, alien.rect.height)
    number_column = get_number_column(ai_settings, ship.rect.width, alien.rect.width)
    
    # Create a fleet of aliens
    for column_number in range(number_column):
        # Create an alien and place it in the column
        for alien_number in range(number_aliens_y):
            alien = Alien(ai_settings, screen)
            create_item(alien, aliens, alien_number, column_number, 0)

# 13-1 & 13-2 implementation
def create_stars(ai_settings, screen, ship, stars):
    # Create a grid of stars
    # Create a star and find the number of stars in a column
    star = Star(ai_settings, screen)
    number_stars_y = get_number_items_y(ai_settings, star.rect.height)
    number_column = get_number_column(ai_settings, ship.rect.width, star.rect.width)

    # Create a grid of stars
    for column_number in range(number_column):
        # Create an star and place it in the column
        for star_number in range(number_stars_y):
            star = Star(ai_settings, screen)
            # Create a random number to randomize the position of the stars
            random_number = randint(-60, 60)
            create_item(star, stars, star_number, column_number, random_number)

# 13-3 implementation
def create_raindrops(ai_settings, screen, ship, raindrops):
    # Create a grid of raindrops
    # Create a raindrop and find the number of raindrop in a column
    raindrop = Raindrop(ai_settings, screen)
    number_raindrops_y = get_number_items_y(ai_settings, raindrop.rect.height)
    number_column = get_number_column(ai_settings, ship.rect.width, raindrop.rect.width)

    # Create a grid of raindrops
    for column_number in range(number_column):
        # Create a raindrop and place it in the column
        for raindrop_number in range(number_raindrops_y):
            raindrop = Raindrop(ai_settings, screen)
            # Create a random number to randomize the position of the raindrops
            random_number = randint(-30, 30)
            create_item(raindrop, raindrops, raindrop_number, column_number, random_number)

# 13-4 implementation
def steady_rain(ai_settings, screen, ship, raindrops):
    # Create a raindrop and find the number of raindrop in a row
    raindrop = Raindrop(ai_settings, screen)
    number_column = get_number_column(ai_settings, ship.rect.width, raindrop.rect.width)

    # Create a row of raindrops
    for column_number in range(number_column):
        raindrop = Raindrop(ai_settings, screen)
        # Create a random number to randomize the position of the raindrops
        random_number = randint(-60, 60)
        create_item(raindrop, raindrops, 0, column_number, random_number)

def check_fleet_edges(ai_settings, aliens):
    # Respond appropriately if any aliens have reached an adge
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    # Forward the entire fleet and change the fleet's direction
    for alien in aliens.sprites():
        alien.rect.x -= ai_settings.fleet_forward_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Check if the fleet is at an edge,
    # and update the positions of all aliens in the fleet
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
    # Look for aliens hitting the bottom of the screen
    check_aliens_left(ai_settings, screen, stats, sb, ship, aliens, bullets)

def update_raindrop(ai_settings, screen, ship, raindrops):
    # Update position of raindrops and get rid of old raindrops
    # Update raindrops positions dwonward
    raindrops.update()

    if len(raindrops) < ai_settings.raindrop_allowed:
        steady_rain(ai_settings, screen, ship, raindrops)

    # Delete the raindrop that have gone out of the screen
    for raindrop in raindrops.copy():
        if raindrop.rect.centery > ai_settings.screen_height:
            raindrops.remove(raindrop)

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # 14-6 implement sound effect for explosion when the ship is hit
    ai_settings.explosion_sound.play()
    # Respond to ship being hit by alien
    if stats.ships_left > 0:
        # Decrement ships_left
        stats.ships_left -= 1

        # Update scoreboard
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_left(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Check if any aliens have reached the left of the screen
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.left <= screen_rect.left:
            # Treat this the same as if the ship got hit
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break
# 14-5 implementation
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    # Start a new game when the player clicks Play
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

# 14-1 $ 14-5 implementation
def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Start a new game with the method is call
    # Check if the game is off
    if not stats.game_active:
        # Reset the game speed settings
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # 14-5 implementation
        # Reset the scoreboard images.
        sb.prep_images()
    
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_high_score(stats, sb):
    # Check to see if there's a new high score
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

# 14-4 implementation
def write_high_score(stats):
    # Write the high_score into high_score.txt
    f = open('high_score.txt', 'w')
    f.write(str(stats.high_score))
    f.close()
