import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats


def run_game():
    #inicjalizacja gry i utworzenie obiektu ekranu
    pygame.init()

    ai_settings=Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    #statek
    ship=Ship(ai_settings, screen)
    #obcy
    alien=Alien(ai_settings, screen)
    aliens=Group()
    #tworzenie floty obcych
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #utworzenie grupy do przechowywania pociskow
    bullets=Group()
    #egzemplarz przechowywania danych statystycznych
    stats = GameStats(ai_settings)

    while True:
        #oczekiwanie na naciśnięcie klawisza
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            #poruszanie sie
            ship.update()
            #poruszanie, kasowanie pociskow
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            #poruszanie obcych
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        #aktualizacja i wyswietlenie ekranu
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)





run_game()