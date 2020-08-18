import pygame
import random
from math import pow

player_bullets_on_screen = []
enemy_bul_on_screen = []

class Bullet:
    def __init__(self, bullet_x, bullet_y): # y = ax^2 + bx + c  __maybe ?)
        self.bullet_x = bullet_x + random.randint(-9,9)
        self.bullet_y = bullet_y
        self.bullet_width = 4
        self.bullet_height = 12
        self.bullet_vel = random.randint(24,36)   #16 -- 28

        self.bullet_rect = pygame.Rect(self.bullet_x,self.bullet_y,self.bullet_width,self.bullet_height)
    def draw(self,window,start_color,bullet_image):
        pygame.draw.rect(window,start_color,self.bullet_rect)
        window.blit(bullet_image,(self.bullet_rect[0],self.bullet_rect[1]))
    def move(self,side):
        if str(side) == "up":
            self.bullet_rect[1] -= self.bullet_vel
        if str(side) == "down":
            self.bullet_rect[1] += self.bullet_vel
