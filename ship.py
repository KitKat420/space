import pygame
from alien import Alien


class Ship(Alien):
    def __init__(self, image_path, image_hint):
        self.image = image_path
        self.hint = image_hint
        super().__init__(self.image, self.hint)
        load_bullet = pygame.image.load(
            './assets/bullet.png', 'bullet_img')
        self.bullet_asset = pygame.transform.scale(load_bullet, (100, 100))
        self.bullet_rect = self.bullet_asset.get_rect()
        self.did_fire = False

    def controls(self, key_pressed):
        """this function takes input from keyboard and performs actions based on the key pressed."""
        if key_pressed[pygame.K_a]:
            self.asset_rect.x -= 5
        elif key_pressed[pygame.K_d]:
            self.asset_rect.x += 5
