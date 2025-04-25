import sys

file = open("input.txt", 'r')

observations = int(file.readline().strip())

total_seconds = 0
total_minutes = 0

for _ in range(observations):
    minutes_displayed, seconds_waited = map(int, file.readline().strip().split())

    total_seconds += seconds_waited
    total_minutes += minutes_displayed

sl = total_seconds / total_minutes
real_minutes = sl / 60

if (real_minutes <= 1):
    print("measurement error")
else:
    print(round(real_minutes, 9))
