import pygame
from pygame.sprite import Sprite
from settings import Settings
from ship import Ship


class Star(Sprite):
    def __init__(self, screen, x, y, ai_settings: Settings, ship: Ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(x, y, 1, 4)
        self.y = float(self.rect.y)
        self.speed = ai_settings.stars_speed
        self.ship = ship
    
    def draw_star(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)

    def update(self):
        if self.ship.is_afterburner:
            self.y += self.speed + 0.2
        else:
            self.y += self.speed
        self.rect.y = self.y
