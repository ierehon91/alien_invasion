import sys
import pygame

from settings import Settings
from ship import Ship


def check_keydown_events(ship: Ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(ship: Ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship: Ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship, event)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)



def update_screen(ai_settings: Settings, screen: pygame.Surface, ship: Ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
