import pygame

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
        self.v = 200  # Скорость машинки

    def update(self, *args):
        """Функция обновляет позицию машинки"""
        if not (self.rect.x + args[0] < 0 or self.rect.x + self.rect.w + args[0] > 320) and \
                not (self.rect.y + args[1] < 0 or self.rect.y + self.rect.h + args[1] > 580):
            self.rect = self.rect.move(args[0], args[1])
        if self.rect.x < 30:
            self.v = 100
            self.rect = self.rect.move(2, args[1] + 1)
        elif self.rect.x + self.rect.w > 290:
            self.v = 100
            self.rect = self.rect.move(-2, args[1] + 1)
        else:
            self.v = 200

    def intersection(self, group):
        sprite = pygame.sprite.spritecollideany(self, group)
        if sprite is not None:
            group.remove(sprite)
        return sprite
