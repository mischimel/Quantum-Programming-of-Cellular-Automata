# Import Librarie
import numpy as np  # Import the numpy library for handling arrays
import pygame  # Import the pygame library for creating the graphical window

# Define Constants
cell_size = 8  # Define the size of each cell in pixels
window_width = 648  # Define the width of the game window
window_height = 480  # Define the height of the game window

# Calculate Grid Dimensions
columns = window_width // cell_size  # Calculate the number of columns in the grid
rows = window_height // cell_size  # Calculate the number of rows in the grid

# Initialise Grid
grid = np.zeros((rows, columns))  # Initialise the grid with zeros
grid[0, int(columns / 2)] = 1  # Set the centre cell of the first row to 1 (alive)

# Define Ruleset
ruleset = [0, 0, 0, 1, 1, 1, 1, 0]  # Define the ruleset for Rule 30

# Define Colors
colour_alive = (200, 200, 225)  # Define the colour for alive cells (light purple)
colour_dead = (10, 10, 40)  # Define the colour for dead cells (dark blue)
colour_grid = (30, 30, 60)  # Define the colour for the grid lines (lighter dark blue)

# Function to determine the next state of a cell based on its neighbourhood (left, middle, and right cell)
def determine_cell_state(left_cell, middle_cell, right_cell):
    neighbourhood = f"{int(left_cell)}{int(middle_cell)}{int(right_cell)}"  # Convert into int and create a binary string of the neighbourhood
    index = int(neighbourhood, 2)  # Convert the binary string to a decimal integer
    return ruleset[7 - index]  # Return the new state of the cell based on the ruleset

# Function to update the grid to the next generation based on the ruleset (Rule 30)
def update_generation(grid):
    for generation in range(1, rows):  # Iterate through each row, starting from the second row
        nextgen = np.zeros(columns)  # Initialise the next generation array with zeros and length of columns

        for i in range(1, columns - 1):  # Iterate through each cell, excluding the edge cells
            left = grid[generation - 1, i - 1]  # Get the state of the left neighbour
            middle = grid[generation - 1, i]  # Get the state of the current cell
            right = grid[generation - 1, i + 1]  # Get the state of the right neighbour
            nextgen[i] = determine_cell_state(left, middle, right)  # Determine the new state and assign it

        grid[generation] = nextgen  # Update the current generation with the new states

# Function to draw the grid on the pygame surface.
def display_grid(surface, grid):
    for i in range(rows):  # Iterate through each row
        for j in range(columns):  # Iterate through each column
            if grid[i, j] == 1:
                colour = colour_alive  # Set the colour to alive if the cell state is 1
            else:
                colour = colour_dead  # Set the colour to dead if the cell state is 0

            x = j * cell_size  # Calculate the x position of the cell
            y = i * cell_size  # Calculate the y position of the cell
            width = cell_size - 1  # Set the width of the cell (rectangle)
            height = cell_size - 1  # Set the height of the cell (rectangle)

            pygame.draw.rect(surface, colour, (x, y, width, height))  # Draw the cell on the surface

# Initialise Pygame
pygame.init()  # Initialise the pygame module
surface = pygame.display.set_mode((window_width, window_height))  # Create the game window
pygame.display.set_caption("1D Cellular Automaton - Rule 30")  # Set the window title

# Game Loop
running = True  # Set the running variable to True to start the game loop
while running:
    for event in pygame.event.get():  # Iterate through all events
        if event.type == pygame.QUIT:  # Check if the user clicked the close button
            running = False  # Set running to False to end the game loop
            pygame.quit()  # Shut down pygame

    surface.fill(colour_grid)  # Fill the surface with the grid colour
    update_generation(grid)  # Update the grid to the next generation
    display_grid(surface, grid)  # Display the grid on the surface
    pygame.display.update()  # Update the display to show the changes