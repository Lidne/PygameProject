import pygame
from car import Car

if __name__ == '__main__':
    pygame.init()
    size = width, height = 620, 580
    road_size = width - 300, height
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Гонки 2D')
    clock = pygame.time.Clock()

    car = Car((width // 2) - 30, (height // 2) - 35, 100, 150)
    fps = 60
    running = True
    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == 1073741904:  # Влево
                    moving_left = True
                elif event.key == 1073741906:  # Вверх
                    moving_up = True
                elif event.key == 1073741903:  # Вправо
                    moving_right = True
                elif event.key == 1073741905:  # Вниз
                    moving_down = True
            if event.type == pygame.KEYUP:
                if event.key == 1073741904:  # Влево
                    moving_left = False
                elif event.key == 1073741906:  # Вверх
                    moving_up = False
                elif event.key == 1073741903:  # Вправо
                    moving_right = False
                elif event.key == 1073741905:  # Вниз
                    moving_down = False
        if moving_left:
            car.move_left(fps)
        if moving_up:
            car.move_up(fps)
        if moving_right:
            car.move_right(fps)
        if moving_down:
            car.move_down(fps)
        screen.fill((0, 0, 0))
        car.render(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
