import pygame 
from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
        self.time = 0
        
# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        draw_player  = pygame.draw.polygon(screen,(255,255,255), self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()
            
        if keys[pygame.K_a]:
            self.rotate(-dt) 
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.time < 0:
                self.shoot()
        self.time -= dt

        

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_TURN_SPEED
        self.time = PLAYER_SHOOT_COOLDOWN

   
