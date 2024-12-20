with open("input.txt") as file:
    data = file.read()

towels, combinations = data.split("\n\n")

towels = towels.split(', ')

combinations = combinations.split('\n')


def solve_combination(combination, towels, current_towel_set=None):
    print(f"Combination: {combination}")
    if current_towel_set is None:
        current_towel_set = []
    possible_towels = [towel for towel in towels if combination.startswith(towel)]
    for towel in possible_towels:
        new_towel_set = current_towel_set + [towel]
        if combination == towel:
            return True
        else:
            solutions = solve_combination(combination[len(towel):], towels, new_towel_set)
            if solutions:
                return True
    return False

answer = 0
for combination in combinations:
    print(combination)
    towel_sets = solve_combination(combination, towels)
    if towel_sets:
        answer += 1

print(answer)
