from math import inf

with open("input.txt") as file:
    data = file.read()


def validate_page(page, pages_before_current):
    if page not in rules:
        return True
    for page_before_current in pages_before_current:
        if page_before_current in rules[page]:
            return False
    return True


def check_update(update):
    for i, page in enumerate(update):
        page_valid = validate_page(page, update[:i])
        if not page_valid:
            return True

    return False


def fix_update(update):
    update = list(update)
    for i in range(len(update)):
        if update[i] not in rules:
            continue
        earliest_violation = inf
        for j in range(len(update[:i])):
            if update[j] in rules[update[i]] and j < earliest_violation:
                earliest_violation = j
        if earliest_violation != inf:
            update.insert(earliest_violation, update.pop(i))
    return update


text_rules, updates = data.split('\n\n')
text_rules = text_rules.splitlines()

rules = {}

for rule in text_rules:
    pagea, pageb = rule.split('|')
    if pagea in rules:
        rules[pagea].append(pageb)
    else:
        rules[pagea] = [pageb]

updates = [update.split(',') for update in updates.splitlines()]

wrong_updates = [update for update in updates if check_update(update)]

fixed_updates = [fix_update(update) for update in wrong_updates]
answer = sum([int(update[int((len(update) - 1) / 2)]) for update in fixed_updates])

print(answer)
