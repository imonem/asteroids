import random
from logger import log_event
from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            self.velocity1 = pygame.math.Vector2.rotate(self.velocity, new_angle)
            self.velocity2 = pygame.math.Vector2.rotate(self.velocity, new_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid1.velocity = self.velocity1
            new_asteroid2.velocity = self.velocity2
