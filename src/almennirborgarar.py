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

#print(grills)

least_common_multiple = reduce(lcm, grills)
greatest_common_factor = reduce(math.gcd, grills)

seconds = 0

grill_increment = 0

for grill in grills:
    grill_increment = grill_increment + (least_common_multiple // grill)

remainder = False
if (int(people / grill_increment) != 0):
    people = int(people / grill_increment)
    seconds = people * least_common_multiple
    remainder = True

int_seconds = int(seconds)
current_time = greatest_common_factor
if seconds != int_seconds or remainder == False:
    while people > 0:
        for grill in grills:
            if current_time % grill == 0:
                people -= 1
        if (people <= 0):
            break
        current_time += greatest_common_factor

int_seconds += current_time

print(int_seconds)


    

    