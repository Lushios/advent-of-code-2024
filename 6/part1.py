with open("input.txt") as file:
    data = file.read().splitlines()


turns = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
}

start = (0, 0)

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == '^':
            start = (x, y)
            break

visited_places = set()

out_of_bounds = False
direction = (0, -1)
current_position = start

while not out_of_bounds:
    if (
            current_position[1] + direction[1] >= len(data) or
            current_position[0] + direction[0] >= len(data[0]) or
            current_position[1] + direction[1] < 0 or
            current_position[0] + direction[0] < 0
    ):
        out_of_bounds = True
        break

    visited_places.add(current_position)
    if data[current_position[1] + direction[1]][current_position[0] + direction[0]] == '#':
        direction = turns[direction]
    current_position = (current_position[0] + direction[0], current_position[1] + direction[1])

    # data[current_position[1]] = (
    #         data[current_position[1]][:current_position[0]] + 'X'
    #         + data[current_position[1]][:current_position[0] + 1:]
    # )


print(visited_places)
