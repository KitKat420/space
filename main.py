from turtle import back
import pygame
import sys

WIDTH, HEIGHT = 800, 600
ORIGIN = (0, 0)
BLACK = (0, 0, 0)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


background = pygame.image.load("./assets/background.jpg", "background-img")
scaled_bg = pygame.transform.scale(background, (800, 800))
ship = pygame.image.load("./assets/ship.png", "ship-img")
scaled_ship = pygame.transform.scale(ship, (100, 100))


def display():
    WINDOW.fill(BLACK)
    pygame.Surface.blit(WINDOW, scaled_bg, ORIGIN)
    pygame.Surface.blit(WINDOW, scaled_ship, ((
        WIDTH - scaled_ship.get_width()) / 2, 500))


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        display()
        pygame.display.flip()


main()
