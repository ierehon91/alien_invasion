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
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 3

        # Парметры коробля пришельцев
        self.alien_width = 75
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 12
        self.fleet_direction = 1

        # Параметры звёзд на фоне
        self.stars_speed = 0.3
        self.stars_afterbern_speed = 2
        self.count_stars_on_screen = 50
