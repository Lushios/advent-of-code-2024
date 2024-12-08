from itertools import combinations

with open("input.txt") as file:
    data = file.read().splitlines()

MAX_X = len(data[0])
MAX_Y = len(data)


def location_is_valid(x, y):
    return 0 <= x < MAX_X and 0 <= y < MAX_Y


antennae_positions = {}

for y in range(MAX_Y):
    for x in range(MAX_X):
        if data[y][x] != '.':
            if data[y][x] in antennae_positions:
                antennae_positions[data[y][x]].append((x, y))
            else:
                antennae_positions[data[y][x]] = [(x, y)]

antinodes = set()
new_data = data.copy()

for key, locations in antennae_positions.items():
    location_combinations = combinations(locations, 2)
    for location1, location2 in location_combinations:
        diffx, diffy = location1[0] - location2[0], location1[1] - location2[1]
        for direction in ['positive', 'negative']:
            if direction == 'positive':
                newx, newy = location1[0], location1[1]
            else:
                newx, newy = location2[0], location2[1]
            while True:
                if direction == 'positive':
                    newx, newy = newx + diffx, newy + diffy
                    if not location_is_valid(newx, newy):
                        break
                    else:
                        antinodes.add((newx, newy))
                        new_data[newy] = new_data[newy][:newx] + '#' + new_data[newy][newx + 1:]
                else:
                    newx, newy = newx - diffx, newy - diffy
                    if not location_is_valid(newx, newy):
                        break
                    else:
                        antinodes.add((newx, newy))
                        new_data[newy] = new_data[newy][:newx] + '#' + new_data[newy][newx + 1:]


for key, value in antennae_positions.items():
    for point in value:
        antinodes.add(point)

print(len(antinodes))
