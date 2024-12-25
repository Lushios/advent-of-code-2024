with open("input.txt") as file:
    data = file.read().splitlines()

directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

start = (0, 0)
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'S':
            start = (j, i)


def find_path(data):
    path = [start]
    while True:
        x, y = path[-1]
        if data[y][x] == 'E':
            return path
        for dx, dy in directions:
            if (
                    0 <= x + dx < len(data[0])
                    and 0 <= y + dy < len(data)
                    and data[y + dy][x + dx] != '#'
                    and (x + dx, y + dy) not in path
            ):
                path.append((x + dx, y + dy))
                break


base_path = find_path(data)
print(len(base_path) - 1, base_path)
cool_paths_counter = 0
savings = {}

for i in range(len(base_path) - 100):
    print(i)
    point = base_path[i]
    for j, point2 in enumerate(base_path):
        distance_between_points = abs(point[0] - point2[0]) + abs(point[1] - point2[1])
        time_savings = j - i - distance_between_points
        if time_savings < 100:
            continue
        if distance_between_points <= 20:
            cool_paths_counter += 1
            if time_savings not in savings:
                savings[time_savings] = 1
            else:
                savings[time_savings] += 1


print(cool_paths_counter)
print(savings)
