import pygame


class GameAsset:
    def __init__(self, image_path, image_hint):
        self.image = image_path
        self.hint = image_hint

        self.asset = pygame.image.load(image_path, image_hint)

    def load_asset(self):
        return pygame.transform.scale(self.asset, (100, 100))
