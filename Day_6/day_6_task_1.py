from collections import Counter
fname = "input.txt"
locs = []
mess_len = 4
with open(fname) as f:
    for line in f:
        # get first repeating
        for i in range(mess_len,len(line),1):
            packet = line[i-mess_len:i] # get packet of data
            counter = Counter(packet)
            counts = [count for _, count in counter.items()]
            if len(counts) == mess_len:
                locs.append(i)
                break
               
print(locs)
    

