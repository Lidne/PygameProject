import os
import sys
import pygame

# Функция для загрузки спрайтов в pygame (НЕ ТРОГАТЬ!!)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def read_record(filename, coding='utf8'):
    with open(filename, encoding=coding, mode='r') as file:
        record = file.read().strip()
        if not record.isdigit():
            return None
    return int(record)


def write_record(filename, record, coding='utf-8'):
    with open(filename, encoding=coding, mode='w') as file:
        file.write(record)
