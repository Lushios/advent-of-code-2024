with open("input.txt") as file:
    data = file.read()

data = data.split('\n\n')
PIN_SIZE = len(data[0].splitlines())
NUMBER_OF_PINS = len(data[0].splitlines()[0])

locks = []
keys = []
for element in data:
    element = element.splitlines()
    sizes = {}
    for i in range(NUMBER_OF_PINS):
        column = [line[i] for line in element]
        sizes[i] = len([el for el in column if el == '#'])
    if all(el == '#' for el in element[0]):
        locks.append(sizes)
    else:
        keys.append(sizes)

fit = 0
for lock in locks:
    for key in keys:
        if all([lock[i] + key[i] <= PIN_SIZE for i in range(NUMBER_OF_PINS)]):
            fit += 1
print(fit)
