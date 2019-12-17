import pygame

class GameStats():
    """Monitorowanie danych statystycznych w grze 'Inwazja obcych' """
    def __init__(self, ai_settings):
        """inicjalizacja danych statystycznych"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Inicjalizacja danych statystycznych, ktore moga zmieniac sie w trakcie gry"""
        self.ships_left = self.ai_settings.ships_left

