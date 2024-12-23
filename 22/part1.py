with open("input.txt") as file:
    data = file.read().splitlines()

brr = 2000


def calculate_secret_number(secret_number):
    secret_number = (secret_number ^ (secret_number * 64)) % 16777216
    secret_number = (secret_number ^ (secret_number // 32)) % 16777216
    return (secret_number ^ (secret_number * 2048)) % 16777216


all_secret_numbers = []
for number in data:
    new_number = int(number)
    for _ in range(brr):
        new_number = calculate_secret_number(new_number)
    all_secret_numbers.append(new_number)

print(sum(all_secret_numbers))

