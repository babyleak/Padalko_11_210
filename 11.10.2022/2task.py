import random

names = ["Мансур", "Алим", "Изида", "Георгий", "Даниил", "Данила", "Элина", "Диана", "Ильназ", "Фарида", "Роман", "Юлия",
         "Тихон", "Данила", "Рамис"]

students = 20
groups = 3

students_list =[]

for x in range(groups):
    this_group = []
    for i in range(students):
        this_name = random.choice(names)
        this_group.append(this_name)
    students_list.append(this_group)
    print(this_group)

set_names = []
set_groups = []
print("set:")
for this_group in students_list:
    this_set = set(this_group)
    set_groups.append(this_set)
    print(this_set)

print("setnames")

set_names = set_groups[0].intersection(set_groups[1], set_groups[2])
print(set_names)

print("unique")
unique_names = set_groups[0].symmetric_difference(set_groups[1]).symmetric_difference(set_groups[2])
print(unique_names)