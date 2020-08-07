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

class Player:
    def __init__(self):
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
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            new_bullet = Bullet(self.x + self.width/2, self.y + 10)
            bullets_on_screen.append(new_bullet)

        if int(len(bullets_on_screen)) > 0:
            for bullet in bullets_on_screen:
                bullet.draw(window,start_color,bul_image)
                bullet.move()
                if bullet.bullet_y <= -20:
                    bullets_on_screen.remove(bullet)
            print('Bullets: ' + str(len(bullets_on_screen)))

    def teleportation(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.x = randint(10,550)
            self.y = randint(10,550)
