import sys

file = open("input.txt", "r")

map = {}

while(True):
    line = file.readline().strip().split()
    if len(line) == 0:
        break
    value = line[0]

    key = line[1]
    map[key] = value

#print(map)

while(True):
    key = file.readline().strip()
    if len(key) == 0:
        break
    if key not in map:
        print("eh")
    else:
        print(map[key])


