import pygame


class Alien:
    def __init__(self, image_path, image_hint):
        self.image = image_path
        self.hint = image_hint
        self.asset = pygame.image.load(image_path, image_hint)
        self.asset_rect = self.asset.get_rect()

    def load_asset(self):
        return pygame.transform.scale(self.asset, (100, 100))
