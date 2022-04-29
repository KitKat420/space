import pygame
STEP = 5


class Ship:

    def __init__(self, asset_path, xpos, ypos):
        # load entity asset
        self.asset = asset_path
        self.entity = pygame.transform.scale(
            pygame.image.load(asset_path), (100, 100))

        # entity position
        self.entity_rect = self.entity.get_rect()
        self.entity_rect.x = xpos - (self.entity_rect.width / 2)
        self.entity_rect.y = ypos

        # load bullet asset
        self.bullet = pygame.transform.scale(
            pygame.image.load("./assets/bullet.png"), (100, 100))
        self.bullet_rect = self.bullet.get_rect()

        # bullets
        self.bullets = []

    def move(self, key):
        if key[pygame.K_a] and self.entity_rect.x >= 25:
            self.entity_rect.x -= STEP
        elif key[pygame.K_d] and self.entity_rect.x <= 675:
            self.entity_rect.x += STEP

    def shoot(self, xpos, ypos):
        """This function receives 2 arguments: the current x position and current y position of the ship so that the bullet centers"""

        self.bullet_rect = self.bullet.get_rect()
        self.bullet_rect.x = xpos
        self.bullet_rect.y = ypos
        self.bullets.append((self.bullet, self.bullet_rect))
