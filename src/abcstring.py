import sys

file = open("src/input.txt", "r")
VALUE_SUBTRACTION = ord('A')


def check_perfect(perfect_string):
    current_letter = perfect_string[0]
    count = 0
    max_count = 0
    for i in range(len(perfect_string)):
        if current_letter == perfect_string[i]:
            count += 1
            if (count > max_count):
                max_count = count
        else:
            count = 1
            current_letter = perfect_string[i]
    print(max_count)
        
perfect_string = file.readline().strip()
check_perfect(perfect_string)




#     perfect_string_list = []

#     for i in range(size):
#         perfect_string_list.append([False, False, False])

#     current_index = 0
#     count_switches = 0
#     i = 0
#     while i < len(perfect_string):

#         if count_switches == size:
#             return False
        
#         letter = ord(perfect_string[i])

#         if (perfect_string_list[current_index][0] is True and perfect_string_list[current_index][1] is True and perfect_string_list[current_index][2] is True):
#             perfect_string_list[current_index][0] = False
#             perfect_string_list[current_index][1] = False
#             perfect_string_list[current_index][2] = False
#             if (current_index >= (size - 1)):
#                 current_index = 0
#             else:
#                 current_index += 1
        
#         if perfect_string_list[current_index][letter - VALUE_SUBTRACTION] is not True:
#             count_switches = 0
#             perfect_string_list[current_index][letter - VALUE_SUBTRACTION] = True

#         else:
#             count_switches += 1
#             i -= 1
#             if (current_index >= (size - 1)):
#                 current_index = 0
#             else:
#                 current_index += 1

#         i += 1
#     return True

# perfect_string = file.readline().strip()

# high_value = (len(perfect_string) // 3) + 1
# low_value = 1
# while (low_value < high_value):
#     middle_value = (low_value + high_value) // 2
    
#     if (check_perfect(perfect_string, middle_value)):       
#         high_value = middle_value
#     else:
#         low_value = middle_value + 1

# print(high_value)
