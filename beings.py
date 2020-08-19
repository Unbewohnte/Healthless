import pygame
from random import randint
from time import time
from bullets import *
from particles import *
import time
import sys

############
windowX = 832
windowY = 832
############ imgs for player-enemy(self,bullet)
bullet_image = pygame.image.load('pics/second_bullet.png')
enemy_bul_img = pygame.image.load('pics/bullet.png')
enemy_image = pygame.image.load('pics/32x64.png')
player_image = pygame.image.load('pics/32x64.png')
############

class Player:
    def __init__(self):
        self.bul_cooldown = 14
        self.tp_cooldown = 100
        self.x = 300
        self.y = 300
        self.vel = 10
        self.height = 64
        self.width = 32
        self.player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x - self.vel > 5 :
        	self.x -= self.vel

        if keys[pygame.K_RIGHT] and self.x + self.vel < windowX- self.width - 5 :
        	self.x += self.vel

        if keys[pygame.K_UP] and self.y + self.height - self.vel > self.height + 5 :
        	self.y -= self.vel

        if keys[pygame.K_DOWN] and self.y + self.height + self.vel < windowY-15 :
        	self.y += self.vel

    def draw(self,window):
        pygame.draw.rect(window,(0,0,0),(self.x,self.y,self.width,self.height))
        window.blit(player_image,(self.x, self.y))
        self.player_rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def shoot(self,window):
        if self.bul_cooldown >= 1:
            self.bul_cooldown -= 2

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z] and self.bul_cooldown == 0:
            new_bullet = Bullet(self.x + self.width/2, self.y + 10)
            player_bullets_on_screen.append(new_bullet)
            self.bul_cooldown = 14

        if int(len(player_bullets_on_screen)) > 0:
            for bullet in player_bullets_on_screen:
                bullet.draw(window,(0,0,0),bullet_image)
                bullet.move("up")
                if bullet.bullet_rect[1] <= -20:
                    player_bullets_on_screen.remove(bullet)

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

    def out_of_area(self):
        if self.x + self.width > windowX or self.x < 0 or self.y+self.height > windowY or self.y < 0:
            return True
        else:
            return False
    def collision(self,window):
        for bullet in enemy_bul_on_screen:
            if self.player_rect.colliderect(bullet.bullet_rect):
                self.x += randint(-100*1.4,100*1.4)
                self.y += randint(-100*1.4,100*1.4)
                enemy_bul_on_screen.remove(bullet)
                for i in range(5):
                    particle = Particle(self.player_rect[0] + self.width/2, self.player_rect[1] + self.height)
                    particles_on_screen_p.append(particle)

        if len(particles_on_screen_p) != 0:
            for particle in particles_on_screen_p:
                particle.draw(window)
                particle.update("down")



class Enemy:
    def __init__(self,x,y):
        self.enemy_x = x #100
        self.enemy_y = y #100
        self.en_width = 32
        self.en_height = 64
        self.vel = 3
        self.bul_cooldown = 10
        self.alive = True
    def draw(self,window):
        pygame.draw.rect(window,(0,0,0),(self.enemy_x, self.enemy_y, self.en_width, self.en_height))
        window.blit(enemy_image,(self.enemy_x, self.enemy_y))
        self.enemy_rect = pygame.Rect(self.enemy_x, self.enemy_y, self.en_width, self.en_height) #Rect object for collision
    def move(self,side):
        if str(side) == "right":
            self.enemy_x += self.vel
        elif str(side) == "left":
            self.enemy_x -= self.vel
        elif str(side) == "up":
            self.enemy_y -= self.vel
        elif str(side) == "down":
            self.enemy_y += self.vel
    def enemy_shoot(self,window):
        if self.bul_cooldown >= 1:
            self.bul_cooldown -= 2

        if self.bul_cooldown <= 0:
            new_bullet = Bullet(self.enemy_x + self.en_width/2, self.enemy_y + 10)
            enemy_bul_on_screen.append(new_bullet)
            self.bul_cooldown = random.randint(6,14) #10

        if int(len(enemy_bul_on_screen)) > 0:
            for bullet in enemy_bul_on_screen:
                bullet.draw(window,(0,0,0),enemy_bul_img)
                bullet.move("down")
                if bullet.bullet_rect[1] >= windowY +20:
                    enemy_bul_on_screen.remove(bullet)

        #print('Bullets (Enemy,Player): ' + str(len(bullets_on_screen + enemy_bul_on_screen)))

    def out_of_area(self):
        if self.enemy_x > windowX+1 or self.enemy_x < -1 or self.enemy_y > windowY+1 or self.enemy_y < -1:
            return True
        else:
            return False

    def collision(self,window):
        for bullet in player_bullets_on_screen:
            if self.enemy_rect.colliderect(bullet.bullet_rect):
                player_bullets_on_screen.remove(bullet)
                self.enemy_x += randint(-100*1.4,100*1.4)
                self.enemy_y += randint(-100*1.4,100*1.4)
                for i in range(5):
                    particle = Particle(self.enemy_rect[0] + self.en_width/2, self.enemy_rect[1] + self.en_height)
                    particles_on_screen_e.append(particle)

        if len(particles_on_screen_e) != 0:
            for particle in particles_on_screen_e:
                particle.draw(window)
                particle.update("up")
