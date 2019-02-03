import sys
from random import randint
import pygame
from ball import Ball

# 13-5 & 13-6 implementation
def check_keydown_events(event, catcher):
    # Respond to keypresses
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = True
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_keyup_events(event, catcher):
    # Respond to key releases
    if event.key == pygame.K_RIGHT:
        catcher.moving_right = False
    elif event.key == pygame.K_LEFT:
        catcher.moving_left = False

def check_events(catcher):
    # Respond to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, catcher)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, catcher)

def update_screen(ai_settings, screen, catcher, balls):
    # Update images on the screen, and flip to the new screen
    # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)
    catcher.blitme()
    balls.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()
    
def ball_miss(ai_settings, stats, screen, balls):
    # Respond to ball miss
    if stats.catcher_left > 0:
        # Decrement catcher_left
        stats.catcher_left -= 1
    else:
        stats.game_active = False
    
    # remove old ball and create a new ball
    balls.empty()
    create_ball(ai_settings, screen, balls)
    
def check_ball_bottom(ai_settings, stats, screen, balls):
    # Check if ball has reached the bottom of the screen
    screen_rect = screen.get_rect()
    for ball in balls:
        if ball.rect.bottom >= screen_rect.bottom:
            # The ball is miss call ball_miss method
            ball_miss(ai_settings, stats, screen, balls)
            
def update_ball(ai_settings, stats, screen, catcher, balls):
    # Update the ball position dring falling
    balls.update(ai_settings)
    
    # Look for ball-catcher collisions.
    if pygame.sprite.spritecollideany(catcher, balls):
        balls.empty()
        create_ball(ai_settings, screen, balls)

    # Look for ball hitting the bottom of the screen.
    check_ball_bottom(ai_settings, stats, screen, balls)
    
def create_ball(ai_settings, screen, balls):
    # Create an ball, and place it on the top
    ball = Ball(ai_settings, screen)
    # create random number to random assign ball's position on x-axis
    random_number = randint(30, 870)
    ball.x = random_number
    ball.rect.x = ball.x
    ball.rect.y = 0
    balls.add(ball)
