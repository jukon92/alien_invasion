import sys
import pygame
#test gita

def check_keydown_events(event, ship):
    """reakcje na nacisniecie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # esc = wylaczenie
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_keyup_events(event, ship):
    """reakcje na zwolnienie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    #reakcja na zdarzenia generowane przez klawiature i mysz

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    #uaktualnienie obrazow oraz ich wyswietlenie

    # odswiezanie ekranu w kazdej iteracji petli
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # wyswietlanie ostatnio zmodyfikowanego ekranu
    pygame.display.flip()