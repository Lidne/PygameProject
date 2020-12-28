import pygame
import random
from load_image import load_image

FPS = 60


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image, parent_rect, *group):
        super().__init__(*group)
        self.image = load_image(image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(61 + parent_rect.x, 190 + parent_rect.x)
        self.rect.y = random.randint(0 + parent_rect.y, 515 + parent_rect.y)

    def update(self, *args):
        self.rect = self.rect.move(0, 1)
