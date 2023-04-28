import pygame
from pygame import Surface
from pygame.sprite import Sprite

from settings import Settings


class Alien(Sprite):

    SCALE_RATIO = 0.4748

    def __init__(self, screen: Surface, ai_settings: Settings):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(
            self.image,
            (self.ai_settings.alien_width, int(self.ai_settings.alien_width * self.SCALE_RATIO)),
            )
        self.image.set_colorkey((255, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

    def update(self):
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x
