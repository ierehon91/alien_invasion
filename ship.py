import pygame
from settings import Settings


class Ship:

    SCALE_RATIO = 1.62

    def __init__(self, screen: pygame.Surface, settings: Settings):
        self.screen = screen
        self.ai_settings = settings

        # Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(
            self.image,
            (self.ai_settings.width_ship, int(self.ai_settings.width_ship * self.SCALE_RATIO)),
            )
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # Кажый новый корабль появляется по центру внизу экрана
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >= self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center