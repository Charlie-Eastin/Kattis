
file = open("input.txt", 'r')

count = int(file.readline().strip())

m = 1000000000

def multiply(a, b):
   value00 = (a[0][0] * b[0][0] + a[0][1] * b[1][0]) % m
   value01 = (a[0][0] * b[0][1] + a[0][1] * b[1][1]) % m
   value10 = (a[1][0] * b[0][0] + a[1][1] * b[1][0]) % m
   value11 = (a[1][0] * b[0][1] + a[1][1] * b[1][1]) % m
   value = [[value00, value01], [value10, value11]]
   return value

for i in range(count):
    case_number, n = list(map(int, (file.readline().strip().split())))
    if (n == 1 or n == 2):
        print(case_number, end="")
        print(" ", end="")
        print(1)
    else:
        a = [[1, 1], [1, 0]]
        output = [[1, 0], [0, 1]]
        power = n - 2
        while (power > 0):
            if (power % 2 == 1):
                output = multiply(output, a)
            a = multiply(a, a)
            power = power // 2
        output_final = (output[0][0] + output[0][1]) % m
        print(case_number, end="")
        print(" ", end="")
        print(output_final)
        
    