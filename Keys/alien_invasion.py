import pygame

from settings import Settings
import game_functions as gf

# 12-4 implementation
def run_test():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Key Testing")
    
    # Start the main loop for the test
    while True:
        gf.check_events()

run_test()
