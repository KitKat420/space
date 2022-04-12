import pygame
from alien import Alien


class Ship(Alien):
    def __init__(self, image_path, image_hint):
        self.image = image_path
        self.hint = image_hint
        super().__init__(self.image, self.hint)

    def controls(self, key_pressed):
        if key_pressed[pygame.K_a]:
            self.asset_rect.x -= 5
        elif key_pressed[pygame.K_d]:
            self.asset_rect.x += 5
