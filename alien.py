import pygame
from explosion import Explosion
# WINDOW DIMENSIONS
WIDTH, HEIGHT = 800, 600


class Alien:
    def __init__(self, char_asset, bullet_asset):
        self.char_asset = char_asset
        self.bullet_asset = bullet_asset
        # bullet asset stuff

        self.bullet = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load(bullet_asset), (100, 100)),
            180
        )

        # alien asset stuff
        self.asset = pygame.image.load(char_asset)
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
