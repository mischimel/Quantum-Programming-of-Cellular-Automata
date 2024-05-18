import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the size of the grid
N = 100
# Define the probability of a cell being alive at the start
prob_alive = 0.2

# Function to initialize the grid randomly
def init_grid(N, prob_alive):
    grid = np.random.choice([0, 1], size=(N, N), p=[1-prob_alive, prob_alive])
    return grid

# Function to update the grid based on the rules of the game
def update_grid(grid):
    new_grid = np.zeros_like(grid)
    for i in range(N):
        for j in range(N):
            # Count the number of alive neighbors
            neighbors_sum = np.sum(grid[i-1:i+2, j-1:j+2]) - grid[i, j]
            # Apply the rules of the game
            if grid[i, j] == 1 and (neighbors_sum < 2 or neighbors_sum > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors_sum == 3:
                new_grid[i, j] = 1
            else:
                new_grid[i, j] = grid[i, j]
    return new_grid

# Function to animate the game
def animate_game(frames):
    global grid
    grid = update_grid(grid)
    img.set_array(grid)
    return img,

# Initialize the grid
grid = init_grid(N, prob_alive)

# Create a figure
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='binary')
plt.axis('off')

# Animate the game
ani = animation.FuncAnimation(fig, animate_game, frames=100, interval=100)
plt.show()
