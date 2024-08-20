# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *



def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    

    def __init__(self, title):
        pygame.init()
        
       
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =  pygame.time.Clock()
    dt = 0
    
    while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
           return
        
    #  print("my first game loop")
     pygame.display.flip()
    
     
     dt =  clock.tick(60) / 1000.0
     print("dt:", dt)
   

if __name__ == "__main__":
    main()