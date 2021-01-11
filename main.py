import pygame
from car import Car
from road import RoadBlock
from start_screen import start_screen
from load_image import load_image

if __name__ == '__main__':
    # Инициализация pygame и окна
    pygame.init()
    size = width, height = 620, 580
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Гонки 2D')
    clock = pygame.time.Clock()
    health = 3
    event1 = pygame.USEREVENT + 1 
    pygame.time.set_timer(event1, 3000)
    HP = load_image('Item 3-1.png.png')  # Инициализация "часов" для работы со временем

    # Инициализируем группы спрайтов qwer
    all_sprites = pygame.sprite.Group()
    car_group = pygame.sprite.Group()
    road_blocks = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
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
            print(car.peresechenie(obstacles))
            # Этот цикл для последующей реализации game over экрана и начала новой игры
            screen.fill((0, 0, 0))
            for i in range(health):
                screen.blit(HP, (310 + 30 * i, 20))

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
                if event.type == event1:

                    list(road_blocks)[0].change_speed(1)
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
                    RoadBlock(0, block.rect.y - 580 * 2, all_sprites, road_blocks).add_object(obstacles)

            pere = car.peresechenie(obstacles)
            if pere is not None:
                obstacles.remove(pere)
                list(road_blocks)[0].change_speed(-2)
                
            font = pygame.font.Font(None, 25)
            screen.blit(font.render(f"Скорость: {RoadBlock.speed * 5}", 1, (255, 255, 255)), (330, 70))
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
