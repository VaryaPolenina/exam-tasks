from itertools import*
count = 0
for i in permutations('ТАВРИЯ', r=5):
    word = ''.join(i)
    if word[0] != 'В' and 'ИЯ' not in word:
        count += 1
print(count)
