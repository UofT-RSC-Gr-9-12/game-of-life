import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Grid size
WIDTH, HEIGHT = 60, 40

# Create random initial state
grid = np.random.randint(0, 2, size=(HEIGHT, WIDTH))

def update(frame):
    global grid
    new_grid = grid.copy()

    for i in range(HEIGHT):
        for j in range(WIDTH):
            # Neighbor placeholder
            neighbors = 2

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
