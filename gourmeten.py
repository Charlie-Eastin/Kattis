import sys

file = open("input.txt", 'r')

time = int(file.readline().strip())
items_count = int(file.readline().strip())
items = []

for i in range(items_count):
    items.append(int(file.readline().strip()))

dp = [0] * (time + 1)
dp[0] = 1

for i in range(1, time + 1):
    for item in items:
        if i >= item:
            dp[i] += dp[i - item]

print(dp[time])