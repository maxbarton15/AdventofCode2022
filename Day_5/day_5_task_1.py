import re
import sys
fname = "input.txt"

# get lines from text
lines = [line.strip() for line in open(fname).readlines()]

# if empty string then seperates stacks from instructions
seperator = [i for i, n in enumerate(lines) if n == ''][0]
crates = lines[:seperator-1]# crates up to empty line -1

instructions = lines[seperator+1:] # instructions
stack_num = 9


crates = [line.strip("\n") for line in open(fname).readlines()][:seperator-1]
len_crates = len(crates[0])

# initialise crate arrays
crate_arrays = []
for i in range(stack_num):
    crate_arrays.append([])

# populate crate_arrays with crate names
# every 4 characters in crates -> crate array column
for crate in crates[::-1]: # loop through crates
    # get list of crate letters
    items = [crate[i] for i in range(1, len_crates, 4)]
    # loop through enumerated list and add to crate arrays at position
    for i, n in enumerate(items):
        if n != " ":
            crate_arrays[i].append(n)

for line in instructions:
    numbers = re.findall(r'\d+', line)


    for i in range(int(numbers[0])):
        to_move = crate_arrays[int(numbers[1])-1].pop()
        crate_arrays[int(numbers[2])-1].append(to_move)

print([c[-1] for c in crate_arrays])




#     
#     items = [crate[i] for i in range(i, len(crate), 4)]
#     for i, n in enumerate(items):
#         if n != " ":
#             stacks.append(i+1).append(n)
