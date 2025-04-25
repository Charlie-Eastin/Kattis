import sys
import math

file = open("input.txt", "r")

kari_start_x, kari_start_y, ola_start_x, ola_start_y, kari_end_x, kari_end_y, ola_end_x, ola_end_y  = list(map(int, file.readline().strip().split()))

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

dist = []

dist.append(distance(kari_start_x, kari_start_y, ola_start_x, ola_start_y))

dist.append(distance(kari_end_x, kari_end_y, ola_end_x, ola_end_y))

largest_distance = max(dist)

if (int(largest_distance) == largest_distance):
    print(int(largest_distance))
else:
    print(round(largest_distance, 10))

