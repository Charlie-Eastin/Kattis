import sys

file = open("input.txt", "r")

n, m, k = file.readline().strip().split()

team_a = list(map(int, file.readline().strip().split()))
team_b = list(map(int, file.readline().strip().split()))

# 1 if team_a[i] is > team_b[i], else 0
results = [1 if team_a[i] - team_b[i] > 0 elif  for i in range(len(team_a))]

wins = sum(1 for value in results if value > 0 )

print(wins)