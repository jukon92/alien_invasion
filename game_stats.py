import pygame

class GameStats():
    """Monitorowanie danych statystycznych w grze 'Inwazja obcych' """
    def __init__(self, ai_settings):
        """inicjalizacja danych statystycznych"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #uruchomienie gry w stanie nieaktywnym
        self.game_active = False
        #najlepszy wynik
        self.high_score = 0

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, ktore moga zmieniac sie w trakcie gry"""
        self.ships_left = self.ai_settings.ships_left
        self.score = 0
        self.level = 1
