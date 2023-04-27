import pygame
import random
from pygame.sprite import Sprite
from settings import Settings


class Star(Sprite):
    def __init__(self, screen, x, y, ai_settings: Settings):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(x, y, 1, 4)
        self.y = float(self.rect.y)
        self.speed = ai_settings.stars_speed
    
    def draw_star(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
