with open("input.txt") as file:
    data = file.read()

visual_data = []

for i, char in enumerate(data):
    if i % 2 == 0:
        visual_data.append({'element': int(i/2), 'length': int(char)})
    else:
        visual_data.append({'element': '.', 'length': int(char)})


blocks_to_add = []

for i in range(len(visual_data) - 1, -1, -2):
    print(i)
    block_length = visual_data[i]['length']
    block_element = visual_data[i]['element']
    for j in range(i):
        if visual_data[j]['element'] != '.' or visual_data[j]['length'] < block_length:
            continue
        else:
            visual_data[j]['length'] -= block_length
            visual_data[i]['element'] = '.'
            blocks_to_add.append({'element': block_element, 'length': block_length, 'location': j})
            break


blocks_to_add = sorted(blocks_to_add, key=lambda x: x['location'])

for i, block in enumerate(blocks_to_add):
    visual_data.insert(block['location'] + i, block)

resulting_data = []
for block in visual_data:
    resulting_data.extend([str(block['element'])] * block['length'])

print(resulting_data)

result = 0
for i, char in enumerate(resulting_data):
    if char == '.':
        continue
    result += int(char) * i

print(result)
