with open("input.txt") as file:
    data = file.read().splitlines()

lines = [row.split() for row in data]

set1 = [int(line[0]) for line in lines]
set2 = [int(line[1]) for line in lines]
set1.sort()
set2.sort()

result = 0
for i in range(len(set1)):
    result += abs(set1[i] - set2[i])

print(result)
