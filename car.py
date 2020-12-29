import pygame
from load_image import load_image

FPS = 60

pygame.init()
screen = pygame.display.set_mode((620, 580))


class Car(pygame.sprite.Sprite):
    # Пока что используем эту картинку для разработки
    # Рисовать позже будем

    def __init__(self, cords, image, *group):
        super().__init__(*group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = cords[0]
        self.rect.y = cords[1]
        self.v = 150

    def update(self, *args):
        self.rect = self.rect.move(args[0], args[1])
