n = int(input(""))

f = 1
summ = 0

for i in range(2, n+1):
    for j in range(1, i+1):
        f = f * j
    summ += f
print("", summ)