import sys

file = open("input.txt", "r")

#line = sys.stdin.readline().strip().split()
line = file.readline().strip().split()

teams = int(line[0])
problems = int(line[1])

rankings = [None] * teams

for i in range(teams):
   #rankings[i] =  int(sys.stdin.readline().strip())
   rankings[i] =  int(file.readline().strip())

score = []

still_zeros = True
rank_ups = 0
previous_value = 0
ambiguous = False

for value in reversed(rankings):
    if value == 0:
        if not still_zeros:
            ambiguous = True
            break
            
        score.append(0)
    else:
        still_zeros = False
        if (value > previous_value):
            rank_ups += 1
            score.append(rank_ups)
            previous_value = value
        elif( value <= previous_value):
            score.append(rank_ups)
            previous_value = value
    
if (rank_ups != problems and still_zeros == False):
   print("ambiguous")
elif (ambiguous == True):
   print("ambiguous")
else:
   for value in reversed(score):
    print(value)
       

