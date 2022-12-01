fname= 'input.txt'
sums = []
elf_calories = []
with open(fname) as f:
    for line in f:
        if line in ['\n', '\r\n']:
            sums.append(sum(elf_calories))
            elf_calories = []
        else:
            elf_calories.append(int(line))

print(max(sums))
            

