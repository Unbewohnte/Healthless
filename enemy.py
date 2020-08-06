import pygame
from player import *
from bullets import *



class Enemy:
    def __init__(self,enemy_x,enemy_y,en_width,en_height,en_damage,en_health):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.en_width = en_width
        self.en_height = en_height
        self.en_damage = en_damage
        self.en_health = en_health
    def draw(self,window,en_color,en_image):
        pygame.draw.rect(window,en_color,(self.enemy_x, self.enemy_y, self.en_width, self.en_height))
        window.blit(en_image,(self.enemy_x, self.enemy_y))
    def update(self):
        self.enemy_x += 3 
        if self.enemy_x >= 600:
            self.enemy_x = 1
    def enemy_shoot(self):
        pass
