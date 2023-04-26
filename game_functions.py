import sys
import pygame
from pygame import Surface
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet


def check_keydown_events(ship: Ship, event, ai_settings: Settings, screen: Surface, bullets: Group):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def check_keyup_events(ship: Ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship: Ship, ai_settings: Settings, screen: Surface, bullets: Group):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship, event, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)



def update_screen(ai_settings: Settings, screen: pygame.Surface, ship: Ship, bullets: Group):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets:
        bullet.draw_bullet()
    pygame.display.flip()
