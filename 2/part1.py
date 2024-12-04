with open("input.txt") as file:
    data = file.read().splitlines()


def is_line_safe(line):
    diff = 0
    for i in range(len(line) - 1):
        new_diff = int(line[i + 1]) - int(line[i])
        if abs(new_diff) not in range(1, 4):
            return False
        if new_diff * diff < 0:
            return False
        # if abs(new_diff - diff) > abs(new_diff):
        #     return False
        diff = new_diff
    return True


lines = [row.split() for row in data]
results = [is_line_safe(line) for line in lines]
answer = len([result for result in results if result])

print(answer)
