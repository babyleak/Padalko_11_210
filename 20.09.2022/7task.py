res = 0
res_old = None
while True:
    res_old = res
    res += 1
    if abs(res_old - res) < 0.001:
        break
