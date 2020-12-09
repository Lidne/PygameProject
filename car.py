import pygame


class Car:
    def __init__(self, pos_x: float, pos_y: float, v_x: int, v_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = v_x
        self.v_y = v_y

    def move_up(self, fps):
        self.pos_y -= self.v_y / fps

    def move_down(self, fps):
        self.pos_y += self.v_y / fps

    def move_left(self, fps):
        self.pos_x -= self.v_x / fps

    def move_right(self, fps):
        self.pos_x += self.v_x / fps

    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255),
                         (int(self.pos_x), int(self.pos_y), 50, 70))
