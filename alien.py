from re import L
import pygame

# WINDOW DIMENSIONS
WIDTH, HEIGHT = 800, 600


class Alien:
    def __init__(self, image_path, image_hint):
        self.image = image_path
        self.hint = image_hint
        load_bullet = pygame.image.load(
            "./assets/alien_bullet.png", "alien_bullet_img")
        self.alien_bullet_asset = pygame.transform.scale(
            load_bullet, (100, 100))
        self.asset = pygame.image.load(image_path, image_hint)
        self.asset_rect = self.asset.get_rect()
        self.direction = 5

    def load_asset(self):
        return pygame.transform.scale(self.asset, (100, 100))

    def movement(self):
        """this function controls the aliens movement."""
        self.asset_rect.x += self.direction
        if self.asset_rect.x == WIDTH - 100:
            self.asset_rect.y += 10
            self.direction *= -1
        elif self.asset_rect.x == WIDTH - 800:
            self.asset_rect.y += 10
            self.direction *= -1
