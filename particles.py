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
        self.timer = 200
    def draw(self,window):
        for i in range(10):
            pygame.draw.rect(window,(255,255,255),(self.x + randint(-30,30), self.y + randint(-30,30), self.width, self.height))
    def update(self):
        for particle in particles_on_screen:
            self.timer -= 1
            #self.x += self.vel - randint(1,2)
            self.y += self.vel
            if particle.timer <= 0:
                particles_on_screen.remove(particle)
        #print('Particles :',str(len(particles_on_screen)))
