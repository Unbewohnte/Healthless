import pygame
import bullets
from bullets import Bullet
import time
import sys

windowX = 600
windowY = 600

bullets_on_screen = []

class Player:
    def __init__(self,x,y,vel,height,width,health):
        self.x = x
        self.y = y
        self.vel = vel
        self.height = height
        self.width = width
        self.health = health

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

    def debug(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.x = 300
            self.y = 300

    # def check__health(self): ################################# Work with that
    #     if self.health <= 0:
    #         mainmenu.deathscreen()
