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


groups = []
for key, items in relations_dict.items():
    groups.append(items + [key])


current_longest_group = []
for group in groups:
    local_relations = {}
    for item in group:
        local_relations[item] = [dict_item for dict_item in relations_dict[item] if dict_item in group]
    local_groups = []
    for key, items in local_relations.items():
        local_groups.append([key] + items)
    for local_group1 in local_groups:
        group_is_valid = True
        for i in range(1, len(local_group1)):
            local_element = local_group1[i]
            local_group_without_local_element = local_group1[:i] + local_group1[i+1:]
            if not set(local_group_without_local_element).issubset(set(local_relations[local_element])):
                group_is_valid = False
                break
        if group_is_valid and len(local_group1) > len(current_longest_group):
            current_longest_group = local_group1


print(','.join(sorted(current_longest_group)))

