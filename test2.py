import numpy
import numpy as np  # Import numpy for handling the grid as a 2D array
import pygame  # Import the pygame library for creating the game window and drawing

# Initialize variables
# 1) Set up the window
cell_size = 8  # Set cell size to 8 px, so a cell is a 8x8 px square
window_width = 640  # Window will be 640 px wide
window_height = 480  # Window will be 480 px tall

columns = window_width // cell_size  # 80 cells of size 8 px fit into the 640 px wide window
rows = window_height // cell_size  # 60 cells of size 8 px fit into the 480 px tall window

colour_alive = (200, 200, 225) # Alive cells will be light purple
colour_dead = (10, 10, 40) # Background (dead cells) will be dark blue
colour_grid = (30, 30, 60) # Grid lines will be lighter dark blue

ruleset = [0, 0, 0, 1, 1, 1, 1, 0]  # Rule 30

grid = np.zeros((1, columns))  # Current generation of cells
grid[0, int(columns/2)] = 1


# Function to initialize the CA only middle cell = 1
#def initialize_grid(grid):
#    grid[0, int(columns/2)] = 1


def determine_cell_state(left_cell, middle_cell, right_cell):
    neighbourhood = (str(left_cell) + str(middle_cell) +
                     str(right_cell))  # Convert the states of neighboring cells into a string
    index = int(neighbourhood, 2)  # Convert the binary string into a decimal integer
    return ruleset[7 - index]  # Reverse the index since ruleset is defined in descending order

#-------------------------------------here ist ein fehler---------------------------------------------------------------
# es soll von der jetzigen Zeile eine Copy machen, das ändern, das geänderte anhöngen, davon eine copy machen, das ändern und wieder anhängen, bis man 60 rows hat
# Function to update the grid to the next generation
def update_generation(grid):
    # Compute the states of cells (excluding edge cells) for multiple generations
    # Loop through 31 generations (0 to 20)
    for generation in range(1, rows):
        nextgen = grid[generation]  # Create a copy of the current state of cells for the next generation
        # Loop through each cell, excluding the edge cells
        for i in range(1, len(grid) - 1):
            left = grid[i - 1]  # Get the state of the left neighbour cell
            middle = grid[i]  # Get the state of the middle cell
            right = grid[i + 1]  # Get the state of the right neighbour cell
            nextgen[i] = determine_cell_state(left, middle, right)  # Determine the state of the middle cell

        grid = numpy.append(nextgen)  # Update the state of cells to the next generation
#-------------------------------------here ist ein fehler---------------------------------------------------------------

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

#initialize_grid(grid)

# Main game loop runs indefinitely until user closes window (Reference 2/3)
while True:
    for event in pygame.event.get():  # Handle event
        if event.type == pygame.QUIT: # If the user closes the window
            pygame.quit()  # Quit pygame

    surface.fill(colour_grid)  # Fill the surface with the grid colour (colour of grid lines)
    update_generation(grid)  # Compute the next generation
    display_grid(surface, grid)  # Display the current generation
    pygame.display.update()  # Update the display