import pygame
from settings import timesurf_image, randsurf_image, gamefont, windowX

pygame.font.init()
surf_font = pygame.font.Font(gamefont, 46)

class BuffRandomSurf:
    def __init__(self,surf_x,surf_y):
            self.x = surf_x
            self.y = surf_y
            self.width = 32
            self.height = 64
            self.color = (30,70,40)
            self.switch = True
            self.activation_timer = 1500
            self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
            #self.timer_rect = pygame.Rect(100,730,self.activation_timer/6,6)

    def place(self,window):
        window.blit(randsurf_image,(self.rect[0],self.rect[1]))

    def collide(self,object):
        if self.rect.colliderect(object):
            return True
        else:
            return False

    def activate(self,window,player):
        self.timer_rect = pygame.Rect(windowX//2.5,730,self.activation_timer/4,6)
        if self.activation_timer > 0:
            self.activation_timer -= 1
            player.power_of_random = 3
            pygame.draw.rect(window,(255/(self.activation_timer+1),16*(self.activation_timer//100),10),self.timer_rect)
        else:
            player.power_of_random = 1
        #print(power_of_random : ',player.power_of_random)

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
