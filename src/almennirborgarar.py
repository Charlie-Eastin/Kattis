import sys
from math import lcm
import math
from functools import reduce

file = open("input.txt", "r")

grills_length, people = file.readline().strip().split()
#grills_length, people = sys.stdin.readline().strip().split()

people = int(people) + 1

grills = list(map(int, file.readline().strip().split()))
#grills = list(map(int, sys.stdin.readline().strip().split()))

least_common_multiple = reduce(lcm, grills)
greatest_common_factor = reduce(math.gcd, grills)

seconds = 0

grill_increment = 0

grill_increment = sum(least_common_multiple // grill for grill in grills)

cycles = people // grill_increment
seconds = cycles * least_common_multiple
people = people - cycles * grill_increment

if (people > 0):
    grill_available = {}
    for grill in grills:
        for i in range(grill, (grill * people) + 1, grill):
            if i not in grill_available:
                grill_available[i] = 1
            else:
                grill_available[i] = grill_available[i] + 1
    
    grill_available = dict(sorted(grill_available.items()))

    seconds_elapsed = 0

    for i in grill_available:
        if people > 0:
            people = people - grill_available[i]
        else:
            break
        if (seconds_elapsed == 0):
            seconds_elapsed += i
        else:
            seconds_elapsed += i - seconds_elapsed
    seconds += seconds_elapsed



print(seconds)


    

    