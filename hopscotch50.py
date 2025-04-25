import sys
import heapq

file = open("input.txt", 'r')

size, steps = list(map(int, file.readline().strip().split()))

grid = []

for i in range(size):
    grid.append(list(map(int,file.readline().strip().split())))

def djikstra(grid, steps, size):

    dict = {}

    for i in range(size):
        for j in range(size):
            value = grid[i][j]
            if (value not in dict):
                dict[value] = []
            dict[value].append((i,j))

    for num in range(1, steps + 1):
        if (num not in dict):
            return -1

    min_heap = []
    best = {}
    for i in range(len(dict[1])):
        heapq.heappush(min_heap, (0, 1, dict[1][i][0], dict[1][i][1]))
        best[(dict[1][i][0], dict[1][i][1], 1)] = 0

    while(len(min_heap) > 0):
        minimum_distance, minimum_index, x1, y1 = heapq.heappop(min_heap)

        if (minimum_index == steps):
            return minimum_distance

        
        for i in range(len(dict[minimum_index + 1])): 
            x2 = dict[minimum_index + 1][i][0]
            y2 = dict[minimum_index + 1][i][1]
            cost = abs(x2 - x1) + abs(y2 - y1) + minimum_distance
            if (x2, y2, minimum_index + 1) not in best or cost < best[(x2, y2, minimum_index + 1)]:
                best[(x2, y2, minimum_index + 1)] = cost
                heapq.heappush(min_heap, (cost, minimum_index + 1, dict[minimum_index + 1][i][0], dict[minimum_index + 1][i][1]))


print(djikstra(grid, steps, size))
