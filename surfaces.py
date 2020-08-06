import pygame

class surface:
    def __init__(self,name):
        self.surf_name = name
        if self.surf_name == 'kill':
            killsurf()
            
    def killsurf(self):
        pass
