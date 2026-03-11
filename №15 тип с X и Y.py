for A in range(1, 10000):
    for x in range(1, 100):
        for y in range(1, 100):
            if ((x * y > A) or (x > y) or (74 > x)) == False:
                break
        if ((x * y > A) or (x > y) or (74 > x)) == False:
                break
    else:
        print(A)
