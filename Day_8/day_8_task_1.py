fname = "input.txt"
import numpy as np

# read in data as numpy array
grid = []
with open(fname) as f:
    for line in f:
        row = [int(num) for num in line.strip()]

        grid.append(row)

grid = np.array(grid)
no_rows, no_cols = grid.shape

# all outside trees can be seen -> no_col*no_col
total_trees = no_cols*2 + (no_rows-2)*2
print(no_rows,no_cols)


# now go through each treeent and check can be seen from any side 
for row in range(1,no_rows-1):
    for col in range(1, no_cols-1):
        tree = grid[row][col]

        tree_up = grid[:row, col]
        tree_down = grid[row+1:, col]
        tree_right = grid[row, col+1:]
        tree_left = grid[row, :col]

        max_up = max(tree_up)
        max_down = max(tree_down)
        max_right = max(tree_right)
        max_left = max(tree_left)

        if tree > max_up:
            total_trees += 1
        elif tree > max_down:
            total_trees += 1
        elif tree > max_left:
            total_trees += 1
        elif tree > max_right:
            total_trees += 1
        else:
            pass

print(total_trees)
