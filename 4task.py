s = u"Сегодня прошла первая пара по программированию. Мы провели время с пользой."

statis = {}
for ch in s:
    if ch in statis:
        statis[ch] += 1
    else:
        statis[ch] = 1

letters = stat.keys()
letters.sort()
for ch in letters:
    print ch, ":", stat[ch]    