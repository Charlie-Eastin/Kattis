import sys
import math

file = open("input.txt", 'r')

def distance(x1, y1, x2, y2, p):
    return math.pow((math.pow(abs(x1 - x2), p) + math.pow(abs(y1-y2), p)), 1/p)

while(True):
    line = list(map(float, file.readline().strip().split()))

    if (line[0] == 0):
        break

    x1, y1, x2, y2, p = line
    value = distance(x1, y1, x2, y2, p)
    print(f"{value:.10f}")

