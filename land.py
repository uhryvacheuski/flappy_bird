import pygame

class Land:
    def __init__(self, surface, x, y, w, h):
        self.surface = surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.draw()
        
    def draw(self):
        pygame.draw.rect(self.surface, (0,255,0), pygame.Rect(self.x, self.y, self.w, self.h))
