from copy import deepcopy

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
old_field = []
for line in field_strings:
    old_field.append(list(line))

field = []

for i in range(len(old_field)):
    line = []
    for j in range(len(old_field[0])):
        match old_field[i][j]:
            case '#':
                line.extend(['#', '#'])
            case '.':
                line.extend(['.', '.'])
            case '@':
                line.extend(['@', '.'])
            case 'O':
                line.extend(['[', ']'])
    field.append(line)

robot_location = get_robot_location(field)
field[robot_location[1]][robot_location[0]] = '.'


for i, step in enumerate(steps):
    direction = directions[step]
    if step in ('<', '>'):
        line = field[robot_location[1]].copy()
        if line[robot_location[0] + direction[0]] == '#':
            continue
        elif line[robot_location[0] + direction[0]] == '.':
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
        if field[robot_location[1] + direction[1]][robot_location[0]] == '#':
            continue
        elif field[robot_location[1] + direction[1]][robot_location[0]] == '.':
            robot_location = (robot_location[0], robot_location[1] + direction[1])
        else:
            wall = False
            boxes_to_move = {(robot_location[0], robot_location[1] + direction[1])}
            if field[robot_location[1] + direction[1]][robot_location[0]] == '[':
                boxes_to_move.add((robot_location[0] + 1, robot_location[1] + direction[1]))
            elif field[robot_location[1] + direction[1]][robot_location[0]] == ']':
                boxes_to_move.add((robot_location[0] - 1, robot_location[1] + direction[1]))
            # we need to gather all boxes tiles to move

            range_value = len(field) - robot_location[1] if step == 'v' else robot_location[1] + 1
            for krok in range(2, range_value):
                next_line = [
                    {
                        'char': field[box_coords[1] + direction[1]][box_coords[0]],
                        'coordinates': (box_coords[0], box_coords[1] + direction[1])
                    } for box_coords in boxes_to_move if box_coords[1] == robot_location[1] + direction[1] * (krok-1)
                ]
                if all(symbol['char'] == '.' for symbol in next_line):
                    break
                if any(symbol['char'] == '#' for symbol in next_line):
                    wall = True
                    break
                for symbol in next_line:
                    if symbol['char'] == ']':
                        boxes_to_move.add((symbol['coordinates'][0], symbol['coordinates'][1]))
                        boxes_to_move.add((symbol['coordinates'][0] - 1, symbol['coordinates'][1]))
                    elif symbol['char'] == '[':
                        boxes_to_move.add((symbol['coordinates'][0], symbol['coordinates'][1]))
                        boxes_to_move.add((symbol['coordinates'][0] + 1, symbol['coordinates'][1]))

            if not wall:
                robot_location = (robot_location[0], robot_location[1] + direction[1])
                field_copy = deepcopy(field)
                boxes_to_move = sorted(boxes_to_move, key=lambda box: box[1], reverse=step == 'v')
                for box in boxes_to_move:
                    field[box[1]][box[0]] = '.'
                    field[box[1] + direction[1]][box[0]] = field_copy[box[1]][box[0]]


with open('output.txt', 'w') as file:
    for line in field:
        file.write(''.join(line) + '\n')

answer = 0
for y in range(len(field)):
    for x in range(len(field[0])):
        if field[y][x] == '[':
            answer += y * 100 + x

print(answer)



