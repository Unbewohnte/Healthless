import pygame
from random import randint,randrange

particles_on_screen_e = []
particles_on_screen_p = []
class Particle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 4 #4
        self.height = self.width
        self.vel = int(randint(0,3)/5)
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.timer = randint(10,66)
    def draw(self,window):
        for i in range(5): #5
            pygame.draw.rect(window,(randint(200,255),randint(50,255),20),(self.rect[0] + randint(-35,35), self.rect[1] + randint(-30,30), self.rect[2], self.rect[3]))
    def update(self,side):
        if str(side) == "up":
            for particle in particles_on_screen_e:
                particle.timer -= 0.5
                #self.rect[1] -= (self.vel - randrange(-7,1))
                particle.rect[1] += (self.vel + randrange(-7,1))
                particle.rect[0] += (self.vel + randrange(-3,3))
                if particle.timer <= 0:
                    particles_on_screen_e.remove(particle)
        if str(side) == "down":
            for particle in particles_on_screen_p:
                particle.timer -= 0.5
                particle.rect[1] += (self.vel + randrange(-1,7))
                particle.rect[0] += (self.vel + randrange(-3,3))
                if particle.timer <= 0:
                    particles_on_screen_p.remove(particle)
