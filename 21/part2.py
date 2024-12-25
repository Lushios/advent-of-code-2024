with open("input.txt") as file:
    data = file.read().splitlines()

lines = [row.split() for row in data]

set1 = [int(line[0]) for line in lines]
set2 = [int(line[1]) for line in lines]

result = 0
for i in range(len(set1)):
    result += set1[i] * len([1 for element in set2 if element == set1[i]])

print(result)
