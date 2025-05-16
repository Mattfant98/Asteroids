import pygame
from player import *
from constants import *
from asteroidfield import *
from circleshape import *
from shot import *
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    Shot.containers = (shot_group, updatable_group, drawable_group)
    player_sprite = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable_group.update(dt)

        for asteroid in asteroid_group:
            for shot in shot_group:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()
            else:
                continue

        for asteroid in asteroid_group:
            if asteroid.collision(player_sprite):
                print("Game over!")
                exit()
            else:
                continue

        screen.fill("black")

       

        for obj in drawable_group:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
