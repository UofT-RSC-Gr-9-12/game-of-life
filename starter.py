# TODO: Import the module numpy

# TODO: Import the module matplotlib.pyplot

from matplotlib.animation import FuncAnimation

# TODO: Create a variable called WIDTH and assign it 60

# TODO: Create a variable called HEIGHT and assign it 40

# TODO: Create a variable called grid and assign it the return value of
# np.random.randint(0, 2, size=(HEIGHT, WIDTH))

# Grid is a 2D list. Each cell contains either a 0 (dead) or 1 (alive)

# This function counts the number of cells that are alive around cell (x, y)
# ?    ?     ?
# ?  (x, y)  ?
# ?    ?     ?
def count_live_neighbors(x, y):
    # TODO: Create a variable called total and assign it 0

    # TODO: Create a for-loop that goes through the numbers -1, 0, 1. Use i as the iterator variable.

    # TODO: Create another for-loop inside the previous that also goes through
    # the numbers -1, 0, 1. Use j as the iterator variable
    
    # We call the first for-loop the outer loop and the second the inner loop

    # TODO: Inside the inner loop, do the following:
    # 1. Check if i==0 and j==0, and if it is, write continue

    # 2. Create a variable called nx and assign it the value of x plus i

    # 3. Create a variable called ny and assign it the value of y plus j

    # 4. Check if nx AND ny's values are: greater than zero, and less than HEIGHT and WIDTH respectively
    # if they are, then add the value of the grid at cell (nx, ny) to the total.
    
    # TODO: Return total

# This function is run on a timer and will update the state of the grid
def update(frame):
    global grid
    new_grid = grid.copy()

    for i in range(HEIGHT):
        for j in range(WIDTH):
            # TODO: Create a variable called neighbors and assign it the return value of count_live_neighbors(i, j)

            # TODO: Apply Conway's rules (hint: you will need an if-else statement)

    grid = new_grid
    mat1.set_data(grid)
    return [mat1]


# Plot setup

# The plt.subplots function takes in these arguments:
# The first argument is the number of rows
# The second argument is the number of columns
# And then, we can specify figsize=(<width>, <height>) as another argument

fig, ax = # TODO: Call plt.subplots to set up a single figure of size 10 x 6
mat1 = ax.imshow(grid)
ax.set_xticks([])
ax.set_yticks([])

# The FuncAnimation function takes in various arguments:
# The first argument is the figure plot to draw on
# The second argument is the update function
# And then, we can specify interval=<milliseconds> as another argument

# TODO: Create a variable called ani and assign the return value of FuncAnimation 
# using fig, update, and an interval of 100 ms

# TODO: Call plt.show
