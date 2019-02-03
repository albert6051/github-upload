import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from character import Character
from target import Target
import game_functions as gf

def run_game():
    # Initialize game
    pygame.init()
    ai_settings = Settings()
    # Create the screen
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button
    play_button = Button(screen, "Play")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Make a character, a ship, a group of bullets, and a group of aliens.
    character = Character(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    target = Target(ai_settings, screen)

    # Main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        # update ship and bullets position
        if stats.game_active:
            ship.update()
            gf.update_target(ai_settings, target)
            gf.update_bullets(ai_settings, target, bullets, stats)

        gf.update_screen(ai_settings, screen, stats, ship, character, bullets, target, play_button)

run_game()