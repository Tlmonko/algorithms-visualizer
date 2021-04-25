import pygame
from typing import List
from drawing import draw_array
import random

WIDTH = 800
HEIGHT = 600

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("bubble sort")
clock = pygame.time.Clock()

array = [random.randint(0, 500) for x in range(800)]
array_states = [array.copy()]


def bubble_sort():
    for i in range(len(array)):
        is_sorted = True
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                is_sorted = False
                array[j], array[j + 1] = array[j + 1], array[j]
            array_states.append(array.copy())
        if is_sorted:
            return


bubble_sort()
state = 0
FPS = len(array_states) // 6
if not FPS:
    FPS = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255, 255, 255))
    draw_array(array_states[state], 1, WIDTH, HEIGHT, screen)
    pygame.display.flip()
    if state < len(array_states) - 1:
        state += 1
    clock.tick(FPS)

pygame.quit()
