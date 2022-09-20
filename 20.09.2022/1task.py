def print_rectangle(m, n):
    for i in range(m):
        for j in range(n):
            print('1', end='')
        print()

m = int(input())
n = int(input())
print_rectangle(m, n)