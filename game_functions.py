import sys
import random
import pygame
from pygame import Surface
from pygame.event import Event
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
from stars import Star


def check_keydown_events(
        ship: Ship,
        event: Event,
        ai_settings: Settings,
        screen: Surface,
        bullets: Group,
        stars: Group
        ):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, ai_settings, screen, ship)
    elif event.key == pygame.K_UP:
        ship.is_afterburner = True
            


def check_keyup_events(ship: Ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.is_afterburner = False


def check_events(ship: Ship, ai_settings: Settings, screen: Surface, bullets: Group, stars):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship, event, ai_settings, screen, bullets, stars)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)



def update_screen(
        ai_settings: Settings,
        screen: Surface,
        ship: Ship,
        bullets: Group,
        aliens: Group,
        stars: Group,
        ):
    screen.fill(ai_settings.bg_color)

    for star in stars:
        star.draw_star()

    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(bullets, aliens, screen, ai_settings, ship):
    bullets.update()

    for bullet in bullets.copy():
            if bullet.rect.y < 0:
                bullets.remove(bullet)
                
    check_bullet_alien_collision(bullets, aliens, screen, ai_settings, ship)


def check_bullet_alien_collision(bullets, aliens, screen, ai_settings, ship):
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(screen, ai_settings, aliens, ship)


def create_star(screen, stars, ai_settings, ship, new_star=False):
    x = random.randint(0, ai_settings.screen_width)
    if new_star:
        y = 0
    else:
        y = random.randint(0, ai_settings.screen_height)
    star = Star(screen, x, y, ai_settings, ship)
    stars.add(star)

def update_stars(stars, screen, ai_settings, ship):
    stars.update()

    for star in stars.copy():
        if star.rect.y > ai_settings.screen_height:
            stars.remove(star)
            create_star(screen, stars, ai_settings, ship, new_star=True)


def fire_bullet(bullets, ai_settings, screen, ship):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_alients_x(alien_width: float, ai_settings: Settings) -> int:
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    return int(available_space_x / (2 * alien_width))


def get_number_rows(alien_height: float, ship_heigt, ai_settings: Settings) -> int:
    avialable_space_y = ai_settings.screen_height - (alien_height * 6) - ship_heigt
    return int(avialable_space_y / (alien_height * 2))


def create_alien(
        screen: Surface,
        ai_settings: Settings,
        aliens: Group,
        alian_number: int,
        number_row: int
        ):
    alien = Alien(screen, ai_settings)
    alien.x = alien.rect.width + 2 * alien.rect.width * alian_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * number_row
    aliens.add(alien)


def create_fleet(screen: Surface, ai_settings: Settings, aliens: Group, ship: Ship):
    alien = Alien(screen, ai_settings)
    number_alients_x = get_number_alients_x(alien.rect.width, ai_settings)
    number_rows = get_number_rows(alien.rect.height, ship.rect.height, ai_settings)
    
    for number_row in range(number_rows):
        for i in range(number_alients_x):
            create_alien(screen, ai_settings, aliens, i, number_row)


def check_fleet_edgas(aliens: Group, ai_settings: Settings):
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(aliens, ai_settings)
            break


def change_fleet_direction(aliens: Group, ai_settings: Settings):
    for alien in aliens:
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(aliens: Group, ai_settings: Settings):
    check_fleet_edgas(aliens, ai_settings)
    aliens.update()
