import sys

file = open("input.txt")

reactants_count, experiments_count = list(map(int, file.readline().strip().split()))

reactivity_table = {}

visited = [0] * reactants_count

reactant_stack = []

unique_order = [True]

def dfs(reactant, reactivity_table, visited, reactant_stack, unique_order):
    if (visited[reactant] == 1):
        return True
    if (visited[reactant] == 2):
        return False
    
    visited[reactant] = 1

    if reactant in reactivity_table:
        for metal in reactivity_table[reactant]:
            if (dfs(metal, reactivity_table, visited, reactant_stack, unique_order)):
                return True

    visited[reactant] = 2
    reactant_stack.append(reactant)
    return False

for _ in range(experiments_count):
    reactant_a, reactant_b = list(map(int, file.readline().strip().split()))
    if (reactant_a not in reactivity_table):
        reactivity_table[reactant_a] = []
    reactivity_table[reactant_a].append(reactant_b)

for i in range(reactants_count):
    if i not in reactivity_table:
        reactivity_table[i] = []

has_cycle = False
for reactant in range(reactants_count):
    if (visited[reactant] == 0):
        if (dfs(reactant, reactivity_table, visited, reactant_stack, unique_order)):
            has_cycle = True
            break

if (has_cycle or not unique_order[0]):
    print("back to the lab")
else:
    starting_nodes = 0
    degree = [0] * reactants_count
    for reactant in reactivity_table:
        for metal in reactivity_table[reactant]:
            degree[metal] += 1
    for i in degree:
        if i == 0:
            starting_nodes += 1

    if (starting_nodes > 1):
        print("back to the lab")
    else:
        print(*reversed(reactant_stack))
    

