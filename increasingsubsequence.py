import sys
import copy

file = open("input.txt", "r")

while (True):
    input = list(map(int,file.readline().strip().split()))

    count_sequence = input[0]

    if (count_sequence == 0):
        break

    sequence = []

    for i in range(1, count_sequence + 1):
        sequence.append(input[i])

    sorted_sequence = copy.deepcopy(sequence)
    sorted_sequence = list(set(sorted_sequence))
    sorted_sequence.sort()
    count_sorted_sequence = len(sorted_sequence)

    dp = []

    for _ in range(count_sequence + 1):
        row = [0] * (count_sorted_sequence + 1)
        dp.append(row)

    for i in range(1, count_sequence + 1):
        for j in range(1, count_sorted_sequence + 1):
            value = 0
            if (sequence[i - 1] == sorted_sequence[j - 1] ):
                value = dp[i - 1][j - 1] + 1
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], value)

    path = []
    i = count_sequence
    j = count_sorted_sequence
    while(i > 0 and j > 0):
        if (sequence[i - 1] == sorted_sequence[j - 1]):
            path.append(sequence[i - 1])
            i = i - 1
            j = j - 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i = i - 1
        else:
            j  = j - 1

    list_printable = " ".join(list(map(str, reversed(path))))
    print(dp[count_sequence][count_sorted_sequence], list_printable)