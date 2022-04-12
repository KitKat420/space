import pygame
import sys
from game_asset import GameAsset

WIDTH, HEIGHT = 800, 600
ORIGIN = (0, 0)
BLACK = (0, 0, 0)
FPS = 60
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()
clock = pygame.time.Clock()

background = pygame.image.load("./assets/background.jpg", "background-img")
scaled_bg = pygame.transform.scale(background, (800, 800))


ship = GameAsset('./assets/ship.png', 'ship_img')
alien = GameAsset('./assets/alien.png', 'alien_img')


def rects():
    WINDOW.fill(BLACK)
    pygame.Surface.blit(WINDOW, scaled_bg, ORIGIN)
    pygame.Surface.blit(WINDOW, ship.load_asset(), ((
        WIDTH - ship.load_asset().get_width()) / 2, 500))
    pygame.Surface.blit(WINDOW, alien.load_asset(), ((
        WIDTH - ship.load_asset().get_width()) / 2, 20))


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        rects()
        pygame.display.flip()
        clock.tick(FPS)


main()
