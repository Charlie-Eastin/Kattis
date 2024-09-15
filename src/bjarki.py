import sys

file = open("input.txt", 'r')

line = file.readline().strip().split()
#line = sys.stdin.readline().strip().split()

height = int(line[0])
width = int(line[1])

movement_map = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}

data = {}

shortcuts = {}

for x in range(height):
    line = file.readline().strip()
    #line = sys.stdin.readline().strip()
    for y in range(width):
        temp_x, temp_y = movement_map.get(line[y])
        temp_x = temp_x + x
        temp_y = temp_y + y
        data[(x ,y)] = (temp_x, temp_y)

query_count = int(file.readline().strip())
#query_count = int(sys.stdin.readline().strip())

for i in range(query_count):
    line = file.readline().strip().split()
    #line = sys.stdin.readline().strip().split()
    x = int(line[0]) - 1
    y = int(line[1]) - 1
    query = int(line[2])
    original_x = x
    original_y = y
    path = []
    step = 0
    #for step in range(query):
    while step < query:
        if ((x, y) in shortcuts):
            max_value = max((k for k in shortcuts[(x, y)] if k <= (query - step)), default=None)
            if max_value is not None:
                x, y = shortcuts[(x, y)][max_value]
                step += max_value
                if (step == query):
                    break
                continue
        else:
            x, y = data[(x, y)]
            if ((x, y) not in path):
                path.append((x, y))
            if ((original_x, original_y) not in shortcuts):
                shortcuts[(original_x, original_y)] = {}

            shortcuts[(original_x, original_y)][(step + 1)] = (x, y)
        step += 1

    for index, (temp_x, temp_y) in enumerate(path):
        for steps in range(1, len(path) - index):
            if (temp_x, temp_y) not in shortcuts:
                shortcuts[(temp_x, temp_y)] = {}
            shortcuts[(temp_x, temp_y)][steps] = path[index + steps]
     
    print(x + 1, y + 1)
#print(shortcuts)   
