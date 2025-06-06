from circleshape import *
from constants import *

class Shot(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        for container in Shot.containers:
            container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),(self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt