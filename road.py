import pygame
import random
from load_image import load_image
from obstacles import WeakObstacle

FPS = 60


class RoadBlock(pygame.sprite.Sprite):
    image = load_image('road.png')  # Это временный спрайт для проверки наложения
    speed = 3
    def __init__(self, x, y, *group):
        # Обращение к конструктору родительского класса и добавление спрайта в группы
        super().__init__(*group)
        self.image = RoadBlock.image
        self.speed = RoadBlock.speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.objects = pygame.sprite.Group()  # Группа спрайтов для объектов на блоке дороги

    def add_object(self, *args):
        if args:
            WeakObstacle(self.rect, self.objects, *args)
        """Фугкция добавляет объект на блок дороги"""
        # eval(f"{random.choice(('Weak', 'Strong'))}Obstacle('container.png', self.rect, self.objects)")


    def update(self):
        """Функция обновляет позицию блока дороги"""
        self.rect = self.rect.move(0, RoadBlock.speed)
        self.objects.update(RoadBlock.speed)

    def change_speed(self, speedplus):
        if RoadBlock.speed < 30:
            RoadBlock.speed += speedplus



    def is_viewing(self):
        """Функция проверяет не выходит ли блок за границы экрана"""
        return self.rect.y <= 580
