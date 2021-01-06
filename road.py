import pygame
import random
from load_image import load_image
from obstacles import WeakObstacle

FPS = 60


class RoadBlock(pygame.sprite.Sprite):
    image = load_image('road_test.png')  # Это временный спрайт для проверки наложения

    def __init__(self, x, y, *group):
        # Обращение к конструктору родительского класса и добавление спрайта в группы
        super().__init__(*group)
        self.image = RoadBlock.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.objects = pygame.sprite.Group()  # Группа спрайтов для объектов на блоке дороги

    def add_object(self):
        """Фугкция добавляет объект на блок дороги"""
        # eval(f"{random.choice(('Weak', 'Strong'))}Obstacle('container.png', self.rect, self.objects)")
        WeakObstacle(self.rect, self.objects)

    def update(self):
        """Функция обновляет позицию блока дороги"""
        self.rect = self.rect.move(0, 3)
        self.objects.update(3)

    def is_viewing(self):
        """Функция проверяет не выходит ли блок за границы экрана"""
        return self.rect.y <= 580
