import pygame
from random import randint
from time import time
import bullets
from bullets import Bullet
import time
import sys

windowX = 640
windowY = 640
bullets_on_screen = []
enemy_bul_on_screen = []

class Player:
    def __init__(self):
        self.bul_cooldown = 50
        self.tp_cooldown = 100
        self.x = 300
        self.y = 300
        self.vel = 10
        self.height = 64
        self.width = 32

    def update(self,window,start_color,bul_image):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 5 :
        	self.x -= self.vel

        if keys[pygame.K_RIGHT] and self.x < windowX- self.width - 5 :
        	self.x += self.vel

        if keys[pygame.K_UP] and self.y + self.height > self.height + 5 :
        	self.y -= self.vel

        if keys[pygame.K_DOWN] and self.y + self.height < windowY-15 :
        	self.y += self.vel

    def draw(self,window,color,player_image):
        self.rect = pygame.draw.rect(window,color,(self.x,self.y,self.width,self.height))
        window.blit(player_image,(self.x, self.y))


    def shoot(self,window,start_color,bul_image):
        # if self.bul_cooldown >= 1: #With cooldown the game looks not so spicy.
        #     self.bul_cooldown -= 2 #Maybe it will be the matter of upgrades ?

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]: # and self.bul_cooldown == 0
            new_bullet = Bullet(self.x + self.width/2, self.y + 10)
            bullets_on_screen.append(new_bullet)
            #self.bul_cooldown = 20

        if int(len(bullets_on_screen)) > 0:
            for bullet in bullets_on_screen:
                bullet.draw(window,start_color,bul_image)
                bullet.move()
                if bullet.bullet_y <= -20:
                    bullets_on_screen.remove(bullet)
            print('Bullets: ' + str(len(bullets_on_screen)))

    def teleportation(self):
        self.vel = 10
        if self.tp_cooldown >= 1:
            self.tp_cooldown -= 2
            print('teleportation cooldown : '+ str(self.tp_cooldown))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and keys[pygame.K_UP] and self.tp_cooldown == 0: #forward-dash
            self.y -= self.height*2
            self.tp_cooldown = 100

        if keys[pygame.K_d] and keys[pygame.K_LEFT] and self.tp_cooldown == 0: #left-dash
            self.x -= self.height*2
            self.tp_cooldown = 100

        if keys[pygame.K_d] and keys[pygame.K_RIGHT] and self.tp_cooldown == 0: #right-dash
            self.x += self.height*2
            self.tp_cooldown = 100

        if keys[pygame.K_d] and keys[pygame.K_DOWN] and self.tp_cooldown == 0: #backward-dash
            self.y += self.height*2
            self.tp_cooldown = 100

        # if keys[pygame.K_d] and keys[pygame.K_DOWN] and keys[pygame.K_RIGHT] and self.tp_cooldown == 0: #back-right-dash
        #     self.y += self.height*2
        #     self.x += self.height*2
        #     self.tp_cooldown = 100

    def out_of_area(self):
        if self.x > windowX or self.x < 0 or self.y > windowY or self.y < 0:
            return True
        else:
            return False
    def collision(self):
        for bullet in enemy_bul_on_screen:
            if bullet.bullet_x + bullet.bullet_width/2 >= self.x and bullet.bullet_x + bullet.bullet_width/2 <= self.x + self.width and bullet.bullet_y <= self.y:
                self.x += randint(-50,50)
                self.y += randint(-50,50)



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

    def collision(self):
        for bullet in bullets_on_screen:
            # if bullet.bullet_x + bullet.bullet_width/2 >= enemy.enemy_x and bullet.bullet_x + bullet.bullet_width/2 <= enemy.enemy_x + enemy.en_width and bullet.bullet_y <= enemy.enemy_y:
            if bullet.bullet_x + bullet.bullet_width/2 >= self.enemy_x and bullet.bullet_x + bullet.bullet_width/2 <= self.enemy_x + self.en_width and bullet.bullet_y <= self.enemy_y:
                self.enemy_x += randint(-50,50)
                self.enemy_y += randint(-50,50)
