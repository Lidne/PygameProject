import pygame
from load_image import load_image

FPS = 60

pygame.init()
screen = pygame.display.set_mode((1, 1))


class Car(pygame.sprite.Sprite):
    image = load_image('car.png')
    image = pygame.transform.scale(image, (70, 50))
    image = pygame.transform.rotate(image, 90)
    # Пока что используем эту картинку для разработки
    # Рисовать позже будем

    def __init__(self, pos_x, pos_y, *group):
        super().__init__(*group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.v = 150

    def update(self, *args):
        self.rect = self.rect.move(args[0], args[1])
