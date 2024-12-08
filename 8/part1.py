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
        new_points = [(location1[0] + diffx, location1[1] + diffy), (location2[0] - diffx, location2[1] - diffy)]
        for point in new_points:
            if location_is_valid(*point):
                antinodes.add(point)
                new_data[point[1]] = new_data[point[1]][:point[0]] + '#' + new_data[point[1]][point[0] + 1:]

print(len(antinodes))
print(new_data)
