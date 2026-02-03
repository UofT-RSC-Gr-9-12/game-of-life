import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Grid size
WIDTH, HEIGHT = 60, 40

# Create random initial state
grid = np.random.randint(0, 2, size=(HEIGHT, WIDTH))


def count_live_neighbors(x, y):
    # Walk students through this function
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i == 0 and j == 0):
                continue
            nx = x + i
            ny = y + j
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH:
                total += grid[nx, ny]
    return total


def update(frame):
    global grid
    new_grid = grid.copy()

    for i in range(HEIGHT):
        for j in range(WIDTH):
            # Count live neighbors
            neighbors = count_live_neighbors(i, j)

            # Apply Conway's rules
            # Students can customize and make their own rules here
            if grid[i, j] > 0:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if neighbors == 3:
                    new_grid[i, j] = 1  # born

    grid = new_grid
    mat1.set_data(grid)
    return [mat1]


# Plot setup
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
mat1 = ax.imshow(grid)
ax.set_xticks([])
ax.set_yticks([])

ani = FuncAnimation(fig, update, interval=100)

plt.show()
