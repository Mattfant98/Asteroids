#This is the main game loop that generates the screen and actually checks for collision in the game loop. 
#Objects are updated/redrawn every game loop(frame) which is 60FPS.
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
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
    channel = pygame.mixer.Channel(0)
    
    pygame.mixer.music.load("asteroids_theme.wav")
    pygame.mixer.music.play(-1, 0.0, 5000)
    pygame.mixer.music.set_volume(0.5)
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

        #checking for bullet/asteroid collision and despawns if true
        for asteroid in asteroid_group:
            for shot in shot_group:
                if asteroid.collision(shot):
                    break_sound = pygame.mixer.Sound("asteroid_break.wav")
                    break_sound.set_volume(0.5)
                    pygame.mixer.Sound.play(break_sound)
                    asteroid.split()             
                    shot.kill()
            else:
                continue

        #checking for player asteroid collision, exit if true 
        for asteroid in asteroid_group:
            if asteroid.collision(player_sprite):
                pygame.mixer.music.unload()
                pygame.mixer.quit()
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
