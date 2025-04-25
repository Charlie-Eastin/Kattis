import sys
import math

file = open("input.txt", 'r')

size = int(file.readline().strip())

houses = []
spies = []

def manhattan_distance(coordinate1, coordinate2):
    return abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])

for i in range(size):
    line = file.readline().strip()
    for j in range(len(line)):
        if line[j] == 'H':
            houses.append((i, j))
        elif line[j] == 'S':
            spies.append((i, j))


distances = []
for spy in spies:
    min = sys.maxsize
    for house in houses:
        dist = manhattan_distance(house, spy)
        if dist < min:
            min = dist
    distances.append(min)
    
print(max(distances))
