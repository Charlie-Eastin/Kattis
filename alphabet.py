import sys
import copy

file = open("input.txt", "r")

letters = file.readline().strip()
letters_count = len(letters)

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_count = len(alphabet)

dp = []

for _ in range(letters_count + 1):
    row = [0] * (alphabet_count + 1)
    dp.append(row)

for i in range(1, letters_count + 1):
    for j in range(1, alphabet_count + 1):
        value = 0
        if (letters[i - 1] == alphabet[j - 1] ):
            value = dp[i - 1][j - 1] + 1
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], value)

path = []
i = letters_count
j = alphabet_count
while(i > 0 and j > 0):
    if (letters[i - 1] == alphabet[j - 1]):
        path.append(letters[i - 1])
        i = i - 1
        j = j - 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i = i - 1
    else:
        j  = j - 1

print(alphabet_count - dp[letters_count][alphabet_count])