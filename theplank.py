import sys

file = open("input.txt", 'r')

length = int(file.readline().strip())
# length = 4
count = 0

def dfs(currentLength):
    global count
    if currentLength == length:
        count += 1
        return
    elif currentLength > length:
        return
    for i in range(1, 4):
        dfs(i + currentLength)

dfs(0)

print(count)