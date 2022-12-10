
fname = "input.txt"

knots = 9
file = open(fname).read().strip()
lines = [x for x in file.split("\n")]

#print(lines)
def change_tail(H, T):
      # differences vertically and laterally
      diff_lateral = (H[0] - T[0])
      diff_vertical = (H[1] - T[1])
      # if both lateral and vertical distances are less than one we are gucci -> don't the move tail!
      if abs(diff_lateral) <=1 and abs(diff_vertical) <=1:
        pass 
      elif abs(diff_lateral) >= 2 and abs(diff_vertical) >=2: # vertical movement - up for both vertical and lateral
        T = (H[0]-1 if H[0] > T[0] else H[0]+1, H[1]-1 if H[1] > T[1] else H[1]+1)
      elif abs(diff_lateral) >= 2: # if columns are different move lateral 
        T = (H[0]-1 if H[0] > T[0] else H[0]+1, H[1])
      elif abs(diff_vertical) >=2: # if rows are different move vertical
        T = (H[0], H[1]-1 if H[1] > T[1] else H[1]+1)
      return T

H = (0,0)
T = [(0,0) for _ in range(knots)] # 9 knots now (not inc head)

d1_dict = {'L':0, 'U':1, 'R': 0, 'D': -1}
d2_dict = {'L':-1, 'U':0, 'R': 1, 'D': 0}
seen_positions = set()

# only add positions of last knot
for line in lines:
  seen_positions.add(T[knots-1]) # add in t positions if not in set
  direction, amount = line.split() # get direction and amount to move H
  amount = int(amount)
  for i in range(amount): 
    seen_positions.add(T[8])
    H = (H[0] + d1_dict[direction], H[1] + d2_dict[direction]) # apply new head position using dicts
    T[0] = change_tail(H, T[0]) # change position of first knot
    for i in range(1, knots-1): # then change the rest of the knots based off previous
      T[i] = change_tail(T[i-1], T[i])
    seen_positions.add(T[knots-1])
        
    #print(direction, i, H, T)
    seen_positions.add(T[knots-1])
    print(T[knots-1])


print(len(seen_positions))