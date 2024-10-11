import sys

file = open("src/input.txt", 'r')

nodes_count = int(file.readline().strip())

nodes = []

for i in range(nodes_count):
    nodes.append(file.readline().strip())

mismatches_count = int(file.readline().strip())


graph = {}

for i in range(mismatches_count):
    current = file.readline().strip().split()
    if (current[0] not in graph):
        graph[current[0]] = {"color": -1, "nodes": []}
    if (current[1]not in graph):
        graph[current[1]] = {"color": -1, "nodes": []}
    
    graph[current[1]]["nodes"].append(current[0])
    graph[current[0]]["nodes"].append(current[1])


def recursive_search(graph, node, color):
    if (graph[node]["color"] == color):
        return True
    if (graph[node]["color"] != color and graph[node]["color"] != -1):
        return False
    graph[node]["color"] = color
    for curr_node in graph[node]["nodes"]:
        current_color = graph[curr_node]["color"]
        if (current_color == -1):
            current_color = color
        for path in graph[node]["nodes"]:
            if (color == 0):
                new_color = -1
            if (color == 1):
                new_color = 0
            correct = recursive_search(graph, path, new_color)
            if (correct == False):
                return False

color = 0
for node in graph:
    if graph[node]["color"] == -1:
        correct = recursive_search(graph, node, color)
        if (correct == False):
            break
        if (color == 0):
            color = 1
        else:
            color = 0

walter_list = []
jessie_list = []

if (correct == False):
    print('impossible')
else:
    for node in graph:
        if (graph[node]["color"]) == 1:
            walter_list.append(node)
        else:
            jessie_list.append(node)

print(walter_list)
print(jessie_list)


    





