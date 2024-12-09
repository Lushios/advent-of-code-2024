with open("input.txt") as file:
    data = file.read()

visual_data = []

for i, char in enumerate(data):
    if i % 2 == 0:
        visual_data.extend([str(int(i/2))] * int(char))
    else:
        visual_data.extend(['.'] * int(char))

dot_locations = [i for i, el in enumerate(visual_data) if el == '.']


i = -1

for dot_location in dot_locations:
    print(dot_location)
    while True:
        if visual_data[i] != '.':
            break
        i -= 1
    if len(visual_data) + i < dot_location:
        break
    visual_data[dot_location], visual_data[i] = visual_data[i], visual_data[dot_location]


# wrote two algos because why the fuck not

# for dot_location in dot_locations:
#     if dot_location > len(visual_data):
#         break
#     element = visual_data.pop()
#     if element == '.':
#         while element == '.':
#             element = visual_data.pop()
#     visual_data[dot_location] = element


result = 0
for i, char in enumerate(visual_data):
    if char == '.':
        break
    result += int(char) * i

print(result)
