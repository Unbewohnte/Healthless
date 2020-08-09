import pygame
from player import *
from bullets import Bullet
from random import randint

windowX = 640
windowY = 640
enemy_bul_on_screen = []

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
    def enemy_shoot(self,window,start_color,bul_image): #Have NO IDEA how it`ll work
        new_bullet = Bullet(self.enemy_x + self.en_width/2, self.enemy_y + 10)
        enemy_bul_on_screen.append(new_bullet)
        if int(len(enemy_bul_on_screen)) > 0:
            for bullet in enemy_bul_on_screen:
                bullet.draw(window,start_color,bul_image)
                bullet.moveb()
                if bullet.bullet_y >= windowY +20:
                    enemy_bul_on_screen.remove(bullet)

    def out_of_area(self):
        if self.enemy_x > windowX or self.enemy_x < 0 or self.enemy_y > windowY or self.enemy_y < 0:
            return True
        else:
            return False

    def collision(self,enemy):
        for bullet in bullets_on_screen:
            if bullet.bullet_x + bullet.bullet_width/2 >= enemy.enemy_x and bullet.bullet_x + bullet.bullet_width/2 <= enemy.enemy_x + enemy.en_width and bullet.bullet_y <= enemy.enemy_y:
                enemy.enemy_x += randint(-50,50)
                enemy.enemy_y += randint(-50,50)
