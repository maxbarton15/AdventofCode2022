

fname = "input.txt"
import numpy as np
import sys
np.set_printoptions(edgeitems=30, linewidth=100000, 
    formatter=dict(float=lambda x: "%.3g" % x))

lines = [line.strip() for line in open(fname).readlines()]
cycles_of_interest = [num for num in range(40,280, 40)]

# create empty grid
grid = np.zeros((6,40))
x = 1
cycle = 1
j = 0 # controlling column of drawing
# at every cycle put a # 
for line in lines:
    
    if line == 'noop': 
        # do nothing to x, draw and add cycle
        sprite = [x-1, x, x+1]
        if cycle-1 in sprite:
            grid[j, cycle-1] = 1
        cycle +=1
        if cycle >= 40:
            j+=1
            cycle= 0
    else: #
        add = int(line.split()[1])

        for _ in range(2):
            sprite = [x-1, x, x+1]

            # draw
            
            if cycle-1 in sprite:
                grid[j, cycle-1] = 1
            cycle +=1
            if cycle >= 40:
                j+=1
                cycle= 0

        x+=add


        
result = np.full(shape = (6,40), fill_value = '.', dtype = str)

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if grid[i,j] == 1:
            result[i,j] = '#'
        else:
            pass

print(result)
        


