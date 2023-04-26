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

    # Запуск основного цикла игры
    while True:
        gf.check_events(ship, ai_settings, screen, bullets)
        ship.update()
        bullets.update()

        gf.update_screen(ai_settings, screen, ship, bullets)

        for bullet in bullets.copy():
            if bullet.rect.y < 0:
                bullets.remove(bullet)
        print(len(bullets))

run_game()
