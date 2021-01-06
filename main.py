import pygame
from car import Car
from road import RoadBlock
from start_screen import start_screen


if __name__ == '__main__':
    # Инициализация pygame и окна
    pygame.init()
    size = width, height = 620, 580
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Гонки 2D')
    clock = pygame.time.Clock()  # Инициализация "часов" для работы со временем

    # Инициализируем группы спрайтов
    all_sprites = pygame.sprite.Group()
    car_group = pygame.sprite.Group()
    road_blocks = pygame.sprite.Group()
    car_image = start_screen(screen)
    car = Car((141, 310), car_image, car_group)

    # Создаём первых 2 блока дороги
    [RoadBlock(0, i, all_sprites, road_blocks) for i in range(-580, 1, 580)]

    fps = 60
    game_is_playing = True
    running = True
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False

    while running:
        while game_is_playing:
            # Этот цикл для последующей реализации game over экрана и начала новой игры
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_is_playing = False
                # Если мы нажали кнопку и не отпустили,
                # то продолжаем двигаться
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        moving_up = True
                    if event.key == pygame.K_DOWN:
                        moving_down = True
                    if event.key == pygame.K_LEFT:
                        moving_left = True
                    if event.key == pygame.K_RIGHT:
                        moving_right = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        moving_up = False
                    if event.key == pygame.K_DOWN:
                        moving_down = False
                    if event.key == pygame.K_LEFT:
                        moving_left = False
                    if event.key == pygame.K_RIGHT:
                        moving_right = False
            # Двигаем машинку (можно попробовать реализовать через функцию update в классе Car)
            if moving_up:
                car_group.update(0, -car.v / fps)
            if moving_down:
                car_group.update(0, car.v / fps)
            if moving_left:
                car_group.update(-car.v / fps, 0)
            if moving_right:
                car_group.update(car.v / fps, 0)

            # Проверяем выходит ли один из блоков за нижнюю границу экрана
            for block in road_blocks:
                if not block.is_viewing():
                    road_blocks.remove(block)
                    RoadBlock(0, block.rect.y - 580 * 2, all_sprites, road_blocks).add_object()

            # Обновляем все группы спрайтов
            # Рисуем поочерёдно, чтобы одни спрайты не накладывались на другие
            road_blocks.update()
            road_blocks.draw(screen)
            for block in road_blocks:
                block.objects.draw(screen)
            car_group.draw(screen)
            # Отсчитываем 1/60 секунды для стабильного fps
            clock.tick(fps)
            pygame.display.flip()
    pygame.quit()
