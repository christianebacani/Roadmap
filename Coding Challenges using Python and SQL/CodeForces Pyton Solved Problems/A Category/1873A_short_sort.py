# 1873A - Short Sort

t = int(input().strip())

for i in range(t):
    cards = input().strip()
    a = cards[0]
    b = cards[1]
    c = cards[2]

    if a + b + c == 'abc':
        print('YES')
        continue

    if b + a + c == 'abc':
        print('YES')
        continue

    if a + c + b == 'abc':
        print('YES')
        continue

    if c + b + a == 'abc':
        print('YES')
        continue

    print('NO')