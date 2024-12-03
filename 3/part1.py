import re
from functools import reduce

with open("input.txt") as file:
    data = file.read()

pattern = r"mul\(\d+,\d+\)"

matches = [match[4:-1].split(',') for match in re.findall(pattern, data)]

result = reduce(lambda acc, match: acc + int(match[0]) * int(match[1]), matches, 0)

print(result)
