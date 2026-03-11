def task(start, end):
    if start < end:
        return 0
    if start == end:
        return 1
    return task(start - 1, end) + task(start//2, end)
print(task(89, 30) * task(30, 7))
