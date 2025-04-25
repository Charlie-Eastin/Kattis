import sys

file = open("input.txt", 'r')

test_cases_count = int(file.readline().strip())

test_cases = []

for i in range(test_cases_count):
    a = 9
    e = int(file.readline().strip()) - 1
    m = 1000000007

    if (e == 0):
        print(8)
    else: # 8 * 9^(e - 1)
        a %= m
        output = 1
        while(e > 0):
            if (e % 2 == 1):
                output = (output * a) % m
            a = (a * a) % m
            e = e // 2
        
        print((8 * output) % m)


