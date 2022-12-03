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
with open(fname) as f:
    for line in f:
        text = line.strip()
        text_len = int(len(text)/2)
        r1 = text[:text_len]
        r2 = text[text_len:]

        code = set(r1).intersection(set(r2)) # item type
        code = list(code)[0]
        scores.append(code_dict[code])

print(sum(scores))
