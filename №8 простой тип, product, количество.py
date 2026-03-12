from itertools import*
count = 0
for i in product('АБКЛН', repeat=6):
    word = ''.join(i)
    if word[0] == 'К' and word.count('Н') == 2:
        count += 1
print(count)
