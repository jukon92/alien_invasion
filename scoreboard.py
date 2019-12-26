import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """Klasa przeznaczona do przedstawiania informacji o punktacji"""
    def __init__(self, ai_settings, screen, stats):
        """inicalizacja atrybutow dotyczacych punktacji"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #ustawienia czcionki
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #przygotowanie poczatkowych obrazow z punktacja i aktualny poziom
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_level(self):
        """konwersja numeru poziomu na wygenerowany obraz"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        #wyswietlanie poziomu pod aktualnym wynikiem
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships (self):
        """Wyświetla liczbę statków jakie zostały graczowi"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def prep_score(self):
        """przeksztalcenie punktacji na wygenerowany obraz"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        #wyswietlanie puntkacji w prawym gornym rogu ekranu
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """konwersja najlepszego wyniku w grze na wygenerowany obraz"""
        rounded_high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        #wyswietlanie puntkacji w prawym gornym rogu ekranu
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.center = self.screen_rect.center
        self.high_score_rect.top = 20

    def show_score(self):
        """wyświetlenie punktacji, poziomu na ekranie"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #wyświetlanie statków
        self.ships.draw(self.screen)