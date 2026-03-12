from itertools import*
numb = 1
for i in product('ACDNY', repeat=4):
    if ''.join(i) == 'ANDY':
        print(numb, ''.join(i))
    numb += 1

