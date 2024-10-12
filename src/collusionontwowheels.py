import sys
from collections import deque

file = open("src/input.txt", 'r')

customer_count = int(file.readline().strip())

edges = []

customers = []

for i in range(customer_count):
    values = file.readline().strip().split()
    x = int(values[0])
    y = int(values[1])
    customers.append((x,y))

for i in range(customer_count):
    for j in range(i + 1, customer_count):
        distance = abs(customers[i][0] - customers[j][0]) + abs(customers[i][1] - customers[j][1])
        edges.append((i, j, distance))

adjacency_list = {i: [] for i in range(customer_count)}

max_distance = 0

for i, j, distance in edges:
    adjacency_list[i].append((j, distance)) 
    adjacency_list[j].append((i, distance))
    if (distance > max_distance):
        max_distance = distance

#print(adjacency_list)

low = 0
high = max_distance

def recursive_search(adjacency_list, colors, max_distance):
    for node in range(customer_count):
        if (colors[node] == -1):
            queue = deque([node])
            colors[node] = 0
        while queue:
            current = queue.popleft()
            current_color = colors[current]

            new_color = 1 - current_color

            for path, distance in adjacency_list[current]:
                if distance > max_distance:
                    if colors[path] == -1:
                        colors[path] = new_color
                        queue.append(path)
                    elif colors[path] == current_color:
                        return False          
    return True

low = 0
high = max_distance

while low < high:
    mid = (low + high) // 2
    colors = {i: -1 for i in range(customer_count)}  # -1 means uncolored

    if (recursive_search(adjacency_list, colors, mid)):
        high = mid
    else:
        low = mid + 1


print(low)
