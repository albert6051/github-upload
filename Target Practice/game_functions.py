import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, stats, play_button, ship, bullets):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, play_button, ship, bullets, mouse_x, mouse_y)

def check_keydown_events(event, ai_settings, screen, stats, ship, bullets):
    # Respond to keypresses.
    if event.key == pygame.K_UP:
        # Set the movement flags moving_up to true when the up key is press
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Set the movement flags moving_down to true when the down key is press
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Create a bullet and add it to the bullets group
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        # Exit the screen with Q is press
        sys.exit()
    elif event.key == pygame.K_p:
        # Start the game with P is press
        start_game(ai_settings, stats, ship, bullets)

def check_keyup_events(event, ship):
    # Respond to key releases.
    if event.key == pygame.K_UP:
        # Set the movement flags moving_up to false when the up key is release
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        # Set the movement flags moving_down to false when the down key is release
        ship.moving_down = False

def update_screen(ai_settings, screen, stats, ship, character, bullets, target, play_button):
    # Update image on the screen and flip to the new screen
    # Redraw the screen for every pass through the loop
    screen.fill(ai_settings.bg_color)
    character.blitme()
    target.draw_target()
    ship.blitme()

    # Redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_settings, target, bullets, stats):
    # Update position of bullets and get rid of old bullets
    # Update bullet positions
    bullets.update()

    # Delete the bullets that have gone out of the screen
    for bullet in bullets.copy():
        if bullet.rect.centerx > ai_settings.screen_width:
            bullets.remove(bullet)
            target_miss(stats)


    check_bullet_target_collisions(ai_settings, target, bullets)

def check_bullet_target_collisions(ai_settings, target, bullets):
    # Check for any bullets that hit target
    # If so, get rid of the bullet and the target
    bullet = pygame.sprite.spritecollideany(target, bullets)
    if bullet != None:
        ai_settings.target_hit += 1
        bullets.remove(bullet)

    if ai_settings.target_hit == 3:
        # Destroy existing bullets, speed up game
        bullets.empty()
        ai_settings.increase_speed()
        ai_settings.target_hit = 0

def fire_bullet(ai_settings, screen, ship, bullets):
    # Fire a bullet if limit not reached yet.
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_play_button(ai_settings, stats, play_button, ship, bullets, mouse_x, mouse_y):
    # Start a new game when the player clicks Play
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        start_game(ai_settings, stats, ship, bullets)

def start_game(ai_settings, stats, ship, bullets):
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
    
        # Empty the list of aliens and bullets.
        bullets.empty()
        ship.center_ship()

def check_target_edges(ai_settings, target):
    # Respond appropriately if any target have reached an edge
    if target.check_edges():
        change_target_direction(ai_settings)

def change_target_direction(ai_settings):
    # Change the target's direction
    ai_settings.target_direction *= -1

def update_target(ai_settings, target):
    # Check if the target is at an edge,
    # and update the positions of the target
    check_target_edges(ai_settings, target)
    target.update()

def target_miss(stats):
    # Respond to target miss
    if stats.miss_left > 0:
        # Decrement ships_left
        stats.miss_left -= 1
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)