# MULTI DIMENSIONALITY OF ARRAY @ NESTED LIST
my_nested_list = [
    ["A", "B", "C"],
    [1, 2, 3],
    ["a", "b", "c"],
    "Hafizi",
    1990,
    [100, [100.1, 100.2, 100.3]]
]

# access
print(my_nested_list[5][1][2])
print(my_nested_list[3])
print(my_nested_list[-1][-1][-1])

# replacing
my_nested_list[5][1][2] = 100.5
print(my_nested_list)

my_nested_list.append("Nur")
print(my_nested_list)

# add item on last index of specific dimension
my_nested_list[5][1].append(100.6)
print(my_nested_list)

# insert item by index
my_nested_list[5][1].insert(2, 100.3)
print(my_nested_list)

print(len(my_nested_list[5][1]))

new_nested_list = [
    [5, 6, 7],
    [15, 16, 17],
    [25, 26, 27]
]

for x in new_nested_list:
    for y in x:
        print(y)