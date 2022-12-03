score_dict = {'A': 1, # Rock
                'B': 2, # Paper
                'C': 3} # Scissors
encoding_dict = {'X':'A',
                'Y': 'B',
                'Z':'C'
}

total_score = []

fname = "input.txt"
with open(fname) as f:
    for line in f:
        # temp = line.strip()
        action = line.strip().split(" ")
        elf = action[0]
        result = action[1]

        if result == 'Y': # if draw
            total_score.append(score_dict[elf]+ 3)

        elif result == 'X': # need to lose
            if elf == 'A': # if rock than we choose scissors
                total_score.append(3+0)
            elif elf == 'B': # if paper we choose rock
                total_score.append(1+0)
            elif elf == 'C': # if paper choose scissors
                total_score.append(2+0)

        elif result == 'Z': # need to win
            if elf == 'A': # if rock than we paper
                total_score.append(2+6)
            elif elf == 'B': # if paper we choose scissors
                total_score.append(3+6)
            elif elf == 'C': # if paper choose rock
                total_score.append(1+6)


print(sum(total_score))


     

        