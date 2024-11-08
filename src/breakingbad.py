import sys
from collections import deque

file = open("src/input.txt", 'r')

nodes_count = int(file.readline().strip())

graph = {}

for i in range(nodes_count):
    current = file.readline().strip()
    graph[current] = {"color": -1, "nodes": []}

mismatches_count = int(file.readline().strip())
    
for i in range(mismatches_count):
    current = file.readline().strip().split()
    graph[current[1]]["nodes"].append(current[0])
    graph[current[0]]["nodes"].append(current[1])


def recursive_search(graph, node):
    queue = deque([node])
    graph[node]["color"] = 0

    while queue:
        current = queue.popleft()
        current_color = graph[current]["color"]

        new_color = 1 - current_color

        for path in graph[current]["nodes"]:
            if graph[path]["color"] == -1:
                graph[path]["color"] = new_color
                queue.append(path)
            elif graph[path]["color"] == current_color:
                return False
    return True

correct = True
for node in graph:
    if graph[node]["color"] == -1:
        correct = recursive_search(graph, node)
        if not correct:
            break

walter_list = []
jessie_list = []

if not correct:
    print('impossible')
else:
    for node in graph:
        if (graph[node]["color"]) == 1:
            walter_list.append(node)
        else:
            jessie_list.append(node)
    print(" ".join(str(x) for x in walter_list))
    print(" ".join(str(x) for x in jessie_list))

