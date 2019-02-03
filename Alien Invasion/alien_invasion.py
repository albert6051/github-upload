import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from character import Character
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

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a character, a ship, a group of bullets, and a group of aliens.
    character = Character(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    stars = Group()
    raindrops = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create the grid of stars
    gf.create_stars(ai_settings, screen, ship, stars)

    # Create the grid of raindrop
    gf.create_raindrops(ai_settings, screen, ship, raindrops)

    # Main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        # update ship and bullets position
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_raindrop(ai_settings, screen, ship, raindrops)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, character, bullets, stars, raindrops, play_button)

run_game()