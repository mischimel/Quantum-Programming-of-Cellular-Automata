# Reference 1: https://editor.p5js.org/mischimel/sketches/g39n5NM9U (my code for Ex 7.7 from Daniel Shiffmann, with the help of ChatGPT)
# Reference 2: https://beltoforion.de/en/recreational_mathematics/game_of_life.php
# Reference 3: https://github.com/beltoforion/recreational_mathematics_with_python/blob/master/game_of_life.py

import numpy as np
import pygame

cell_size = 8
window_width = 640
window_height = 480

columns = window_width // cell_size
rows = window_height // cell_size

grid = np.zeros((rows, columns))

colour_alive = (200, 200, 225)
colour_dead = (10, 10, 40)
colour_grid = (30, 30, 60)


def initialise_grid(gird):
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            gird[i, j] = np.random.randint(2)


def compute_neighbour_sum(grid, i, j):
    sum = 0
    # Skip edge cells (first and last row and column)
    if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
        return 0

    for x in range(max(0, i - 1), min(rows, i + 2)):
        for y in range(max(0, j - 1), min(columns, j + 2)):
            if (x, y) != (i, j):
                sum += grid[x, y]
    return sum


def update_generation(grid):
    new_grid = np.copy(grid)

    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            neighbour_sum = compute_neighbour_sum(grid, i, j)

            if grid[i, j] == 1 and (neighbour_sum < 2 or neighbour_sum > 3):
                new_grid[i, j] = 0

            elif grid[i, j] == 0 and neighbour_sum == 3:
                new_grid[i, j] = 1

    grid[:] = new_grid[:]


def display_grid(surface, grid):
    for i in range(rows):
        for j in range(columns):
            if grid[i, j] == 1:
                colour = colour_alive
            else:
                colour = colour_dead

            x = j * cell_size
            y = i * cell_size
            width = cell_size - 1
            height = cell_size - 1

            pygame.draw.rect(surface, colour, (x, y, width, height))


pygame.init()
surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Conway's Game of Life")

initialise_grid(grid)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    surface.fill(colour_grid)
    update_generation(grid)
    display_grid(surface, grid)
    pygame.display.update()