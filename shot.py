from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        position = pygame.Vector2(x, y)
        velocity = pygame.Vector2(0, 0)
        super().__init__(position, velocity, SHOT_RADIUS)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt