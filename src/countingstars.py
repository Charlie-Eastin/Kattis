import sys
import math

def breadth_first_search(sky, i, j, visited):
  queue = []
  queue.append([i,j])
  while(len(queue) > 0):
    node = queue.pop(0)
    x = node[0]
    y = node[1]
    
    if visited[x][y] == 1:
      continue
    else:
      visited[x][y] = 1


    if y > 0 and sky[x][y - 1] == '-' :
      queue.append([x, y - 1])
    if y < (len(sky[0]) - 1) and sky[x][y + 1] == '-':
      queue.append([x, y + 1])
    if x > 0 and sky[x - 1][y] == '-':
      queue.append([x - 1, y])
    if x < (len(sky) - 1) and sky[x + 1][y] == '-':
      queue.append([x + 1, y])
    


case = 0
while(True):
  line = sys.stdin.readline().strip().split()
  if not line:
    break

  height = int(line[0])
  width = int(line[1])
  sky = []

  for i in range(height):
    line = sys.stdin.readline().strip()
    sky.append(line)

  visited = []

  for i in range(height):
    visited.append([0] * width)

  count = 0

  for i in range(0, height, 1):
    for j in range(0, width, 1):
      if (sky[i][j] == '-' and visited[i][j] == 0):
        breadth_first_search(sky, i, j, visited)
        count += 1
  case += 1
  print(f"Case {case}: {count}")





