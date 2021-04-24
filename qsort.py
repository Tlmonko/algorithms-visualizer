import pygame
from typing import List
from drawing import draw_array
import random

WIDTH = 800
HEIGHT = 600

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("quick sort")
clock = pygame.time.Clock()

array = [random.randint(0, 30) for x in range(40)]
array_states = [array.copy()]


def qsort(start_index, end_index):
    if end_index - start_index < 2:
        return
    global array
    less = []
    equals = []
    more = []
    num = array[start_index]
    for number in array[start_index:end_index]:
        if number < num:
            less.append(number)
        elif number == num:
            equals.append(number)
        else:
            more.append(number)
    array[start_index:end_index] = less + equals + more
    array_states.append(array.copy())
    qsort(start_index, start_index + len(less))
    qsort(end_index - len(more), end_index)


qsort(0, len(array))
state = 0
FPS = len(array_states) // 6
if not FPS:
    FPS = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255, 255, 255))
    draw_array(array_states[state], 10, WIDTH, HEIGHT, screen)
    pygame.display.flip()
    if state < len(array_states) - 1:
        state += 1
    clock.tick(FPS)

pygame.quit()
