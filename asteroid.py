
from circleshape import *
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),(self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def split(self):
        groups = self.groups()
        
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(random_angle)
        vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        New1 =Asteroid(self.position.x, self.position.y, new_radius)
        New1.velocity = vector1 *1.2
        New2 =Asteroid(self.position.x, self.position.y, new_radius)
        New2.velocity = vector2 * 1.2

        for group in groups:
            group.add(New1)
            group.add(New2)


        


    