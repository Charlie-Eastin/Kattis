import sys

file = open("input.txt", 'r')

n, t = map(int, file.readline().strip().split())
distances = []
spedometer = []

for i in range(n):
    d, s = map(int, file.readline().strip().split())
    distances.append(d)
    spedometer.append(s)


low = -10000000.0
high = 10000000.0
precision = 1e-9


while high - low > precision:
    mid = (low + high) / 2
    total = 0.0
    invalid = False
    for i in range(len(distances)):
        if (spedometer[i] + mid > 0): #Figure out how to handle this
            total += distances[i] / (spedometer[i] + mid)
        else:
            invalid = True
            break
    if (total > t or invalid == True):
        low = mid
    else:
        high = mid
print(f"{low:.9f}")
    



