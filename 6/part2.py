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

direction = (0, -1)
current_position = start

while True:
    if (
            current_position[1] + direction[1] >= len(data) or
            current_position[0] + direction[0] >= len(data[0]) or
            current_position[1] + direction[1] < 0 or
            current_position[0] + direction[0] < 0
    ):
        visited_places.add(current_position)
        break

    visited_places.add(current_position)
    if data[current_position[1] + direction[1]][current_position[0] + direction[0]] == '#':
        direction = turns[direction]
    current_position = (current_position[0] + direction[0], current_position[1] + direction[1])

visited_places.remove(start)


def add_obstacle(data, obstacle_location):
    new_data = data.copy()
    x, y = obstacle_location
    new_data[y] = new_data[y][:x] + '#' + new_data[y][x + 1:]
    return new_data


def check_for_loops(field):
    # visited_places_with_directions = set()
    obstacles_hit = set()

    direction = (0, -1)
    current_position = start
    while True:
        # print(field[current_position[1]][current_position[0]])
        if (
                current_position[1] + direction[1] >= len(field) or
                current_position[0] + direction[0] >= len(field[0]) or
                current_position[1] + direction[1] < 0 or
                current_position[0] + direction[0] < 0
        ):
            return False
        # if tuple([current_position[0], current_position[1], direction]) in visited_places_with_directions:
        #     return True
        # visited_places_with_directions.add((current_position[0], current_position[1], direction))
        if field[current_position[1] + direction[1]][current_position[0] + direction[0]] == '#':
            if (current_position[0] + direction[0], current_position[1] + direction[1], direction) in obstacles_hit:
                return True
            obstacles_hit.add((current_position[0] + direction[0], current_position[1] + direction[1], direction))
            direction = turns[direction]
        else:
            current_position = (current_position[0] + direction[0], current_position[1] + direction[1])


final_answer = 0
for obstacle_location in visited_places:
    new_data = add_obstacle(data, obstacle_location)
    result = check_for_loops(new_data)
    if result:
        final_answer += 1

print(final_answer)
