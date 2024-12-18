from math import inf
from collections import deque

with open("input.txt") as file:
    input = file.read().splitlines()

X_LEN = 71
Y_LEN = 71

walls = []

for line in input:
    wallx, wally = line.split(",")
    walls.append((int(wallx), int(wally)))

data = [["." for _ in range(X_LEN)] for _ in range(Y_LEN)]


for wall in walls:
    data[wall[1]][wall[0]] = "#"

with open('output.txt', 'w') as file:
    for line in data:
        file.write("".join(line) + "\n")

# yeah I used my code from part 16, FUCKING SUE ME
