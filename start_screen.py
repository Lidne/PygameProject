import sys
import pygame
from load_image import load_image
from car import Car
from button import Button

FPS = 50

pygame.init()
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen(screen):
    size = width, height = screen.get_rect().w, screen.get_rect().h
    intro_text = ["2D Гонки", "",
                  "Выберите машину"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, (255, 255, 255))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = width // 2 - intro_rect.w // 2
        text_coord += intro_rect.height
        fon.blit(string_rendered, intro_rect)

    car_sprites = pygame.sprite.Group()
    buttons = pygame.sprite.Group()
    btn = Button((200, 400), 'start_button.png', buttons)

    for i in range(4):
        Car((80 + i * 130, 200), load_image(f'car{i}.png'), car_sprites)

    selected_car = None
    selection_rect = pygame.Rect(-10, -10, 1, 1)

    while True:
        screen.blit(fon, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for car in car_sprites:
                    if car.rect.collidepoint(event.pos):
                        selected_car = car
                        selection_rect = selected_car.rect
                if btn.button_pressed(event.pos) and selected_car is not None:
                    return selected_car.image

        pygame.draw.rect(screen, (255, 255, 255), selection_rect)
        car_sprites.draw(screen)
        buttons.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
