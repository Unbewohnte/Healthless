import pygame
from beings import *

class Surface:
    def __init__(self,name):
        if str(name) == 'killsurf':
            self.width = windowX
            self.height = windowY
            self.color = (30,70,40)

    def place(self,window,surf_x,surf_y):
        pygame.draw.rect(window,self.color,(surf_x,surf_y,self.width,self.height))
