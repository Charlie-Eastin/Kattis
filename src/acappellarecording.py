import sys

file = open("input.txt", "r")

n, d = file.readline().strip().split()

n, d = int(n), int(d)

notes = []

for i in range(n):
    notes.append(int(file.readline().strip()))

notes.sort()

recording_count = 1
current_note = notes[0]

for note in notes:
    if note - current_note > d:
        recording_count += 1
        current_note = note

print(recording_count)
    