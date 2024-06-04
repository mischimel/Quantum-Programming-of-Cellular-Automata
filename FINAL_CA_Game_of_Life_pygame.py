# Reference 1: https://editor.p5js.org/mischimel/sketches/g39n5NM9U (my code for Ex 7.7 from Daniel Shiffmann, with the help of ChatGPT)
# Reference 2: https://beltoforion.de/en/recreational_mathematics/game_of_life.php
# Reference 3: https://github.com/beltoforion/recreational_mathematics_with_python/blob/master/game_of_life.py

import numpy as np
import pygame

# Define cell size and window dimensions
cell_size = 8
window_width = 640
window_height = 480

# Calculate the number of columns and rows in the grid
columns = window_width // cell_size
rows = window_height // cell_size

# Initialize the grid with zeros using NumPy
grid = np.zeros((rows, columns))

# Define colours for representing cell states and grid lines
colour_alive = (200, 200, 225)  # Light purple
colour_dead = (10, 10, 40)       # Dark blue
colour_grid = (30, 30, 60)       # Lighter dark blue

# Function to initialise the grid with random cell states
def initialise_grid(grid):
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            grid[i, j] = np.random.randint(2)

# Function to compute the sum of neighbouring cell states
def compute_neighbourhood_sum(grid, i, j):
    sum = 0
    # Skip edge cells (first and last row and column)
    if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
        return None

    for x in range(max(0, i - 1), min(rows, i + 2)):
        for y in range(max(0, j - 1), min(columns, j + 2)):
            if (x, y) != (i, j):
                sum += grid[x, y]
    return sum

# Function to update the grid based on Conway's Game of Life rules
def update_generation(grid):
    new_grid = np.copy(grid)

    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            neighbourhood_sum = compute_neighbourhood_sum(grid, i, j)

            if grid[i, j] == 1 and (neighbourhood_sum < 2 or neighbourhood_sum > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbourhood_sum == 3:
                new_grid[i, j] = 1

    grid[:] = new_grid[:]

# Function to display the grid on the pygame surface
def display_grid(surface, grid):
    for i in range(rows):
        for j in range(columns):
            # Determine the colour based on cell state
            if grid[i, j] == 1:
                colour = colour_alive
            else:
                colour = colour_dead

            # Calculate position and size of each cell
            x = j * cell_size
            y = i * cell_size
            width = cell_size - 1
            height = cell_size - 1

            # Draw rectangle representing the cell
            pygame.draw.rect(surface, colour, (x, y, width, height))

# Initialize pygame and create a game window
pygame.init()
surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Conway's Game of Life")

# Initialise the grid with random cell states
initialise_grid(grid)

# Main game loop
while True:
    # Check for events and handle quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Fill the surface with grid line colour
    surface.fill(colour_grid)

    # Update the generation of the grid
    update_generation(grid)

    # Display the grid on the surface
    display_grid(surface, grid)

    # Update the display
    pygame.display.update()
