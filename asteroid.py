from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(position, velocity)
        self.x = x
        self.y = y
        self.radius = radius
        
    def draw(self, screen):
        pygame.draw.circle(self.x, self.y, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

