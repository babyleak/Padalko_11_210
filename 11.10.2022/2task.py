from random import randint

students = list(map(int(input().split())))
group_list = []
for group in range(1, 3):
    number_students = randint(*students)

print(max(group_list, key=lambda x: [1])[0])