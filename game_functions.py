import sys
import pygame
from bullet import Bullet
from alien import Alien
#test gita


#przyciski
def check_events(ai_settings, screen, ship, bullets):
    #reakcja na zdarzenia generowane przez klawiature i mysz

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

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


#pociski
def fire_bullet(ai_settings, screen, ship, bullets):
    """wystrzelenie pocusku, jesli nie przekroczono limitu"""
    if len(bullets) <= ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    """auktualnienie położenia pociskow i ich kasowanie"""
    bullets.update()

    #usuwanie
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


#tworzenie floty
def create_fleet(ai_settings, screen, ship, aliens):
    """utworzenie pelnej floty obcych"""
    #odlegosc miedzy obcymi jest rowna ich szerokosci
    alien = Alien(ai_settings, screen)
    #"siatka" statkow obcych, ile wierszy i kolumn
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #utworzenie floty
    for row_number in range(number_rows):
        #utworzenie jednego rzedu
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Utworzenie obcego i umieszczenie go w rzedzie"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_aliens_x(ai_settings, alien_width):
    """ustalanie liczbny obcych, ktorzy zmieszcza sie w rzedzie"""
    avalible_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(avalible_space_x / ( 2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Ustalenie ile rzedow obcych zmisci sie na ekranie"""
    avalible_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(avalible_space_y / (2 * alien_height))
    return number_rows


#poruszanie sie floty
def check_fleet_edges(ai_settings, aliens):
    """odpowiednia reakcja, gdy obcy dotrze do krawedzi ekranu"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Przesuniecie calej floty w dol i zmiana kierunku, w ktorym sie porusza"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1




def update_aliens(ai_settings, aliens):
    """sprawdzenie, czy flota znajduje sie przy krawedzi ekranu,
    a nastepnie uaktualnienie położenia wszystkich obcych we flocie"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def update_screen(ai_settings, screen, ship, aliens, bullets):
    #uaktualnienie obrazow oraz ich wyswietlenie

    # odswiezanie ekranu w kazdej iteracji petli
    screen.fill(ai_settings.bg_color)

    #wyswietlanie pociskow
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # wyswietlanie ostatnio zmodyfikowanego ekranu
    pygame.display.flip()