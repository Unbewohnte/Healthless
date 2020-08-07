import pygame
from player import *
from bullets import Bullet



class Enemy:
    def __init__(self):
        self.enemy_x = 100
        self.enemy_y = 100
        self.en_width = 32 
        self.en_height = 64

    def draw(self,window,en_color,en_image):
        pygame.draw.rect(window,en_color,(self.enemy_x, self.enemy_y, self.en_width, self.en_height))
        window.blit(en_image,(self.enemy_x, self.enemy_y))
    def update(self):
        self.enemy_x += 3
        if self.enemy_x >= 600:
            self.enemy_x = 1
    def enemy_shoot(self):
        pass
