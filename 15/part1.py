import time
t0 = time.time()

with open("input.txt") as file:
    data = file.read()


directions = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, -1),
    'v': (0, 1)
}


def get_robot_location(data) -> tuple[int, int]:
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == '@':
                return j, i


field_string, steps = data.split("\n\n")
steps = steps.replace("\n", "")
field_strings = field_string.splitlines()
field = []
for line in field_strings:
    field.append(list(line))
robot_location = get_robot_location(field)
field[robot_location[1]][robot_location[0]] = '.'

for step in steps:
    direction = directions[step]
    if step in ('<', '>'):
        line = field[robot_location[1]].copy()
        if line[robot_location[0] + direction[0]] == '#':
            continue
        elif line[robot_location[0] + direction[0]] == '.':
            field[robot_location[1]][robot_location[0]] = '.'
            robot_location = (robot_location[0] + direction[0], robot_location[1])
        else:
            wall = False
            boxes_to_move = [robot_location[0] + direction[0]]
            range_value = len(line) - robot_location[0] if step == '>' else robot_location[0] + 1
            for krok in range(2, range_value):
                next_symbol = line[robot_location[0] + krok * direction[0]]
                if next_symbol == '#':
                    wall = True
                    break
                elif next_symbol == '.':
                    break
                else:
                    boxes_to_move.append(robot_location[0] + krok * direction[0])
            if not wall:
                for box in boxes_to_move:
                    field[robot_location[1]][box] = line[box - direction[0]]
                    field[robot_location[1]][box + direction[0]] = line[box]
                robot_location = (robot_location[0] + direction[0], robot_location[1])
    elif step in ('^', 'v'):
        column = [field[i][robot_location[0]] for i in range(len(field))]
        if column[robot_location[1] + direction[1]] == '#':
            continue
        elif column[robot_location[1] + direction[1]] == '.':
            field[robot_location[1]][robot_location[0]] = '.'
            robot_location = (robot_location[0], robot_location[1] + direction[1])
        else:
            wall = False
            boxes_to_move = [robot_location[1] + direction[1]]
            range_value = len(column) - robot_location[1] if step == 'v' else robot_location[1] + 1
            for krok in range(2, range_value):
                next_symbol = column[robot_location[1] + krok * direction[1]]
                if next_symbol == '#':
                    wall = True
                    break
                elif next_symbol == '.':
                    break
                else:
                    boxes_to_move.append(robot_location[1] + krok * direction[1])
            if not wall:
                for box in boxes_to_move:
                    field[box][robot_location[0]] = column[box - direction[1]]
                    field[box + direction[1]][robot_location[0]] = column[box]
                robot_location = (robot_location[0], robot_location[1] + direction[1])


with open('output.txt', 'w') as file:
    for line in field:
        file.write(''.join(line) + '\n')

answer = 0
for y in range(len(field)):
    for x in range(len(field[0])):
        if field[y][x] == 'O':
            answer += y * 100 + x


t1 = time.time()

print(answer)
print((t1 - t0) * 1000, " ms")


