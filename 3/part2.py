import re

with open("input.txt") as file:
    data = file.read()

pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"

matches = re.findall(pattern, data)

result = 0
do = True

for match in matches:
    match match:  # this naming is horrible, but funny, so yeah
        case "do()":
            do = True
        case "don't()":
            do = False
        case _:
            if do:
                match = match[4:-1].split(',')
                result += int(match[0]) * int(match[1])


print(result)
