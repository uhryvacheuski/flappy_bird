import random
import pygame

class Bird:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.bird_point = [100, 100]
        self.draw()

    def draw(self):
        self.bird = pygame.draw.circle(self.surface, (225,100,100), self.bird_point, 10, 3) #(r, g, b) is color, (x, y) is center, R is radius and w is the thickness of the circle border.
    
    def update(self,gravity):
        self.bird_point = [100, self.bird_point[1]+gravity]
