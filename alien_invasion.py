import sys

import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Alien Invasion')
    bg_color = (230, 230, 230)

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                sys.exit()
        
        # Отображение последнего кадра
        pygame.display.flip()

run_game()
