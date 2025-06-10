#file containing the asteroid class, which inherets from circleshape class
#draw actually draws the asteroid to the screen
#update updates the position of the asteroid. Position is a Vector2
#split will delete an asteroid if its the smallest type. If it is medium or large, it will break into 2 smaller asteroids and speed up
from circleshape import *
import pygame
import math
import random
from constants import ASTEROID_MIN_RADIUS, COLOR_LIST, PI

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = random.choice(COLOR_LIST)
        self.local_points = self.generate_lumpy_outline()

    def draw(self, screen):
        screen_points = [
            (self.position.x + x, self.position.y + y) for (x, y) in self.local_points
        ]
        pygame.draw.polygon(screen, self.color, screen_points, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20,50)
        new_vector_1 = self.velocity.rotate(angle)
        new_vector_2 = self.velocity.rotate(-1 * angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = new_vector_1 * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = new_vector_2 * 1.2
        
    def generate_lumpy_outline(self, point_count=20, roughness=0.1):
        angle_step = 2 * math.pi / point_count
        points = []

        for i in range(point_count):
            angle = i * angle_step
            noise = random.uniform(1 - roughness, 1 + roughness)
            r = self.radius * noise
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            points.append((x, y))

        return points

