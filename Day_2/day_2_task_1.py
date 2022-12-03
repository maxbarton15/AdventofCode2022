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
        me = action[1]
        me = encoding_dict[me]

        # if both choose same action
        if (me == elf):
            total_score.append(score_dict[me]+3)

        # if you choose a rock
        elif me == 'A':
            if elf == 'B': # if paper then loses
                total_score.append(score_dict[me]+ 0)
            elif elf == 'C': # if scissors wins
                total_score.append(score_dict[me]+ 6)
        
        # if you choose paper
        elif me == 'B':
            if elf == 'A': # if they chose rock then win
                total_score.append(score_dict[me] + 6)
            elif elf == 'C': # if they chose scissors lose
                total_score.append(score_dict[me]+ 0)
        
        else: # if chose scissors
            if elf == 'A': # if rock lose
                total_score.append(score_dict[me] + 0)
            elif elf == 'B': # win
                total_score.append(score_dict[me] + 6)
                
print(sum(total_score))


     

        