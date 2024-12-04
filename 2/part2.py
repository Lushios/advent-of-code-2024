with open("input.txt") as file:
    data = file.read().splitlines()


def is_line_safe(line, allow_recursion=True):
    diff = 0
    for i in range(len(line) - 1):
        new_diff = int(line[i + 1]) - int(line[i])
        if abs(new_diff) not in range(1, 4):
            if allow_recursion:
                candidates_for_removal = [x for x in [i-1, i, i+1, i+2] if 0 <= x < len(line)]
                result = False
                for candidate in candidates_for_removal:
                    result |= is_line_safe(line[:candidate] + line[candidate+1:], False)
                return result
            else:
                return False
        elif new_diff * diff < 0:
            if allow_recursion:
                candidates_for_removal = [x for x in [i-1, i, i+1, i+2] if 0 <= x < len(line)]
                result = False
                for candidate in candidates_for_removal:
                    result |= is_line_safe(line[:candidate] + line[candidate+1:], False)
                return result
            else:
                return False
        diff = new_diff
    return True


lines = [row.split() for row in data]
results = [is_line_safe(line) for line in lines]
answer = len([result for result in results if result])

print(answer)
