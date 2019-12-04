import pygame

class Ship():

    def __init__(self, screen):
        self. screen = screen

        #wczytanie obrazu statku
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #pojawianie sie nowego statku kosmicznego
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #opcje wskazujace na poruszanie sie statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #uaktualnienie polozenia statku na podstawie opcji wskazujacej na jego ruch
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1


    def blitme(self):
        #wyswietlanie statku w jego aktualnym polozeniu
        self.screen.blit(self.image, self.rect)



