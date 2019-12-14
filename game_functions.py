import sys
import pygame
from bullet import Bullet
#test gita

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """reakcje na nacisniecie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # esc = wylaczenie
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)



def check_keyup_events(event, ship):
    """reakcje na zwolnienie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    #reakcja na zdarzenia generowane przez klawiature i mysz

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def fire_bullet(ai_settings, screen, ship, bullets):
    """wystrzelenie pocusku, jesli nie przekroczono limitu"""
    if len(bullets) <= ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings, screen, ship, bullets):
    #uaktualnienie obrazow oraz ich wyswietlenie

    # odswiezanie ekranu w kazdej iteracji petli
    screen.fill(ai_settings.bg_color)

    #wyswietlanie pociskow
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # wyswietlanie ostatnio zmodyfikowanego ekranu
    pygame.display.flip()

def update_bullets(bullets):
    """auktualnienie położenia pociskow i ich kasowanie"""
    bullets.update()

#usuwanie
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))