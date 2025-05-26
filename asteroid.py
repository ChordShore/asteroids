import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.velocity = 0
        self.position = pygame.Vector2(x, y)
    
    def split(self):
        old_velocity = self.velocity
        old_radius = self.radius
        old_position = self.position
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        
        new_vector_1 = old_velocity.rotate(random_angle)
        new_vector_2 = old_velocity.rotate(-random_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(old_position.x, old_position.y, new_radius)
        new_asteroid_2 = Asteroid(old_position.x, old_position.y, new_radius)

        new_asteroid_1.velocity = new_vector_1 * 1.2
        new_asteroid_2.velocity = new_vector_2 * 1.2

        


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, delta_time):
       self.position += (self.velocity * delta_time)