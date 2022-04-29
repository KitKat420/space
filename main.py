import pygame
import sys
from ship import Ship
from alien import Alien

# CONSTANTS
WIDTH, HEIGHT = 800, 600
ORIGIN = (0, 0)
BLACK = (0, 0, 0)
FPS = 60

pygame.init()

# OBJECTS
ship = Ship("./assets/ship.png", WIDTH / 2, HEIGHT / 2 + 200)
alien = Alien("./assets/alien.png", WIDTH / 2, HEIGHT / 2 - 300)
clock = pygame.time.Clock()

background_img = pygame.transform.scale(
    pygame.image.load('./assets/background.jpg'), (1000, 1000))

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space invaders")


def draw():
    WINDOW.fill(BLACK)
    WINDOW.blit(background_img, ORIGIN)
    WINDOW.blit(ship.entity, ship.entity_rect)
    WINDOW.blit(alien.entity, alien.entity_rect)
    if len(ship.bullets) != 0:
        for bullet in ship.bullets:
            WINDOW.blit(bullet[0], bullet[1])
            bullet[1].y -= 5


def main():
    while True:

        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            # SHOOTING FUNCTION WILL CHANGE LATER
            elif event.type == pygame.KEYUP and key_pressed[pygame.K_SPACE]:
                ship.shoot(ship.entity_rect.x, ship.entity_rect.y)
        draw()
        ship.move(key_pressed)
        alien.move()
        clock.tick(FPS)
        pygame.display.flip()


main()
