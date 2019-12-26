class Settings():
    #klasa przeznaczona do przechowywania ustawien gry

    def __init__(self):
        #inicalizacja danych statystycznych gry
        #ekran
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #pocisk
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 4
        #statek
        self.ships_left = 3
        #obcy
        self.fleet_drop_speed = 100
        #przyspieszenie po pokonaniu floty
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initalize_dynamic_settings()

    def initalize_dynamic_settings(self):
        """inicalizacja ustawien, ktore ulegaja zmianie w trakcie gry"""
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 3

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """zmiana ustawien dotyczacych szybkosci"""
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)