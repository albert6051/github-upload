import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from catcher import Catcher
import game_functions as gf

# 13-5 & 13-6 implementation
def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Catch")
    
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    
    # Make a catcher, and ball group
    catcher =Catcher(ai_settings, screen)
    balls = Group()
    
    # Create the falling ball.
    gf.create_ball(ai_settings, screen, balls)

    # Start the main loop for the game.
    while True:
        # Check for any input events
        gf.check_events(catcher)
        
        # Keep updating the catcher and ball until gameover
        if stats.game_active:
            catcher.update()
            gf.update_ball(ai_settings, stats, screen, catcher, balls)
        
        gf.update_screen(ai_settings, screen, catcher, balls)

run_game()
