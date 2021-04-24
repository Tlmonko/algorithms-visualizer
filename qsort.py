import pygame
from typing import List

WIDTH = 800
HEIGHT = 600
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("quick sort")
clock = pygame.time.Clock()

array = [5, 8, 23, 6, 9]


def draw_array(array: List[int], rect_size: int):
    global WIDTH, HEIGHT
    x_coord = (WIDTH - rect_size * len(array)) // 2
    for el in array:
        pygame.draw.rect(screen, (100, 100, 100), (x_coord,
                         HEIGHT - el * rect_size, rect_size, el * rect_size))
        x_coord += rect_size


def qsort(start_index, end_index):
    if end_index - start_index < 2:
        return
    global array
    less = []
    equals = []
    more = []
    num = array[start_index]
    for number in array[start_index: end_index]:
        if number < num:
            less.append(number)
        elif number == num:
            equals.append(number)
        else:
            more.append(number)
    array[start_index: end_index] = less + equals + more
    qsort(0, len(less))
    qsort(len(array) - len(more), len(array))


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
