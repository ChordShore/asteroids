import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init
    clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    loop_number = 0

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    while loop_number == 0:
        #draw screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        #draw player
        updatable.update(delta_time)
        for drawable_items in drawable:
            drawable_items.draw(screen)
        for asteroid in asteroids:
            if asteroid.check_collision(player) == True:
                print("Game over!")
                sys.exit()

        #render functions
        delta_time = (clock.tick(60))/1000
        pygame.display.flip()



if __name__ == "__main__":
    main()