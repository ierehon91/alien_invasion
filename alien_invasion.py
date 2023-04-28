import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen, ai_settings)

    bullets = Group()
    aliens = Group()
    stars = Group()

    for i in range(ai_settings.count_stars_on_screen):
        gf.create_star(screen, stars, ai_settings, ship)

    gf.create_fleet(screen, ai_settings, aliens, ship)
    # Запуск основного цикла игры
    while True:
        gf.check_events(ship, ai_settings, screen, bullets, stars)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_stars(stars, screen, ai_settings, ship)
        gf.update_aliens(aliens, ai_settings)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stars)

        
run_game()
