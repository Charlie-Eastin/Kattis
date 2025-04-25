import sys
import math

file = open("input.txt", 'r')

def check_sour(x1, y1, x2, y2, sour_dist):
    x_distance = (x1 - x2) ** 2
    y_distance = (y1 - y2) ** 2

    distance = math.sqrt(x_distance + y_distance)

    if (distance <= sour_dist):
        return True
    return False

while(True):
    line = file.readline().strip().split()
    if len(line) == 0 or line[0] == "0.0" and line[1] == "0":
        break
    distance = float(line[0])
    hives_count = int(line[1])
    coordinate_list = []
    sour_list = [False] * hives_count

    for i in range(hives_count):
        line = file.readline().strip().split()
        coordinate = [float(line[0]), float(line[1])]
        coordinate_list.append(coordinate)


    for i in range(len(coordinate_list)):
        for j in range(i + 1, len(coordinate_list)):
            sour = check_sour(coordinate_list[i][0], coordinate_list[i][1], coordinate_list[j][0], coordinate_list[j][1], distance)
            if (sour):
                sour_list[i] = True
                sour_list[j] = True

    count = 0
    for i in range(len(sour_list)):
        if sour_list[i] == True:
            count +=1

    print(f"{count} sour, {len(sour_list) - count} sweet")
        


