from random import randint

x = []
for a in range(10):
    x.append(randint(1, 50))
x.sort()
print(x)

value = int(input())

mid = len(x) // 2
low = 0
high = len(x) - 1

while x[mid] != value and low <= high:
    if value > x[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("Not value")
else:
    print("ID =", mid)