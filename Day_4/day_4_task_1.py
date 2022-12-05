import numpy as np
fname = "input.txt"
result = 0 
with open(fname) as f:
    for line in f:
        # split by the comma
        line = line.strip()
        line = line.split(",")

        # then split by the dash
        ranges = []
        for r in line:
            ranges.append(r.split("-"))
        
    
        # get range lists and then conver to sets 
        r1 = np.arange(int(ranges[0][0]), int(ranges[0][1])+1)
        r2 = np.arange(int(ranges[1][0]), int(ranges[1][1])+1)
        r1 = set(r1)
        r2 = set(r2)

        if len(r1.intersection(r2)) > 0:
            result +=1



print(result)

        #r1 = np.arange(int(ranges[0][0], 10), int(ranges[0][1]+1, 10))
        # print(int(ranges[0][0]), int(ranges[0][1]))
        # r1 = np.arange(int(ranges[0][0], int(ranges[0][1])))
        # #r1 = np.arange(int(ranges[0][0]), int(ranges[0][1]+1))
        # #print(r1)