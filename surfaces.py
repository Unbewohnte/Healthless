import pygame
#from beings import *
from settings import timesurf_image

class BuffRandomSurf:
    def __init__(self,surf_x,surf_y):
            self.x = surf_x
            self.y = surf_y
            self.width = 32
            self.height = 64
            self.color = (30,70,40)
            self.rect = pygame.Rect(self.x,self.y,self.width,self.height,)
    def place(self,window,surf_x,surf_y):
        pygame.draw.rect(window,self.color,self.rect)
    def collide(self,object):
        if self.rect.colliderect(object):
            return True
        else:
            return False

class SlowTimeSurf:
    def __init__(self,surf_x,surf_y):
        self.x = surf_x
        self.y = surf_y
        self.width = 32
        self.height = 64
        self.color = (0,0,0)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.switch = True
        self.activation_timer = 1000
    def place(self,window):
        pygame.draw.rect(window,self.color,self.rect)
        window.blit(timesurf_image,(self.rect[0], self.rect[1]))
    def collide(self,object):
        if self.rect.colliderect(object):
            return True
        else:
            return False
    def activate(self,enemy):
        if self.activation_timer > 0:
            self.activation_timer -= 1
            if enemy.vel <= 1:
                enemy.bul_cooldown += 0.5//enemy.vel #- 1
            if 0.3 <= enemy.vel:
                enemy.vel -= 0.03
            if self.activation_timer <= 500 and enemy.vel <= 3:
                enemy.vel += 0.043
        else:
            enemy.vel = 3
