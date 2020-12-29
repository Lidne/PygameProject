import pygame
import os
from car import Car
from road import RoadBlock
from obstacles import Obstacle
from start_screen import start_screen

# Понять почему это окно съезжает в угол

if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    size = width, height = 620, 580
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Гонки 2D')
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    car_group = pygame.sprite.Group()
    road_blocks = pygame.sprite.Group()
    car_image = start_screen(screen)
    car = Car((155, 310), car_image, car_group)

    for i in range(-580, 1160, 580):
        RoadBlock(0, i, all_sprites, road_blocks)
        print(i)

    for block in road_blocks:
        for _ in range(2):
            block.add_object(Obstacle('container.png', block.rect, all_sprites))

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
        for block in road_blocks:
            block.objects.draw(screen)
            block.update()
        car_group.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
