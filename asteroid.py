import pygame
import random
from constants import * 
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x 
        self.y = y


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            random_angle = random.uniform(20,50)
            rotate_vect1 = pygame.Vector2(self.position.x, self.position.y).rotate(random_angle)
            rotate_vect2 = pygame.Vector2(self.position.x, self.position.y).rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            

            asteroid_split1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_split2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid_split1.velocity = rotate_vect1 * 0.3
            asteroid_split2.velocity = rotate_vect2 * 0.3
       
