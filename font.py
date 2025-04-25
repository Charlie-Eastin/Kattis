import sys
from itertools import permutations, chain, combinations
file = open("input.txt", "r")

word_count = int(file.readline().strip())

routines = []

for i in range(word_count):
    routine = file.readline().strip()
    routines.append(set(routine))

def get_count(iteration):
    combined_set = set().union(*iteration)
    if (len(combined_set) == 26):
        return True
    return False


def get_permutations(lst):
    new_list = list(chain.from_iterable(combinations(lst, r) for r in range(1, len(lst) + 1)))
    return new_list

count = 0
for iteration in get_permutations(routines):
    found = get_count(iteration)
    if found:
        count += 1
    

print(count)