from itertools import product

with open("input.txt") as file:
    data = file.read().splitlines()

brr = 2000

diff_ranges = list(range(-9, 10))
comb = list(product(diff_ranges, repeat=4))
useful_combs = list(
    filter(
        lambda x: (sum(x) > 0)
                  and (abs(sum(x[0:3])) < 10)
                  and (abs(sum(x[0:2])) < 10)
                  and (abs(sum(x[1:3])) < 10)
                  and (abs(sum(x[1:4])) < 10)
                  and (abs(sum(x[2:4])) < 10)
        , comb)
)


def calculate_secret_number(secret_number):
    secret_number = (secret_number ^ (secret_number * 64)) % 16777216
    secret_number = (secret_number ^ (secret_number // 32)) % 16777216
    return (secret_number ^ (secret_number * 2048)) % 16777216


all_secret_numbers = []
for number in data:
    new_number = int(number)
    secret_numbers_sequence = [new_number]
    for _ in range(brr):
        new_number = calculate_secret_number(new_number)
        secret_numbers_sequence.append(new_number)
    all_secret_numbers.append(secret_numbers_sequence)

prices_n_diffs = []
for sequence in all_secret_numbers:
    prices_n_diffs.append([(int(str(sequence[i + 1])[-1]), int(str(sequence[i + 1])[-1]) - int(str(sequence[i])[-1])) for i in range(len(sequence) - 1)])


result = 0
win = None

for num, useful_comb in enumerate(useful_combs):
    print(len(useful_combs) - num)
    combo_counter = 0
    for price_n_diff in prices_n_diffs:
        for i in range(3, len(price_n_diff)):
            if (price_n_diff[i][1] == useful_comb[3]) and (price_n_diff[i-1][1] == useful_comb[2]) and (price_n_diff[i - 2][1] == useful_comb[1]) and (price_n_diff[i - 3][1] == useful_comb[0]):
                combo_counter += price_n_diff[i][0]
                break
    if result < combo_counter:
        result = combo_counter
        win = useful_comb


print(result)
print(win)
