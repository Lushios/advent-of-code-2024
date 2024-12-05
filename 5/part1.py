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
            return 0

    return int(update[int((len(update) - 1) / 2)])


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

answer = 0
for update in updates:
    update_result = check_update(update)
    print(update_result)
    answer += update_result

print(answer)
