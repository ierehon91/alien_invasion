import pygame


class Ship:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        # Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/ship.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Кажый новый корабль появляется по центру внизу экрана
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)