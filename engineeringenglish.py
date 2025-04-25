import sys

file = open("input.txt", "r")

words = set()

while(True):
    line = file.readline().strip().split()
    if (not line):
        break

    output = []

    for word in line:
        if (word.lower() in words):
            output.append(".")
        else:
            output.append(word)
            words.add(word.lower())
    print(" ".join(output))