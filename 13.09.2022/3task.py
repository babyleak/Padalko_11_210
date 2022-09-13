def func(x, y, n):
    return x * x + y * y <= n * n

if __name__ == '__main__':
    x = float(input())
    y = float(input())
    n = float(input())
    func(x, y, n)
    if func(x, y, n):
        print('yes')
    else:
        print('no')