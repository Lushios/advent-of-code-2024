with open("input.txt") as file:
    data = file.read().splitlines()


directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def find_trails(x, y, nines):
    local_directions = []
    if x > 0:
        local_directions.append((-1, 0))
    if x < len(data[0]) - 1:
        local_directions.append((1, 0))
    if y > 0:
        local_directions.append((0, -1))
    if y < len(data) - 1:
        local_directions.append((0, 1))

    if data[y][x] == '8':
        return [(x + x1, y + y1) for x1, y1 in local_directions if data[y + y1][x + x1] == '9']
    for direction in local_directions:
        if int(data[y + direction[1]][x + direction[0]]) - int(data[y][x]) == 1:
            trails = find_trails(x + direction[0], y + direction[1], nines)
            if trails:
                nines.extend(trails)


answa = 0
for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '0':
            nines = []
            trails = find_trails(x, y, nines)
            answa += len(nines)

print(answa)
