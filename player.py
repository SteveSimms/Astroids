# import pygame
# from circleshape import CircleShape
# from constants import *

# class Player(CircleShape):
#     def __init__(self, x, y):
#         super().__init__(x, y, PLAYER_RADIUS)  # Example radius value
#         self.position = pygame.Vector2(x, y)
#         self.radius = PLAYER_RADIUS
#         self.rotation = 0
#         # Additional initialization code
    


# # To draw the player, override the draw method of CircleShape. It should take the screen object as a parameter, and call pygame.draw.polygon. It takes:
# def draw(self, screen):
#          pygame.draw.polygon(screen, "white", self.triangle(), 2)
         
# # in the player class
# def triangle(self):
#     forward = pygame.Vector2(0, 1).rotate(self.rotation)
#     right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
#     a = self.position + forward * self.radius
#     b = self.position - forward * self.radius - right
#     c = self.position - forward * self.radius + right
#     return [a, b, c]








import pygame
from constants import *
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]



