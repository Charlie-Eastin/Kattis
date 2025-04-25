import sys

file = open("input.txt", 'r')

n, k = map(int, file.readline().strip().split())

weights = list(map(int, file.readline().strip().split()))

low = max(weights)
high = sum(weights)

while (low < high):
    mid = (high + low) // 2
    weight_sum = 0
    box_count = 1
    cutLow = True
    for weight in weights:
        if weight_sum + weight > mid:
            box_count += 1
            weight_sum = weight
            if (box_count > k):
                cutLow = False
        else:
            weight_sum += weight
    if (cutLow == True):
        high = mid
    else:
        low = mid + 1
print(low)

