from random import randint
N=randint(0,9)
K = int(input("целое число от 0 до 9"))
while K != N:
    K = int(input("повторите попытку"))
    if K < N:
        print("число меньше")
    elif K > N:
        print("число больше")
    else:
        print("q")
print(K)
print(N)