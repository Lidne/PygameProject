import pygame
from car import Car
from road import RoadBlock

# Понять почему это окно съезжает в угол

if __name__ == '__main__':
    pygame.init()
    size = width, height = 620, 580
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Гонки 2D')
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    car_group = pygame.sprite.Group()
    road_blocks = pygame.sprite.Group()
    car = Car(100, 150, car_group, all_sprites)
    for i in range(-580, 1160, 580):
        RoadBlock(0, i, all_sprites, road_blocks)
        print(i)
    fps = 60
    running = True

    moving_left = False
    moving_right = False
    moving_up = False
    moving_down = False

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    moving_up = True
                elif event.key == pygame.K_DOWN:
                    moving_down = True
                elif event.key == pygame.K_LEFT:
                    moving_left = True
                elif event.key == pygame.K_RIGHT:
                    moving_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    moving_up = False
                elif event.key == pygame.K_DOWN:
                    moving_down = False
                elif event.key == pygame.K_LEFT:
                    moving_left = False
                elif event.key == pygame.K_RIGHT:
                    moving_right = False
        if moving_up:
            car_group.update(0, -car.v / fps)
        if moving_down:
            car_group.update(0, car.v / fps)
        if moving_left:
            car_group.update(-car.v / fps, 0)
        if moving_right:
            car_group.update(car.v / fps, 0)
        road_blocks.update()
        road_blocks.draw(screen)
        car_group.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
