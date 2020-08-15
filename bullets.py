import pygame
import random


bullets_on_screen = []
enemy_bul_on_screen = []

class Bullet:
    def __init__(self, bullet_x, bullet_y):
        self.bullet_x = bullet_x + random.randint(-9,9) # -8 -- 8
        self.bullet_y = bullet_y
        self.bullet_width = 4
        self.bullet_height = 12
        self.bullet_vel = random.randint(16,28)   #12 -- 22
        self.bullet_rect = pygame.Rect(self.bullet_x,self.bullet_y, self.bullet_width,self.bullet_height)
    def draw(self,window,start_color,bullet_image):
        self.rect = pygame.draw.rect(window,start_color,(self.bullet_x,self.bullet_y,self.bullet_width,self.bullet_height))
        window.blit(bullet_image,(self.bullet_x, self.bullet_y))
    def move(self):
        self.bullet_y -= self.bullet_vel
    def movedwn(self):
        self.bullet_y += self.bullet_vel
