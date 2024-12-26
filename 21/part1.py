with open("input.txt") as file:
    data = file.read().splitlines()

numpad_coordinates = {
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '0': (1, 3),
    'A': (2, 3),
}

arrows_coordinates = {
    '^': (1, 0),
    'A': (2, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1),
}


def numpad_into_arrows(code):
    x, y = numpad_coordinates['A']
    arrows = []
    for button in code:
        button_x, button_y = numpad_coordinates[button]
        dx, dy = button_x - x, button_y - y
        if dx < 0:
            if button_x == 0 and y == 3:
                arrows.extend(['^' for _ in range(-dy)])
                arrows.extend(['<' for _ in range(-dx)])
                arrows.append('A')
                x, y = button_x, button_y
                continue
            arrows.extend(['<' for _ in range(-dx)])
        if dy > 0:
            if button_y == 3 and x == 0:
                arrows.extend(['>' for _ in range(dx)])
                arrows.extend(['v' for _ in range(dy)])
                arrows.append('A')
                x, y = button_x, button_y
                continue
            arrows.extend(['v' for _ in range(dy)])
        if dy < 0:
            arrows.extend(['^' for _ in range(-dy)])
        if dx > 0:
            arrows.extend(['>' for _ in range(dx)])
        arrows.append('A')
        x, y = button_x, button_y
    # print(''.join(arrows))
    return arrows


def arrows_into_arrows(code):
    x, y = arrows_coordinates['A']
    arrows = []
    for arrow in code:
        arrow_x, arrow_y = arrows_coordinates[arrow]
        dx, dy = arrow_x - x, arrow_y - y
        if dx < 0:
            if arrow_x == 0 and y == 0:
                arrows.extend(['v' for _ in range(dy)])
                arrows.extend(['<' for _ in range(-dx)])
                arrows.append('A')
                x, y = arrow_x, arrow_y
                continue
            arrows.extend(['<' for _ in range(-dx)])
        if dy > 0:
            arrows.extend(['v' for _ in range(dy)])
        if dx > 0:
            arrows.extend(['>' for _ in range(dx)])
        if dy < 0:
            arrows.extend(['^' for _ in range(-dy)])
        arrows.append('A')
        x, y = arrow_x, arrow_y
    # print(''.join(arrows))
    return arrows


result = 0
for code in data:
    final_input = ''.join(arrows_into_arrows(arrows_into_arrows(numpad_into_arrows(code))))
    # print(arrows_into_arrows(arrows_into_arrows(['^', '>'])))
    # print(len(arrows_into_arrows(arrows_into_arrows(['^', '>']))))

    print(len(final_input), int(code[:3]))
    result += len(final_input) * int(code[:3])
print(result)
