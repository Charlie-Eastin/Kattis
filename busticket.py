import sys

file = open("input.txt", 'r')


price_single_trip, price_period_ticket, period_length, trips_count = list(map(int, file.readline().strip().split()))
trips = []

for _ in range(trips_count):
    trips = list(map(int, file.readline().strip().split()))

dp = []







