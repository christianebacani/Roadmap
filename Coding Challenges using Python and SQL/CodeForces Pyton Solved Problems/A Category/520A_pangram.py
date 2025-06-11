# 520A - Pangram

n = int(input().strip())
letters = str(input().strip()).lower()
alphabets = 'abcdefghijklmnopqrstuvwxyz'

pangram = True

for i in range(len(alphabets)):
    if alphabets[i] not in letters:
        pangram = False
        break

if pangram:
    print('YES')

else:
    print('NO')