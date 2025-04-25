import sys
import math

file = open("input.txt", "r")

cases = int(file.readline().strip())

def sorter(item):
    return item[0]

def find(value, edges_set):
    starting_value = value
    while(edges_set[value] > 0):
        value = edges_set[value]
    
    if value == starting_value:
        return 0
    return value

for _ in range(cases):
    coordinate_count = int(file.readline().strip())
    coordinate_list = []
    for _ in range(coordinate_count):
        coordinate_x, coordinate_y = list(map(float, file.readline().strip().split()))
        coordinate_list.append((coordinate_x, coordinate_y))
    edges = []
    for i in range(coordinate_count):
        for j in range(i + 1, coordinate_count):
            edges.append([math.dist(coordinate_list[i], coordinate_list[j]), (coordinate_list[i][0], coordinate_list[i][1]), (coordinate_list[j][0], coordinate_list[j][1])])

    edges.sort(key=sorter)
    #print(edges)
    edges_set = [-1] * len(edges)

    distance = 0
    size = (len(coordinate_list) - 1) * -1
    for i in range(len(edges)):
        edge_1 = edges[i][1]
        edge_2 = edges[i][2]

        index1 = coordinate_list.index(edge_1)
        index2 = coordinate_list.index(edge_2)

        if (edges_set[index1] < 0 and edges_set[index2] < 0):
            temp = edges_set[index1]
            edges_set[index1] = index2
            edges_set[index2] += temp
            distance += edges[i][0]
            if edges_set[index2] == size:
                break
        elif(edges_set[index1] < 0 and edges_set[index2] > 0):
            value = find(edges_set[index2], edges_set)
            temp = edges_set[index1]
            edges_set[index1] = value
            edges_set[value] += temp
            distance += edges[i][0]
            if edges_set[index2] == size:
                break
        elif(edges_set[index1] > 0 and edges_set[index2] < 0):
            value = find(edges_set[index1], edges_set)
            temp = edges_set[index1]
            edges_set[index2] = value
            edges_set[value] += temp
            distance += edges[i][0]
            if edges_set[index2] == size:
                break
            
        
    print(distance)

