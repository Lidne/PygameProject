import pygame
from load_image import load_image

FPS = 60


class RoadBlock(pygame.sprite.Sprite):
    image = load_image('road.png')

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.image = RoadBlock.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.objects = pygame.sprite.Group()

    def add_object(self, obj):
        self.objects.add(obj)

    def update(self):
        self.rect = self.rect.move(0, 1)
        self.objects.update()
