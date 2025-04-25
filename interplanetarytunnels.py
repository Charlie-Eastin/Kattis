import sys
from collections import deque
import math

file = open("input.txt", "r")

planets, tunnels = list(map(int, file.readline().strip().split()))

alice, bob = list(map(int, file.readline().strip().split()))

graph = {}

for _ in range(tunnels):
    planet_1, planet_2 = list(map(int, file.readline().strip().split()))

    if planet_1 not in graph:
        graph[planet_1] = [planet_2]
    else:
        graph[planet_1].append(planet_2)

    if planet_2 not in graph:
        graph[planet_2] = [planet_1]
    else:
        graph[planet_2].append(planet_1)

def bfs(graph, alice, bob):
    queue = deque([alice])
    found = {}
    found[alice] = 0
    while(len(queue)):
        current_panet = queue.popleft()
        distance = found[current_panet]
        for planet in graph[current_panet]:
            if planet == bob:
                return distance + 1
            if planet not in found:
                found[planet] = distance + 1
                queue.append(planet)
    return None

distance = bfs(graph, alice, bob)

print(math.ceil(distance / 2))



