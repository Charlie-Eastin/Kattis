import sys

line = sys.stdin.readline().strip().split()

sticks = int(line[0])
size = int(line[1])

graph = {}
nodes = []


for i in range(size):
    line = sys.stdin.readline().strip().split()

    vertex1 = line[0]
    vertex2 = line[1]

    if vertex1 not in graph:
        graph[vertex1] = []
    if vertex2 not in graph:
        graph[vertex2] = []
    if vertex1 not in nodes:
        nodes.append(vertex1)
    if vertex2 not in nodes:
        nodes.append(vertex2)

    graph[vertex1].append(vertex2)

#print(graph)

def search(nodes):
    found = False
    for key, value in graph.items():
        if (found == True):
            for item in nodes_list:
                print(item)
            return True
        visited = []
        queue = []
        queue.append(key)
        visited.append(key)
        nodes_list = []
        while(len(queue) > 0): 
            node = queue.pop(0)
            nodes_list.append(node) 
            for path in graph[node]:
                if (path not in visited):
                    queue.append(path)
                else:
                    print("IMPOSSIBLE")
                    return False
            if len(nodes_list) == len(nodes):
                found = True

search(nodes)