with open("input.txt") as file:
    data = file.read()

data = data.split(' ')

BLINKS = 25

print(data)

stones = {}


def add_to_stones(list_of_stones, stone, number):
    if stone in list_of_stones:
        list_of_stones[stone] += number
    else:
        list_of_stones[stone] = number
    return list_of_stones


def blink_stone(stone, number, stones_list):
    if stone == 0:
        stones_list = add_to_stones(stones_list, 1, number)
    elif len(str(stone)) % 2 == 0:
        stone1 = int(str(stone)[:len(str(stone)) // 2])
        stone2 = int(str(stone)[len(str(stone)) // 2:])
        stones_list = add_to_stones(stones_list, stone1, number)
        stones_list = add_to_stones(stones_list, stone2, number)
    else:
        stones_list = add_to_stones(stones_list, stone * 2024, number)
    return stones_list


for initial_stone in data:
    add_to_stones(stones, int(initial_stone), 1)

i = 0
while i < BLINKS:
    new_stones = {}
    for stone, number in stones.items():
        new_stones = blink_stone(stone, number, new_stones)
    stones = new_stones
    i += 1

print(sum([number for _, number in stones.items()]))
