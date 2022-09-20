x = int(input(""))
n = int(input(""))

for i in range(n):
    if i == 0 or i == n - 1:
        for y in range(x):
            print('1', end=' ')
    else:
        print('1', end=' ')
        for y in range(1, x - 1):
            print(' ', end=' ')
        print('1', end=' ')
    print()
