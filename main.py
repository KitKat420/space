import pygame
import sys


WIDTH, HEIGHT = 800, 600
ORIGIN = (0, 0)
BLACK = (0, 0, 0)

pygame.init()

background_img = pygame.transform.scale(
    pygame.image.load('./assets/background.jpg'), (1000, 1000))

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space invaders")


def draw():
    WINDOW.fill(BLACK)
    WINDOW.blit(background_img, ORIGIN)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    draw()
    pygame.display.flip()
