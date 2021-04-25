import pygame
from typing import List
from drawing import draw_array
import random
from math import log2

WIDTH = 800
HEIGHT = 600

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("merge sort")
clock = pygame.time.Clock()

array = [random.randint(0, 500) for x in range(800)]
start_array = array.copy()
array_states = []


def merge_sort(start_index, end_index, depth):
    global array, array_states
    if end_index - start_index == 2:
        if array[start_index] > array[end_index - 1]:
            array[start_index], array[end_index -
                                      1] = array[end_index - 1], array[start_index]
        if depth >= len(array_states):
            array_states += [[] for x in range(depth - len(array_states) + 1)]
        array_states[depth].append((array.copy(), start_index, end_index))
        return
    if end_index - start_index == 1:
        return
    middle = (end_index + start_index) // 2
    merge_sort(start_index, middle, depth + 1)
    merge_sort(middle, end_index, depth + 1)
    arr1 = array[start_index:middle]
    arr2 = array[middle: end_index]
    result_arr = []
    while len(result_arr) < end_index - start_index:
        if not arr1:
            result_arr += arr2
            continue
        if not arr2:
            result_arr += arr1
            continue
        el1 = arr1[0]
        el2 = arr2[0]
        if el1 < el2:
            result_arr.append(arr1.pop(0))
        else:
            result_arr.append(arr2.pop(0))
    if depth >= len(array_states):
        array_states += [[] for x in range(depth - len(array_states) + 1)]
    array[start_index:end_index] = result_arr.copy()
    array_states[depth].append((array.copy(), start_index, end_index))


merge_sort(0, len(array), 1)
array_states.append([(start_array.copy(), 0, len(array))])
state = len(array_states) - 1
FPS = len(array_states) // 6
if not FPS:
    FPS = 1
array_to_draw = array_states[state][0][0].copy()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255, 255, 255))
    for el in array_states[state]:
        (arr, index_start, index_end) = el
        array_to_draw[index_start:index_end] = arr[index_start:index_end]
    draw_array(array_to_draw, 1, WIDTH, HEIGHT, screen)
    pygame.display.flip()
    if state > 0:
        state -= 1
    clock.tick(FPS)

pygame.quit()
