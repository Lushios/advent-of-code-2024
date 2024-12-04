with open("input.txt") as file:
    data = file.read().splitlines()


def get_directions(x, y, data):
    if data[y][x] != 'X':
        return []
    possible_directions = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    remove = []
    if x < 3:
        remove.extend([(-1, 1), (-1, 0), (-1, -1)])
    if x > len(data[y]) - 4:
        remove.extend([(1, 1), (1, 0), (1, -1)])
    if y < 3:
        remove.extend([(-1, -1), (0, -1), (1, -1)])
    if y > len(data) - 4:
        remove.extend([(-1, 1), (0, 1), (1, 1)])
    remove = set(remove)

    result = [direction for direction in possible_directions if direction not in remove]

    return result


def check_for_XMAS(x, y, direction, data):
    word = data[y][x]
    for i in range(1, 4):
        word += data[y + direction[1] * i][x + direction[0] * i]

    if word in ('XMAS'):
        return True
    return False


XMAS_counter = 0

for y in range(len(data)):
    for x in range(len(data[0])):
        directions = get_directions(x, y, data)
        for direction in directions:
            is_XMAS = check_for_XMAS(x, y, direction, data)
            if is_XMAS:
                XMAS_counter += 1

print(XMAS_counter)
