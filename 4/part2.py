with open("input.txt") as file:
    data = file.read().splitlines()


def check_for_XMAS(x, y, data):
    sides_to_check = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    mas_counter = 0
    for side in sides_to_check:
        if data[y + side[1]][x + side[0]] not in ['M', 'S']:
            return False
        if data[y + side[1]][x + side[0]] == 'M' and data[y - side[1]][x - side[0]] == 'S':
            mas_counter += 1
    print(mas_counter)
    if mas_counter < 2:
        return False
    return True


XMAS_counter = 0

for y in range(1, len(data) - 1):
    for x in range(1, len(data[0]) - 1):
        if data[y][x] == 'A':
            XMAS_counter += int(check_for_XMAS(x, y, data))

print(XMAS_counter)
