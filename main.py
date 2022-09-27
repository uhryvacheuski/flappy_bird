from time import sleep
import pygame, sys
from pygame.locals import *
from pipe import *
from land import *
from bird import *
        

def main():
    WINDOW_HEIGHT = 800 
    WINDOW_WIDTH = 600

    pygame.init()
    color = (255,0,0)
    x = 400
    pipe_pos = x + 300
    DISPLAYSURF = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    pipe1 = Pipe(DISPLAYSURF,color, pipe_pos, 50, 280)
    pipe2 = Pipe(DISPLAYSURF,color, x, 50, 350) #min 60
    bird = Bird(DISPLAYSURF)
    land = Land(DISPLAYSURF,0 ,DISPLAYSURF.get_height()-25, DISPLAYSURF.get_width(), 25)
    pygame.display.set_caption('Hello World!')
    bird_gravity = 0
    
    while True: # main game loop

        pipe_pos += 0.1

        pipe1.update(pipe_pos)
        pipe2.update(pipe_pos)
        bird.update(bird_gravity)

        pygame.time.delay(50)
        DISPLAYSURF.fill((0,0,0))

        pipe1.draw()
        pipe2.draw()
        bird.draw()
        pipe1.is_collision(bird.bird_point)
        pipe2.is_collision(bird.bird_point)

        land.draw()

        bird_gravity = 7
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                bird_gravity = -40
                pygame.event.clear()

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()