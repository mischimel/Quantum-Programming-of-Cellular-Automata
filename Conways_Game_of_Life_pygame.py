# Reference 1: https://editor.p5js.org/mischimel/sketches/g39n5NM9U (my code for Ex 7.7 from Daniel Shiffmann, with the help of ChatGPT)
# Reference 2: https://beltoforion.de/en/recreational_mathematics/game_of_life.php
# Reference 3: https://github.com/beltoforion/recreational_mathematics_with_python/blob/master/game_of_life.py

import numpy as np  # Import numpy for handling the grid as a 2D array
import pygame  # Import the pygame library for creating the game window and drawing (Reference 2/3)

# Initialize variables
# 1) Set up the window
cell_size = 8  # Set cell size to 8 px, so a cell is a 8x8 px square
window_width = 640  # Window will be 640 px wide
window_height = 480  # Window will be 480 px tall
columns = window_width // cell_size  # 80 cells of size 8 px fit into the 640 px wide window
rows = window_height // cell_size  # 60 cells of size 8 px fit into the 480 px tall window
# 2) Create a 2D numpy array with dimensions (rows, columns), initialized with all elements set to 0
grid = np.zeros((rows, columns))  # Current generation of cells
# 3) Define color constants using RGB values for the pygame game window (Reference 2/3)
colour_alive = (200, 200, 225) # Alive cells will be light purple
colour_dead = (10, 10, 40) # Background (dead cells) will be dark blue
colour_grid = (30, 30, 60) # Grid lines will be lighter dark blue


""" 
# This code initializes the grid starting from the second row and second column (index 1) to 
# the second-to-last row and column. This approach avoids issues related to boundary conditions.

# Function to initialize the grid with random values (generation 0)
def initialize_grid(current_generation):
    # Loop through each row, starting from the second row (index 1) to the second-to-last row
    for i in range(1, rows - 1):
        # Loop through each column, starting from the second column (index 1) to the second-to-last column
        for j in range(1, columns - 1):
            # Assign a random value (0 or 1) to the cell at position (i, j)
            # np.random.randint(2) generates either 0 or 1
            current_generation[i, j] = np.random.randint(2)
"""


# Function to initialize the grid with random values (generation 0)
def initialize_grid(grid):
    for i in range(rows): # Loop through each row, starting from the first to the last row
        for j in range(columns): # Loop through each column, starting from the first to the last column
            grid[i, j] = np.random.randint(2) # Assign a random value (0 or 1) to the cell at position (i, j)


# Function to calculate the sum of neighbour's states
def compute_neighbour_sum(grid, i, j):
    sum = 0  # Initialize a variable to store the sum of neighbour values
    # Loop over the neighbourhood of the cell at position (i, j)
    # First loop over the rows (only rows within the grid are considered)
    for x in range(max(0, i - 1), min(rows, i + 2)):  # min (not below first row) and max (not above last row)
        # Secondly loop over the columns (only columns within the grid are considered)
        for y in range(max(0, j - 1),
                       min(columns, j + 2)):  # min (not below first column) and max (not above last column)
            if (x, y) != (i, j):  # Exclude the state of the cell itself from the sum
                sum += grid[x, y]  # Add the value of the state of the neighbour cell to the sum
    return sum  # Return the sum


# Function to update the grid to the next generation
def update_generation(grid):
    new_grid = np.copy(grid) # Create an independent copy of the current grid to store the next generation (new_grid)
    # Loop through each row and column to update the cells
    for i in range(rows): # Loop through each row
        for j in range(columns): # Loop through each column
            neighbour_sum = compute_neighbour_sum(grid, i, j) # Calculate the sum of neighbour's states to see how many neighbours are alive
            # Apply Conways game of life rules to determine the next generation
                # Any cell alive with less than two alive neighbours dies, due to underpopulation.
                # Any cell alive with two or three alive neighbours survives on to the next generation.
                # Any cell alive with more than three alive neighbours dies due to overpopulation.
            if grid[i, j] == 1 and (neighbour_sum < 2 or neighbour_sum > 3):
                new_grid[i, j] = 0  # Cell dies (underpopulation or overpopulation)
                # Any dead cell with exactly three alive neighbours becomes alive in the next generation due to reproduction, all other dead cells remain dead.
            elif grid[i, j] == 0 and neighbour_sum == 3:
                new_grid[i, j] = 1  # Cell becomes alive (reproduction)
    # Update the grid with the next generation (new_gird)
    grid[:] = new_grid[:] # update entire content of array grid with the entire content of array new_grid


# Function to display the current generation (Reference 2/3)
def display_grid(surface, grid): # surface = the pygame surface onto which the grid will be drawn
                                # grid = 2D numpy array of current generation of cells
    # loop over the entire grid
    for i in range(rows): # loop over rows of the grid
        for j in range(columns): # loop over columns of the grid
            if grid[i, j] == 1: # check the status of the cell is 1 (alive) and set colour to colour_alive
                colour = colour_alive
            else:
                colour = colour_dead # if cell's status is 0 (dead) set to colour_dead

            # Determine necessary information to represent cells as rectangles
            # 1) determine the coordinates of the rectangle
            x = j * cell_size  # x-coordinate based on the column index
            y = i * cell_size  # y-coordinate based on the row index

            # 2) determine the size of the rectangle
            width = cell_size - 1  # Width of the rectangle
            height = cell_size - 1  # Height of the rectangle

            # Draw cell as rectangle onto the pygame surface
            pygame.draw.rect(surface, colour, (x, y, width, height))
                # surface = the pygame surface onto which the rectangle will be drawn
                # colour = colour of the rectangle (cell) based on the cell's state (dead or alive)
                # rectangle as tuple with x-coordinate, y-coordinate, width, and height of the rectangle


# Set up and run the game
pygame.init()  # Initialize the pygame library (Reference 2/3)
surface = pygame.display.set_mode((window_width, window_height))  # Create the game window with the specified dimensions (Reference 2/3)
pygame.display.set_caption("Conway's Game of Life")  # Set the window title (Reference 2/3)

initialize_grid(grid)  # Initialize the grid with random values

# Main game loop runs indefinitely until user closes window (Reference 2/3)
while True:
    for event in pygame.event.get():  # Handle event
        if event.type == pygame.QUIT: # If the user closes the window
            pygame.quit()  # Quit pygame


    surface.fill(colour_grid)  # Fill the surface with the grid colour (colour of grid lines)
    update_generation(grid)  # Compute the next generation
    display_grid(surface, grid)  # Display the current generation
    pygame.display.update()  # Update the display