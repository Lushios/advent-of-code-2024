with open("input.txt") as file:
    data = file.read().splitlines()

directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

start = (0, 0)
walls = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'S':
            start = (j, i)
        elif data[i][j] == '#' and i != 0 and i != len(data) - 1 and j != 0 and j != len(data[i]) - 1:
            neighbors = []
            for direction in directions:
                dx, dy = direction
                neighbors.append((j + dx, i + dy))
            if not all(neighbor in walls for neighbor in neighbors):
                walls.append((j, i))


wall_times = []


def find_path(data, swapped_wall, basic_path):
    path = [start]
    while True:
        x, y = path[-1]
        if data[y][x] == 'E':
            return path
        force_way = False
        for dx, dy in directions:
            if (x + dx, y + dy) == swapped_wall and (x + dx, y + dy) not in path:
                path.append((x + dx, y + dy))
                force_way = True
                break
        if not force_way:
            possible_steps = []
            for dx, dy in directions:
                if (
                        0 <= x + dx < len(data[0])
                        and 0 <= y + dy < len(data)
                        and data[y + dy][x + dx] != '#'
                        and (x + dx, y + dy) not in path
                ):
                    possible_steps.append((x + dx, y + dy))
            if len(possible_steps) == 1:
                path.append(possible_steps[0])
            elif len(possible_steps) == 0:
                return None
            else:
                step_rankings = {step: basic_path.index(step) for step in possible_steps}
                next_step = max(step_rankings, key=step_rankings.get)
                path.extend(basic_path[basic_path.index(next_step):])
                return path


base_path = find_path(data, [], [])

print(len(walls))

for i, wall in enumerate(walls):
    print(i)
    adjacent_steps = []
    for direction in directions:
        dx, dy = direction
        if (wall[0] + dx, wall[1] + dy) in base_path:
            adjacent_steps.append((wall[0] + dx, wall[1] + dy))
    if len(adjacent_steps) != 2:
        continue
    step_rankings = {step: base_path.index(step) for step in adjacent_steps}
    next_step = max(step_rankings, key=step_rankings.get)
    previous_step = min(step_rankings, key=step_rankings.get)
    wall_times.append(len(base_path[:base_path.index(previous_step)]) + len(base_path[base_path.index(next_step):]))


print(len([wall_time for wall_time in wall_times if len(base_path) - 1 - wall_time > 100]))
