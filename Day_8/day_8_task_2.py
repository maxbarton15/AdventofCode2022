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


best_scenic = 0
# loop through elements in tree 
for row in range(0,no_rows):
    for col in range(0, no_cols):
        viewing_distances = np.zeros(4, dtype = 'int32')
        tree = grid[row][col]

        tree_up = grid[:row, col][::-1]
        tree_down = grid[row+1:, col]
        tree_right = grid[row, col+1:]
        tree_left = grid[row, :col][::-1]

        # got to be a better way than this but just going to loop upwards, downwards, left, right and count viewing distances
        for i in tree_up:
            if tree > i:
                viewing_distances[0]+=1
            else:
                viewing_distances[0] += 1
                break
        for i in tree_down:
            if tree > i:
                viewing_distances[1] += 1
            else:
                viewing_distances[1] += 1
                break
        for i in tree_left:
            if tree > i:
                viewing_distances[2] += 1
            else:
                viewing_distances[2] += 1
                break
        for i in tree_right:
            if tree > i:
                viewing_distances[3] += 1
            else:
                viewing_distances[3] += 1
                break

        if np.prod(viewing_distances) > best_scenic:
            best_scenic = np.prod(viewing_distances)
            
print(best_scenic)


