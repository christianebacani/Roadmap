# 2000A - Primary Task

t = int(input().strip())

for _ in range(t):
    a = input().strip()

    if not a.startswith('10'):
        print('NO')
        continue

    if len(a) <= 2:
        print('NO')
        continue

    a = a[2:]

    if a[0] == '0':
        print('NO')
        continue

    if int(a) >= 2:
        print('YES')
    
    else:
        print('NO')