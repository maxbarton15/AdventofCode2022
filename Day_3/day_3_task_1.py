fname = "input.txt"

with open(fname) as f:
    for line in f:
        text = line.strip()
        print(text)