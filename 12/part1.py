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


def get_region_perimeter(region):
    perimeter = 0
    all_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for point in region:
        region_neighbors = [
            (point[0] + direction[0], point[1] + direction[1])
            for direction in all_directions
            if (point[0] + direction[0], point[1] + direction[1]) in region
        ]
        perimeter += 4 - len(region_neighbors)
    return perimeter


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
    answer += get_region_area(region['region']) * get_region_perimeter(region['region'])

print(answer)
