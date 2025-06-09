# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# initiate different parts that will be needed
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    # create group for player
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # create group for asteroids
    asteroid_group = pygame.sprite.Group()
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    asteroid_field = AsteroidField()
    # create group for shots
    shots_group = pygame.sprite.Group()
    Shot.containers = (shots_group, updatable_group, drawable_group)


# main game loop
    while True:
        #check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        # update all objects
        updatable_group.update(dt)
        # move objects that have a move method
        for object in updatable_group:
            if hasattr(object, 'move'):
                object.move(dt)

        # draw all drawable objects
        for object in drawable_group:
            object.draw(screen)

        # check for collision with player
        for asteroid in asteroid_group:
            if player.collides_with(asteroid) == True:
                print("Game Over!")
                sys.exit()

        # check for shot collision with asteroids
        for asteroid in asteroid_group:
            for shot in shots_group:
                if shot.collides_with(asteroid) == True:
                    shot.kill()
                    asteroid.split()


        dt = game_clock.tick(60) / 1000
        
        
        pygame.display.flip()

if __name__ == "__main__":
    main()