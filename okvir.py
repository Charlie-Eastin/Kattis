import sys
import math

file = open("input.txt", 'r')

height, width = list(map(int, file.readline().strip().split()))

up, left, right, down = list(map(int, file.readline().strip().split()))

counter = 0

def print_value(x, y):
    if x == 1 and y == 0:
        return '.'
    elif x == 1 and y == 1:
        return '#'
    elif x == 0 and y == 0:
        return '#'
    elif x == 0 and y == 1:
        return '.'

for i in range(up):
    line = ""
    for j in range(left + width + right):
        value = print_value(counter, j % 2)
        print(value, end="")
    print()
    counter = counter ^ 1
for _ in range(height):
    line = ""
    for j in range(left):
        value = print_value(counter, j % 2)
        print(value, end="")
    value2 = file.readline().split()[0]
    print(value2, end="")
    for j in range(right):
        value = print_value(counter, (j + len(value2) % 2))
        print(value, end="")
    counter = counter ^ 1
    print()
counter = counter ^ 1
for _ in range(down):
    line = ""
    for j in range(left + width + right):
        value = print_value(counter, j % 2)
        print(value, end="")
    print()
    counter = counter ^ 1


    