n = 2

cur = 2
sum = cur
for i in range(2, n + 1):
    cur *= 2
    sum += cur

print(sum)