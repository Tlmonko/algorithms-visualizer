import pygame
from typing import List


def draw_array(array: List[int], rect_size: int, WIDTH: int, HEIGHT: int, screen: pygame.display):
    x_coord = (WIDTH - rect_size * len(array)) // 2
    for el in array:
        pygame.draw.rect(screen, (100, 100, 100), (x_coord,
                         HEIGHT - el * rect_size, rect_size, el * rect_size))
        x_coord += rect_size
