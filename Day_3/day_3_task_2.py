import string
fname = "input.txt"

code_dict = {}
count = 1
for s in string.ascii_lowercase:
    code_dict[s] = count
    count +=1
for s in string.ascii_uppercase:
    code_dict[s] = count
    count +=1

scores = []
count = 1
strings = []
with open(fname) as f:
    for line in f:
        if count % 3 == 0: # every 3 lines
            strings.append(line.strip())
            common_letter = set(strings[0]).intersection(set(strings[1]))
            common_letter = common_letter.intersection(set(strings[2]))
            scores.append(code_dict[list(common_letter)[0]])
            strings = []

        else:
            strings.append(line.strip())

        count+=1

print(sum(scores))
        # code = set(r1).intersection(set(r2)) # item type
        # code = list(code)[0]
        # scores.append(code_dict[code])

# print(sum(scores))
