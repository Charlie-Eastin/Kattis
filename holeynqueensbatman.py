import sys

file = open("input.txt", "r")

def findsolutions(x, cols, diagUp, diagDown, holes, solutions, size):
    if (x == size):
        return solutions + 1
    for y in range(size):
        if y not in cols and (x - y) not in diagUp and (x + y) not in diagDown and (x,y) not in holes:
            cols.add(y)
            diagUp.add(x - y)
            diagDown.add(x + y)

            solutions = findsolutions(x + 1, cols, diagUp, diagDown, holes, solutions, size)

            cols.remove(y)
            diagUp.remove(x - y)
            diagDown.remove(x + y)
    return solutions


while(True):
    line = file.readline().strip().split()
    if line[0] == '0' and line[1] == '0' :
        break
  
    holes = set() 

    for i in range(int(line[1])):
        x, y = file.readline().strip().split()
        x = int(x)
        y = int(y)
        holes.add((x,y))

    cols = set()
    diagUp = set()
    diagDown = set()

    count = findsolutions(0, cols, diagUp, diagDown, holes, 0, int(line[0]))
    print(count)
