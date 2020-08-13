import pygame
from beings import *

class Surface:
    def __init__(self,name):
        if str(name) == 'killsurf':
            self.width = windowX
            self.height = windowY
            self.color = (30,70,40)
        if str(name) == 'default':
            self.width = windowX/1.5
            self.height = windowY/1.5
            self.color = (50,20,60)

    def place(self,window,surf_x,surf_y):
        pygame.draw.rect(window,self.color,(surf_x,surf_y,self.width,self.height))
