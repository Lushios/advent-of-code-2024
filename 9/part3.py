with open("input.txt") as file:
    data = file.read()

visual_data = []

for i, char in enumerate(data):
    if i % 2 == 0:
        visual_data.extend([str(int(i/2))] * int(char))
    else:
        visual_data.extend(['.'] * int(char))






result = 0
for i, char in enumerate(visual_data):
    if char == '.':
        break
    result += int(char) * i

print(result)
