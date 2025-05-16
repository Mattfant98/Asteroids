#This file holds the shot class which is for bullet projectiles. When a shot is created it is drawn and updated 
#with these functions via the main file.
from constants import SHOT_RADIUS
from circleshape import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
        
    def draw(self,screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, 0)

    def update(self, dt):
        self.position += (self.velocity * dt)