class Settings():
    #klasa przeznaczona do przechowywania ustawien gry

    def __init__(self):
        #ustawienia gry
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #pocisk
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        #predkosc statku
        self.ship_speed_factor = 1.5