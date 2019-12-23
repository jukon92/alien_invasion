import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        #wczytanie obrazu statku
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #pojawianie sie nowego statku kosmicznego
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #punkt środkowy statku jest przechowywany w liczbie zmiennoprzecinkowej
        self.center = float(self.rect.centerx)

        #opcje wskazujace na poruszanie sie statku
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """wysrodkowanie statku po kolizji z obcym"""
        self.center = self.screen_rect.centerx

    def update(self):
        #uaktualnienie polozenia statku na podstawie opcji wskazujacej na jego ruch
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        #wyswietlanie statku w jego aktualnym polozeniu
        self.screen.blit(self.image, self.rect)



