with open("input.txt") as file:
    data = file.read().splitlines()


def get_possible_directions(x, y):
    directions_to_check = []
    if x > 0:
        directions_to_check.append((-1, 0))
    if x < len(data[0]) - 1:
        directions_to_check.append((1, 0))
    if y > 0:
        directions_to_check.append((0, -1))
    if y < len(data) - 1:
        directions_to_check.append((0, 1))

    return directions_to_check


def find_region(x, y, data):
    points_to_check = [(x, y)]
    range = [(x, y)]
    range_value = data[y][x]
    while points_to_check:
        pointx, pointy = points_to_check.pop()
        directions_to_check = get_possible_directions(pointx, pointy)
        for direction in directions_to_check:
            newx = pointx + direction[0]
            newy = pointy + direction[1]
            if data[newy][newx] == range_value and (newx, newy) not in range:
                range.append((newx, newy))
                points_to_check.append((newx, newy))
    return range, range_value


def get_region_area(region):
    return len(region)


def get_region_number_of_sides(region, region_value):
    # the idea is to go through all the vertical and horizontal lines and count the amount of times sides on those lines

    vertical_sides = 0

    minx = min(region, key=lambda point: point[0])[0]
    miny = min(region, key=lambda point: point[1])[1]

    for x in range(minx, len(data[0])):
        wall = False
        filtered_region = sorted(list(filter(lambda point: point[0] == x, region)), key=lambda point: point[1])
        if not filtered_region:
            continue

        if x == minx:
            for y in range(len(data)):
                if (x, y) in region:
                    if not wall:
                        vertical_sides += 1
                    wall = True
                else:
                    wall = False

        left_wall = False
        right_wall = False

        for y in range(len(data)):
            if (x, y) in region and (x + 1, y) not in region:
                if not right_wall:
                    vertical_sides += 1
                right_wall = True
                left_wall = False
            elif (x, y) not in region and (x + 1, y) in region:
                if not left_wall:  # this is the right wall? they are all right, wtf???
                    vertical_sides += 1
                left_wall = True
                right_wall = False
            else:
                left_wall = False
                right_wall = False
            # if ((x, y) in region and (x + 1, y) not in region) or ((x, y) not in region and (x + 1, y) in region):
            #     pass
            #     if not wall:
            #         vertical_sides += 1
            #     wall = True
            # else:
            #     wall = False

    horizontal_sides = 0

    for y in range(miny, len(data)):
        wall = False
        filtered_region = sorted(list(filter(lambda point: point[1] == y, region)), key=lambda point: point[0])
        if not filtered_region:
            continue

        if y == miny:
            for x in range(len(data[0])):
                if (x, y) in region:
                    if not wall:
                        horizontal_sides += 1
                    wall = True
                else:
                    wall = False

        top_wall = False
        bottom_wall = False

        for x in range(len(data[0])):
            if (x, y) in region and (x, y + 1) not in region:
                if not bottom_wall:
                    horizontal_sides += 1
                bottom_wall = True
                top_wall = False
            elif (x, y) not in region and (x, y + 1) in region:
                if not top_wall:
                    horizontal_sides += 1
                top_wall = True
                bottom_wall = False
            else:
                top_wall = False
                bottom_wall = False

            # if ((x, y) in region and (x, y + 1) not in region) or ((x, y) not in region and (x, y + 1) in region):
            #     if not wall:
            #         horizontal_sides += 1
            #     wall = True
            # else:
            #     wall = False

    return vertical_sides + horizontal_sides


regions = []
sorted_data_entries = set()


while len(sorted_data_entries) < len(data) * len(data[0]):
    for y in range(len(data)):
        for x in range(len(data[y])):
            if (x, y) not in sorted_data_entries:
                new_region, new_region_value = find_region(x, y, data)
                for point in new_region:
                    sorted_data_entries.add(point)
                regions.append({'region': new_region, 'value': new_region_value})


answer = 0
for region in regions:
    print(region['value'], get_region_number_of_sides(region['region'], region['value']))
    answer += get_region_area(region['region']) * get_region_number_of_sides(region['region'], region['value'])

print(answer)
