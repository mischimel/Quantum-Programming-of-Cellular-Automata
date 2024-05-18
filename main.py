# Define variables
generation = 0  # Start at generation 0
ruleset = [0, 0, 0, 1, 1, 1, 1, 0]  # Rule 30

# Initialize cells array
cells = [0] * (99)  # Array with 99 cells all set to 0 (dead)
cells[len(cells) // 2] = 1  # Set the center cell to 1 (alive)


def rules(a, b, c):
    s = str(a) + str(b) + str(c)
    index = int(s, 2)
    return ruleset[7 - index]


def print_cells(cells, generation):
    print(f"Generation {generation}: ", end="")
    for cell in cells:
        if cell == 1:
            print("■", end="")
        else:
            print("□", end="")
    print()

# Compute generations
for generation in range(0, 48):  # Limiting to 48 generations for console output
    nextgen = cells[:]
    for i in range(1, len(cells) - 1):
        left = cells[i - 1]
        me = cells[i]
        right = cells[i + 1]
        nextgen[i] = rules(left, me, right)

    cells = nextgen
    print_cells(cells, generation)
