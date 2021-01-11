import pygame
import random
from load_image import load_image

FPS = 60


class WeakObstacle(pygame.sprite.Sprite):
    # Класс препятствий, которые при столкновении убавляют скорость
    def __init__(self, parent_rect, *group):
        super().__init__(*group)
        self.image = load_image(f'weak_obst_{random.randint(0, 1)}.png')
        # Тут в отличии от класса Car нужно передавать путь к картинке
        # Тут это не играет особой разницы, (в отличии от класса Car) так что можно поменять
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(61 + parent_rect.x, 190 + parent_rect.x)  # Генерируем случайное положение по x
        self.rect.y = random.randint(0 + parent_rect.y, 515 + parent_rect.y)  # Генерируем случайное положение по y

    def update(self, *args):
        self.rect = self.rect.move(0, args[0])


class StrongObstacle(pygame.sprite.Sprite):
    # Класс препятствий, которые при столкновении убавляют жизни
    def __init__(self, parent_rect, *group):
        super().__init__(*group)
        self.image = load_image(f'strong_obst_{random.randint(0, 1)}.png')  # Лучше пока не вызывать без картинок
        # Тут в отличии от класса Car нужно передавать путь к картинке
        # Тут это не играет особой разницы, (в отличии от класса Car) так что можно поменять
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(61 + parent_rect.x, 190 + parent_rect.x)  # Генерируем случайное положение по x
        self.rect.y = random.randint(0 + parent_rect.y, 515 + parent_rect.y)  # Генерируем случайное положение по y

    def update(self, *args):
        self.rect = self.rect.move(0, args[0])
