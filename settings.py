class Settings:
    def __init__(self) -> None:

        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (15, 15, 15)

        # Параметры коробля игрока
        self.width_ship = 75
        self.ship_speed_factor = 1.8

        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 230, 230)
        self.bullets_allowed = 3
