from operator import add, mul
from itertools import product


with open("input.txt") as file:
    data = file.read().splitlines()

operators = [add, mul]


def check_result(result, numbers):
    operator_combinations = product(operators, repeat=len(numbers) - 1)
    for combination in operator_combinations:
        current_sum = numbers[0]
        for i in range(len(combination)):
            current_sum = combination[i](current_sum, numbers[i + 1])
        if current_sum == result:
            return True
    return False


answer = 0
for line in data:
    result, numbers = line.split(': ')
    result = int(result)
    numbers = [int(x) for x in numbers.split()]
    if check_result(result, numbers):
        answer += result

print(answer)
