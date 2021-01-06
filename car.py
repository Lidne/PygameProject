import pygame
from load_image import load_image

FPS = 60

pygame.init()
screen = pygame.display.set_mode((620, 580))


class Car(pygame.sprite.Sprite):
    def __init__(self, cords, image, *group):
        # Обращение к конструктору родительского класса и добавление спрайта в группы
        super().__init__(*group)
        # Загружается переданная картинка
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = cords[0]
        self.rect.y = cords[1]
        self.v = 170  # Скорость машинки

    def update(self, *args):
        """Функция обновляет позицию машинки"""
        self.rect = self.rect.move(args[0], args[1])
