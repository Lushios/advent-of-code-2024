with open("input.txt") as file:
    data = file.read().splitlines()

pairs = [row.split('-') for row in data]

relations_dict = {}

for comp1, comp2 in pairs:
    if comp1 not in relations_dict:
        relations_dict[comp1] = [comp2]
    else:
        relations_dict[comp1].append(comp2)

    if comp2 not in relations_dict:
        relations_dict[comp2] = [comp1]
    else:
        relations_dict[comp2].append(comp1)


answers = set()
for key1, values_list in relations_dict.items():
    for value1 in values_list:
        for value2 in relations_dict[value1]:
            for value3 in relations_dict[value2]:
                if value3 == key1:
                    answers.add(tuple(sorted((key1, value1, value2))))


print(len(answers))
print(len(list(filter(lambda x: 't' in [x[0][0], x[1][0], x[2][0]], answers))))
