#this class is used for the player hitbox as well as asterioids and bullets.
#collision is basic and just checks if the distance between the center points of two circles is less than their summed radii.
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, collision_object):
        return self.position.distance_to(collision_object.position) <= (self.radius + collision_object.radius)