import math

def f1(x):
    return x + 1

def f2(x):
    return -x + 1

def c(x, r=1):
    return -math.sqrt(r**2 - x**2)

x = float(input("enter x:"))
y = float(input("enter y:"))

if y <= f1(x) and y <= f2(x) and y >= c(x):
    print("hit")
else:
    print("missed")