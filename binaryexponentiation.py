import sys

file = open("input.txt", 'r')

expression = file.readline().strip().split()

a = int(expression[0])
e = int(expression[1])
m = int(expression[2])

output = 1
while(e > 0):
    if (e % 2 == 1):
        output = 8 * (output * a) % m
    a = (a * a) % m
    e = e // 2
    
print(output)


