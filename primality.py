import sys
import random

file = open("input.txt", "r")

num = int(file.readline().strip())

# exponentionation by squaring
# Uses binary representation of the exponent for squaring?
def fermat_func_1(x, y, modulus):
    if(y == 0):
        return 1
    elif(y == 1):
        return x % modulus
    elif y % 2 == 1:
        return x * fermat_func_1(x * x % modulus, y // 2, modulus) % modulus
    else:
        return fermat_func_1(x * x % modulus, y // 2, modulus)
def fermat_func_2(num, k):
    if (num == 2 or num == 3):
        print("YES")
        return
    for _ in range(k):
        if fermat_func_1(random.randint(2, num - 1), num - 1, num) != 1:
            print("NO")
            return
    print("YES")

fermat_func_2(num, 10000)

