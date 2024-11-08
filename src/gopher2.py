import sys

import math

file = open("src/input.txt", 'r')

gopher_count, gopher_hole_count, hawk_time, gopher_speed = list(map(int, file.readline().strip().split()))

gophers = []
holes = []

for i in range(gopher_count):
    values = file.readline().strip().split()
    x = float(values[0])
    y = float(values[1])
    gophers.append((x,y))

for i in range(gopher_hole_count):
    values = file.readline().strip().split()
    x = float(values[0])
    y = float(values[1])
    holes.append((x,y))

adjacency_list = {i: [] for i in range(gopher_count)}
for i in range(gopher_count):
    for j in range(gopher_hole_count):
        distance = math.sqrt((gophers[i][0] - holes[j][0]) ** 2 + (gophers[i][1] - holes[j][1]) ** 2)
        if (distance / gopher_speed <= hawk_time):
            adjacency_list[i].append(j)

hole_matches = [-1] * gopher_hole_count

def depth_first_search(gopher, visited):
    for hole in adjacency_list[gopher]:
        if not visited[hole]:
            visited[hole] = True

            if hole_matches[hole] == -1 or depth_first_search(hole_matches[hole], visited):
                #gopher_matches[gopher] = hole
                hole_matches[hole] = gopher
                return True
    return False

def max_matching():
    matches = 0
    for gopher in range(gopher_count):
        visited = [False] * gopher_hole_count
        if (depth_first_search(gopher, visited)):
            matches += 1
    return matches

matches = max_matching()
print(gopher_count - matches)