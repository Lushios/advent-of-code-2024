from collections import deque
from math import inf

with open("input.txt") as file:
    data = file.read().splitlines()

directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

start = (0, 0)
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'S':
            start = (j, i)
            break


def get_directions_for_position(position):
    possible_directions = []
    for direction in directions:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if 0 <= new_position[0] < len(data[0]) and 0 <= new_position[1] < len(data):
            if data[new_position[1]][new_position[0]] != '#':
                possible_directions.append(direction)
    return possible_directions


class Path:
    def __init__(self, path: deque = deque([start]), score=0, direction=(1, 0)):
        self.path = path
        self.score = score
        self.direction = direction
        self.is_terminated = False
        self.is_finish = False

    def add_to_path(self, position):
        new_direction = (position[0] - self.path[-1][0], position[1] - self.path[-1][1])
        self.path.append(position)
        self.score += 1
        if new_direction != self.direction:
            self.direction = new_direction
            self.score += 1000


paths = [Path()]
lowest_score = inf

shortest_distance_to = {}
for i in range(len(data)):
    for j in range(len(data[i])):
        shortest_distance_to[(j, i)] = inf

while any([not path.is_terminated for path in paths]):
    new_paths = []
    for current_path in [path for path in paths if not path.is_terminated]:
        if current_path.score > lowest_score:
            current_path.is_terminated = True
        if current_path.is_terminated:
            continue
        current_element = current_path.path[-1]
        possible_directions = get_directions_for_position(current_element)
        possible_steps = [
            (current_element[0] + possible_direction[0], current_element[1] + possible_direction[1])
            for possible_direction in possible_directions
            if (current_element[0] + possible_direction[0], current_element[1] + possible_direction[1])
            not in current_path.path
        ]
        if len(possible_steps) == 0:
            current_path.is_terminated = True
            continue
        else:
            for step in possible_steps:
                if data[step[1]][step[0]] == 'E':
                    current_path.add_to_path(step)
                    current_path.is_finish = True
                    current_path.is_terminated = True
                    break
            if current_path.is_finish:
                if current_path.score < lowest_score:
                    lowest_score = current_path.score
                continue
            step_for_the_current_path = possible_steps.pop()
            for step in possible_steps:
                new_path = Path(current_path.path.copy(), current_path.score, current_path.direction)
                new_path.add_to_path(step)
                if new_path.score < shortest_distance_to[step]:
                    shortest_distance_to[step] = new_path.score
                else:
                    continue
                new_paths.append(new_path)
            current_path.add_to_path(step_for_the_current_path)
            if current_path.score < shortest_distance_to[step_for_the_current_path]:
                shortest_distance_to[step_for_the_current_path] = current_path.score
            else:
                current_path.is_terminated = True
    paths.extend(new_paths)


print(lowest_score)
