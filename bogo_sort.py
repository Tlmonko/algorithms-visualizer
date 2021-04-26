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


def is_sorted(arr: List[int]) -> bool:
    for index in range(len(arr) - 1):
        if arr[index] > arr[index + 1]:
            return False
    return True

state = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255, 255, 255))
    if not is_sorted(array):
        random.shuffle(array)
    draw_array(array, 1, WIDTH, HEIGHT, screen)
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
