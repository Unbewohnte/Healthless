import pygame

class Surface:
    def __init__(self):
        self.width = 64 
        self.height = 64

    def killsurf(self):
        pass

    def place(self,window,surf_x,surf_y):
        pygame.draw.rect(window,(100,200,240),(surf_x,surf_y,self.width,self.height))
