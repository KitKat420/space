import pygame
import sys
from ship import Ship
from alien import Alien

WIDTH, HEIGHT = 800, 600

CENTER_X = 350

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


ship_bullets = []
alien_bullets = []


def draw():
    WINDOW.fill(BLACK)
    WINDOW.blit(scaled_bg, ORIGIN)
    WINDOW.blit(ship.load_asset(), ship.asset_rect)
    WINDOW.blit(alien.load_asset(), alien.asset_rect)
    WINDOW.blit(ship.load_asset(), ship.asset_rect)

    bullet_as_rect = ship.bullet_asset.get_rect()
    bullet_group = (ship.bullet_asset, bullet_as_rect)

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        # assigning the ship current coordinates to the bullet asset
        bullet_group[1].x = ship.asset_rect.x
        bullet_group[1].y = ship.asset_rect.y

        # appending bullet to bullets list
        ship_bullets.append(bullet_group)

    for bullet in ship_bullets:
        WINDOW.blit(bullet[0], bullet[1])
        bullet[1].y -= 5

    for bullet in alien_bullets:
        WINDOW.blit(bullet[0], bullet[1])
        bullet[1].y += 2


def main():
    ship.asset_rect.x = CENTER_X
    ship.asset_rect.y = 500

    alien.asset_rect.x = CENTER_X
    alien.asset_rect.y = 20

    alien_bullet_as_rect = alien.alien_bullet_asset.get_rect()
    alien_b_group = (alien.alien_bullet_asset, alien_bullet_as_rect)

    my_event = pygame.USEREVENT + 1
    pygame.time.set_timer(my_event, 3000)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == my_event:
                alien_b_group[1].x = alien.asset_rect.x
                alien_b_group[1].y = alien.asset_rect.y
                alien_bullets.append(alien_b_group)

        ship.controls(pygame.key.get_pressed())
        alien.movement()
        draw()
        pygame.display.flip()
        clock.tick(FPS)


main()
