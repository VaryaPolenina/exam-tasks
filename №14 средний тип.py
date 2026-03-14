for x in range(1, 2070):
    s = 7**230 + 7**130 + 7**30 - x
    count = 0
    while s > 0:
        if s % 7 == 0:
            count += 1
        s = s // 7
    if count == 199:
        print(x)
