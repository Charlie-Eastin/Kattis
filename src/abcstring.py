import sys

file = open("input.txt", "r")


def check_perfect(perfect_string, size):

    perfect_string_list = []

    for i in range(size):
        perfect_string_list.append([False, False, False])

    current_index = 0
    count_switches = 0
    i = 0
    while i < len(perfect_string):

        if count_switches == size:
            return False

        letter = perfect_string[i]

        if (perfect_string_list[current_index][0] is True and perfect_string_list[current_index][1] is True and perfect_string_list[current_index][2] is True):
            perfect_string_list[current_index][0] = False
            perfect_string_list[current_index][1] = False
            perfect_string_list[current_index][2] = False
            if (current_index >= (size - 1)):
                current_index = 0
            else:
                current_index += 1
        
        if letter == 'A' and perfect_string_list[current_index][0] is not True:
            count_switches = 0
            perfect_string_list[current_index][0] = True

        elif letter == 'B' and perfect_string_list[current_index][1] is not True:
            count_switches = 0
            perfect_string_list[current_index][1] = True
        
        elif letter == 'C' and perfect_string_list[current_index][2] is not True:
            count_switches = 0
            perfect_string_list[current_index][2] = True

        else:
            count_switches += 1
            i -= 1
            if (current_index >= (size - 1)):
                current_index = 0
            else:
                current_index += 1

        i += 1
    return True

perfect_string = file.readline().strip()

high_value = 100000
low_value = 1
while (low_value < high_value):
    middle_value = (low_value + high_value) // 2
    
    if (check_perfect(perfect_string, middle_value)):       
        high_value = middle_value
    else:
        low_value = middle_value + 1

print(high_value)