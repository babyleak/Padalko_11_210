array = []

def fnd(n1, n2, n3):
    return pow(n1, n2, n3)

for x in range(int(input())):
    a = list(map(int, input().split()))
    array.append(fnd(a[1], a[0] - 2, a[0]))

print(array, sep = "\n")