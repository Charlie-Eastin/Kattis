import sys
from math import lcm
import math
from functools import reduce

file = open("input.txt", "r")

grills_length, people = file.readline().strip().split()
#grills_length, people = sys.stdin.readline().strip().split()

people = int(people) + 1

grills = list(map(int, file.readline().strip().split()))

high_value = pow(10, 15)
low_value = 1

while (low_value < high_value):
    middle_value = (low_value + high_value) // 2
    people_served = 0

    for grill in grills:
        people_served += (middle_value // grill)
    
    if (people_served < people):
        low_value = middle_value + 1
    else:
        high_value = middle_value

print(high_value)
    

    