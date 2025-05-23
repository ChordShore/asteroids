from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 0
        self.position = pygame.Vector2(x, y)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, delta_time):
       self.position += (self.velocity * delta_time)