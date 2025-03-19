# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import AsteroidField
import sys
from shot import *


def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))
        for object in drawable:
            object.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
           if asteroid.collision(player1):
               print("Game over!")
               sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()
       
        #limit framerate to 60 fps
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()