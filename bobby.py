import sys

file = open("input.txt", 'r')

cases_count = int(file.readline().strip())
cases = []

for _ in range(cases_count):
    roll, sides, x, y, multiplier = list(map(int, file.readline().strip().split()))
    success = (sides - roll + 1) / sides
    failure = 1 - success
    results = []
    dp = []

    for _ in range(y + 1):
        row = [0] * (y + 1)
        dp.append(row)

    dp[0][0] = 1
        
    for i in range(1, y + 1):
        for j in range(i + 1):
            dp[i][j] = dp[i - 1][j] * failure
            if j > 0:
                dp[i][j] += dp[i-1][j-1] * success
    
    probability = 0
    for i in range(x, y + 1):
        probability += dp[y][i]

    if (probability * multiplier > 1):
        print("yes")
    else:
        print("no")





