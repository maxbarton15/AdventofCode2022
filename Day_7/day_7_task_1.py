import re
from collections import defaultdict
fname = "input.txt"
file_struct = []
commands = [l.split(" ") for l in list(open(fname).read().rstrip().split("\n"))]
max = 100000
# build the file structure -> unsure if there is an easier solution to this

tree_struct = defaultdict(int) # dict that defaults to integer if key not found
path = []
for c in commands:

    # Change directory 
    if c[1] == 'cd': 

        # go back a directory
        if c[2] == '..': 
            path.pop()

        # else append directory name to path
        else:
            path.append(c[2])

    # lists subdirectories - just continue onto next command
    elif c[1] == 'ls':
        continue


    else: # if dir or number

        # if a number get file size and add to dictionary of path, otherwise pass
        try:
            file_size = int(c[0]) # file size
            for i in range(len(path)+1): #loop through path 
                tree_struct['/'.join(path[:i])] += file_size # add file size to path 
        except:
            pass

          
file_sums = []
for _, value in tree_struct.items():
    if value < max:
        file_sums.append(value)

print(sum(file_sums))