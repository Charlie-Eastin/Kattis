import sys

file = open("input.txt", 'r')

while(True):
    expression = file.readline().strip().split()
    
    if (not expression):
        break

    num1 = int(expression[0]) 
    operator = expression[1]
    num2 = int(expression[2])
    output = 0
    if operator == "+":
        num1_last4 = num1 % 10000
        num2_last4 = num2 % 10000

        output = (num1_last4 + num2_last4) % 10000
    elif operator == "*":
        num1_last4 = num1 % 10000
        num2_last4 = num2 % 10000

        output = (num1_last4 * num2_last4) % 10000
    elif operator == "^":
        exponent_binary = bin(num2)[2:] # Binary Conversion
        output = 1
        num1 %= 10000
        while(num2 > 0):
            if (num2 % 2 == 1):
                output = (output * num1) % 10000
            num1 = (num1 * num1) % 10000
            num2 = num2 // 2

    print(int(output))
            



