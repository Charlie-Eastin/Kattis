import sys
from collections import deque
import math
import re

file = open("input.txt", "r")

sets = []


for line in file:
    sides = line.strip().split(';')
    for side in sides:
        pattern = r"\((\d+),(\d+)\),\((\d+),(\d+)\)"
        match = re.match(pattern, side)
        if match:      
            x1, y1, x2, y2 = map(int, match.groups())
            coordinate_1 = (x1, y1)
            coordinate_2 = (x2, y2)
            found = False
            for set_poly in sets:
                if coordinate_1 in set_poly:
                    set_poly.add(coordinate_2)
                    found = True
                elif coordinate_2 in set_poly:
                    set_poly.add(coordinate_1)
                    found = True
            if not found:
                new_set = set()
                new_set.add(coordinate_1)
                new_set.add(coordinate_2)
                sets.append(new_set)
                break
                

print(sets)                



