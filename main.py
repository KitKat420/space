import pygame
import sys
from ship import Ship
from alien import Alien

WIDTH, HEIGHT = 800, 600
ORIGIN = (0, 0)
BLACK = (0, 0, 0)
FPS = 60

pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load("./assets/background.jpg", "background-img")
scaled_bg = pygame.transform.scale(background, (1000, 1000))


ship = Ship('./assets/ship.png', 'ship_img')
alien = Alien('./assets/alien.png', 'alien_img')


def draw():
    WINDOW.fill(BLACK)
    WINDOW.blit(scaled_bg, ORIGIN)
    WINDOW.blit(ship.load_asset(), ship.asset_rect)
    WINDOW.blit(alien.load_asset(), alien.asset_rect)


def main():
    ship.asset_rect.x = 350
    ship.asset_rect.y = 500

    alien.asset_rect.x = 350
    alien.asset_rect.y = 20

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ship.controls(pygame.key.get_pressed())
        draw()
        pygame.display.flip()

        clock.tick(FPS)


main()
