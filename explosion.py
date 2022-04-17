import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        # sprites: required property
        self.sprites = [
            pygame.transform.scale(pygame.image.load(
                f"./animation/explosion_1.png"), (50, 50)),
            pygame.transform.scale(pygame.image.load(
                f"./animation/explosion_2.png"), (50, 50)),
            pygame.transform.scale(pygame.image.load(
                f"./animation/explosion_3.png"), (50, 50))
        ]
        self.current_sprite = 0
        # image: required property
        self.image = self.sprites[self.current_sprite]
        # rect: required property
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)

    def update(self):
        self.current_sprite += 0.1

        if self.current_sprite >= 3:
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]
