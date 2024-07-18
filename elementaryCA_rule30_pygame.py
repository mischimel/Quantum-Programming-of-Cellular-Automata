import numpy as np  # Import numpy for handling the grid as a 2 array
import pygame  # Import the pygame library for creating the game window and drawing

# Initialise variables
# Set up the window
cell_size = 8  # Set cell size to 8 px, making each cell an 8x8 px square
window_width = 648  # Window width set to 648 px
window_height = 480  # Window height set to 480 px

# Calculate number of cells that fit horizontally and vertically in the window
columns = window_width // cell_size  # 81 cells of size 8 px fit into the 640 px wide window
rows = window_height // cell_size  # 60 cells of size 8 px fit into the 480 px tall window

# Initialise the grid for the cellular automaton
grid = np.zeros((rows, columns))  # Current generation of cells
grid[0, int(columns / 2)] = 1  # Set the center cell of the first row to 1 (alive)

# Define the ruleset for the cellular automaton
ruleset = [0, 0, 0, 1, 1, 1, 1, 0]  # Rule 30
#ruleset = [0, 1, 0, 1, 1, 0, 1, 0]  # Rule 90

# Define colours for cell states and grid lines
colour_alive = (200, 200, 225)  # Light purple for alive cells
colour_dead = (10, 10, 40)  # Dark blue for dead cells
colour_grid = (30, 30, 60)  # Lighter dark blue for grid lines


# Function to initialise the CA only middle cell = 1
#def initialise_grid(grid):
#    grid[0, int(columns/2)] = 1

def determine_cell_state(left_cell, middle_cell, right_cell):
    # Convert cell states to integers and then to a binary string
    neighbourhood = f"{int(left_cell)}{int(middle_cell)}{int(right_cell)}"
    index = int(neighbourhood, 2)  # Convert the binary string into a decimal integer
    return ruleset[7 - index]  # Reverse the index since ruleset is defined in descending order


def update_generation(grid):
    # Loop through each row to generate the next state
    for generation in range(1, rows):
        nextgen = np.zeros(columns)  # Create a placeholder for the next generation
        # Loop through each cell, excluding the edge cells
        for i in range(1, columns - 1):
            left = grid[generation - 1, i - 1]  # Get the state of the left neighbour cell
            middle = grid[generation - 1, i]  # Get the state of the middle cell
            right = grid[generation - 1, i + 1]  # Get the state of the right neighbour cell
            nextgen[i] = determine_cell_state(left, middle, right)  # Determine the state of the middle cell

        grid[generation] = nextgen  # Update the grid with the next generation


def display_grid(surface, grid):
    for i in range(rows):  # Loop over rows of the grid
        for j in range(columns):  # Loop over columns of the grid
            if grid[i, j] == 1: # Set colour based on cell's state
                colour = colour_alive
            else:
                colour = colour_dead

            # Determine necessary information to represent cells as rectangles
            x = j * cell_size  # x-coordinate based on the column index
            y = i * cell_size  # y-coordinate based on the row index
            width = cell_size - 1  # Width of the rectangle
            height = cell_size - 1  # Height of the rectangle

            pygame.draw.rect(surface, colour, (x, y, width, height))  # Draw cell as rectangle onto the pygame surface


# Set up and run the game
pygame.init()  # Initialise the pygame library
surface = pygame.display.set_mode((window_width, window_height))  # Create the game window with the specified dimensions
pygame.display.set_caption("1D Cellular Automaton - Rule 30")  # Set the window title

#initialise_grid(grid)

# Main game loop runs indefinitely until user closes window
running = True
while running:
    for event in pygame.event.get():  # Handle events
        if event.type == pygame.QUIT:  # If the user closes the window
            running = False
            pygame.quit()

    surface.fill(colour_grid)  # Fill the surface with the grid colour
    update_generation(grid)  # Compute the next generation
    display_grid(surface, grid)  # Display the current generation
    pygame.display.update()  # Update the display