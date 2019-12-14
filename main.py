import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group



def run_game():
    #inicjalizacja gry i utworzenie obiektu ekranu
    pygame.init()

    ai_settings=Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    ship=Ship(ai_settings, screen)
    #utworzenie grupy do przechowywania pociskow
    bullets=Group()


    while True:
        #oczekiwanie na naciśnięcie klawisza
        gf.check_events(ai_settings, screen, ship, bullets)

        #poruszanie sie
        ship.update()

        #poruszanie, kasowanie pociskow
        gf.update_bullets(bullets)

        #aktualizacja i wyswietlenie ekranu
        gf.update_screen(ai_settings, screen, ship, bullets)





run_game()