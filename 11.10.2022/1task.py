message = "this so cool"
cnt = 1
for i in message:
    if i == message[1:-1]:
        cnt += 1
        print(i, end='')
    else:
        print(i, end='')
        print(cnt, end='')
        cnt = 1