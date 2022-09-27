import random
import pygame

class Pipe:
    def __init__(self, surface,color,x,w,h) -> None:
        self.x = x
        self.y = 0
        self.height = h
        self.width = w
        self.color = color
        self.surface = surface

        self.gap = random.randint(30,60)
        self.pos_upper = pygame.Rect(self.x, 0, self.width, self.height-self.gap)
        self.pos_lower = pygame.Rect(self.x, self.height+self.gap, self.width, self.surface.get_width()-self.height)
        self.draw()
    
    def update(self ,x):
        self.pos_upper.move_ip(-1,0)
        self.pos_lower.move_ip(-1,0)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.pos_upper)
        pygame.draw.rect(self.surface, (0,255,255),self.pos_lower)

    def __check_upper_collisions(self, mouse_x,mouse_y) -> bool:
        return self.__check_upper_y_collision(mouse_y) and self.__check_upper_x_collision(mouse_x)

    def __check_upper_x_collision(self, mouse_x) -> bool:
        return (mouse_x > self.pos_upper.x and mouse_x < self.pos_upper.x+self.width)

    def __check_upper_y_collision(self, mouse_y) -> bool:
        return (mouse_y>self.pos_upper.y and mouse_y < self.height-self.gap)

    def __check_lower_collisions(self, mouse_x, mouse_y) -> bool:
        return self.__check_lower_y_collision(mouse_y) and self.__check_lower_x_collision(mouse_x)


    def __check_lower_x_collision(self, mouse_x) -> bool:
        return (mouse_x > self.pos_lower.x and mouse_x < self.pos_lower.x+self.width)

    def __check_lower_y_collision(self, mouse_y) -> bool:
        return (mouse_y>self.pos_lower.y and mouse_y < self.surface.get_width()-self.height)


    def is_collision(self, bird) -> bool:
        mouse_x, mouse_y = bird

        if self.__check_upper_collisions(mouse_x, mouse_y) or self.__check_lower_collisions(mouse_x, mouse_y):
            pygame.draw.rect(self.surface, (225,0,0),(self.x + 10,100,30,30))
            return True
        else:
            pygame.draw.rect(self.surface, (0,255,0),(self.x + 10,100,30,30))
            return False


