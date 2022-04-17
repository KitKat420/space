import pygame
import sys
from ship import Ship
from alien import Alien
from explosion import Explosion

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


ship = Ship('./assets/ship.png', './assets/bullet.png')
alien = Alien('./assets/alien.png', './assets/alien_bullet.png')
explosion_group = pygame.sprite.Group()
explosion = Explosion(CENTER_X + 50, (HEIGHT - 50) / 2)
explosion_group.add(explosion)


ship_bullets = []
alien_bullets = []


def draw_on_window():
    WINDOW.fill(BLACK)
    WINDOW.blit(scaled_bg, ORIGIN)
    WINDOW.blit(ship.load_asset(), ship.asset_rect)
    WINDOW.blit(alien.load_asset(), alien.asset_rect)
    WINDOW.blit(ship.load_asset(), ship.asset_rect)
    bullet_as_rect = ship.bullet.get_rect()
    bullet_group = (ship.bullet, bullet_as_rect)

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

    explosion_group.draw(WINDOW)

    explosion_group.update()


def main():
    ship.asset_rect.x = CENTER_X
    ship.asset_rect.y = 500

    alien.asset_rect.x = CENTER_X
    alien.asset_rect.y = 20

    my_event = pygame.USEREVENT + 1
    pygame.time.set_timer(my_event, 3000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == my_event:
                alien_bullet_as_rect = alien.bullet.get_rect()
                alien_t = (alien.bullet,
                           alien_bullet_as_rect)

                alien_t[1].x = alien.asset_rect.x
                alien_t[1].y = alien.asset_rect.y
                alien_bullets.append(alien_t)

        ship.controls(pygame.key.get_pressed())
        alien.movement()
        draw_on_window()
        pygame.display.flip()
        clock.tick(FPS)


main()
