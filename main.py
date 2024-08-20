import pygame 
from constants import *
from player import *        
from asteroidfield import *
from asteroid import *
from shot import Shot
import sys


def main():
    pygame.init()
    clock = pygame.time.Clock() 
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()
   

    Player.containers = (updatables, drawables)
        
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dis_key_repeat = pygame.key.set_repeat(0, 0)
        
        for item in updatables:
            item.update(dt)
        
        screen_color  = pygame.Surface.fill(screen, (0,0,0))

        for item in drawables:
            item.draw(screen)
        for asteroid in asteroids:
            if player.check_for_collision(asteroid) == True:
                sys.exit("Game over!")
            for bullet in shots:
                if bullet.check_for_collision(asteroid) == True:
                    asteroid.split()
                    bullet.kill()
        
        update = pygame.display.flip()
        dt = clock.tick(40) / 1000

if __name__ == "__main__":
    main()

