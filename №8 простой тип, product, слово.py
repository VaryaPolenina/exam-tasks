from itertools import*
numb = 1
for i in product('AEY', repeat=5):
    if numb == 50:
        print(numb, ''.join(i))
    numb += 1
