from functools import lru_cache

with open("input.txt") as file:
    data = file.read()

towels, combinations = data.split("\n\n")

towels = towels.split(', ')

combinations = combinations.split('\n')


@lru_cache
def solve_combination(combination):
    if combination == '':
        return 1
    answer = 0
    for towel in towels:
        if combination.startswith(towel):
            answer += solve_combination(combination[len(towel):])
    return answer


answer = 0
for combination in combinations:
    answer += solve_combination(combination)


print(answer)
