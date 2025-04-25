import sys
import itertools

#file = open("src/input.txt", "r")

routine_count = int(sys.stdin.readline().strip())

routines = []

for i in range(routine_count):
    routine = sys.stdin.readline().strip()
    routines.append(set(routine))

intersections = [[0] * routine_count for _ in range(routine_count)] #intersection matrix to avoid redundant intersection lookups 

for i in range(routine_count):
    for j in range(routine_count):
        if i != j:
            intersections[i][j] = len(routines[i] & routines[j])

def count_changes(routines, min_changes):
    changes = 0
    for i in range(len(routines) - 1):
        changes += intersections[routines[i]][routines[i + 1]]
        if changes >= min_changes:
            return changes
    return changes

def min_changes(routines):
    min_changes = sys.maxsize
    routines_len = len(routines)
    routine_indexes = list(range(routines_len)) # Getting the indexes as a list
    for permutation in itertools.permutations(routine_indexes):
        changes = count_changes(permutation, min_changes)
        min_changes = min(min_changes, changes)
    return min_changes


minimum = min_changes(routines)
print(minimum)

