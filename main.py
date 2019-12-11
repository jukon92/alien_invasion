import pygame

from settings import Settings
from ship import Ship
import game_functions as gf



def run_game():
    #inicjalizacja gry i utworzenie obiektu ekranu
    pygame.init()

    ai_settings=Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    ship=Ship(ai_settings, screen)


    while True:
        #oczekiwanie na naciśnięcie klawisza
        gf.check_events(ship)

        #poruszanie sie
        ship.update()

        #aktualizacja i wyswietlenie ekranu
        gf.update_screen(ai_settings, screen, ship)





run_game()