from turtle import screensize
import pygame

class Gun():
    def __init__(self, screen): 
        """Инициализация пушки"""
        self.screen = screen
        self.image = pygame.image.load('C:\Users\Галина\Desktop\Космонавтика\Images\spaceship.png')
        self.rect = self.image.get_rect() 
        """Получили нашу картинку как обьект - прямоугольник"""
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def output(self):
        """Рисование пушки"""
        self.screen.blit(self.image, self.rect)
