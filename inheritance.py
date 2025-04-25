import sys

suns = int(sys.stdin.readline().strip())

current = '0'
children = []

def bfs(current, suns):
    if (int(current) > suns):
        return
    
    if (suns % int(current) == 0):
        children.append(int(current))
    current_2 = current + "2"
    current_4 = current + "4"
    
    bfs(current_2, suns)
    bfs(current_4, suns)

bfs('2', suns)
bfs('4', suns)

children.sort()

for child in children:
    print(child)


