# 1722A - Spell Check

t = int(input().strip())
name = 'Timur'

for _ in range(t):
    n = int(input().strip())
    s = input().strip()

    if sorted(name) == sorted(s):
        print('YES')

    else:
        print('NO')