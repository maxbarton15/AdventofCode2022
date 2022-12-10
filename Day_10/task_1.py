

fname = "input.txt"

lines = [line.strip() for line in open(fname).readlines()]


cycles_of_interest = [20, 60, 100, 140, 180, 220]
result = []
x = 1
cycle = 1
for line in lines:
    
    if line == 'noop': 
        # do nothing to x during cycle
        if cycle in cycles_of_interest:
            result.append(x)
        cycle+=1

    else:
        add = int(line.split()[1])
        #print(int(line[4])) # if add x
        for i in range(2):
            # do nothing during first two cycles
            if cycle in cycles_of_interest:
                result.append(x)
            cycle += 1


        x+= add


sum = 0
for i, j in zip(result, cycles_of_interest):
    sum += (i*j)

print(sum)


        
        

        



#print(lines)