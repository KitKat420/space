import pygame
from ship import Ship


class Alien(Ship):
    def __init__(self, asset_path, xpos, ypos):
        self.asset = asset_path
        super().__init__(self.asset, xpos, ypos)
        self.step = 5

    def move(self):
        self.entity_rect.x += self.step

        if self.entity_rect.x >= 675:
            self.step *= -1
            self.entity_rect.y += 10
        elif self.entity_rect.x <= 25:
            self.step *= -1
            self.entity_rect.y += 10
