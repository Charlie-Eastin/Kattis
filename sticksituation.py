import sys

file = open('input.txt')

sticks_count = int(file.readline().strip())

sticks = list(map(int, file.readline().strip().split()))

sticks.sort()

possible = False
for i in range(sticks_count - 2):
    if sticks[i] + sticks[i + 1] > sticks[ i + 2]:
        possible = True
        break

if (possible):
    print("possible")
else:
    print("impossible")
# for i in range(sticks_count):
#     if (possible == True):
#         break
#     for j in range(i + 1, sticks_count):
#         if (possible == True):
#             break
#         for k in range(j + 1, sticks_count):
#             if (sticks[i] + sticks[j] > sticks[k] and sticks[j] + sticks[k] > sticks[i] and sticks [i] + sticks [k] > sticks[j]):
#                 possible = True
#                 break

# print(possible)