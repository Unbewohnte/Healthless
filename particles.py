import pygame
from random import randint

particles_on_screen = []

class Particle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 4
        self.height = self.width
        self.vel = int(randint(0,3)/5)
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.timer = randint(10,40)
    def draw(self,window):
        for i in range(5): #+ randint(-30,30)
            pygame.draw.rect(window,(255,255,255),(self.rect[0] + randint(-30,30), self.rect[1] + randint(-30,30), self.rect[2], self.rect[3]))
    def update(self):
        for particle in particles_on_screen:
            self.timer -= 0.5
            #self.x += self.vel - randint(1,2)
            self.rect[1] += int(randint(-2,2)) #self.vel +
            self.rect[0] += int(randint(-1,1))
            if particle.timer <= 0:
                particles_on_screen.remove(particle)
        #print('Particles :',str(len(particles_on_screen)))
