# 1742A - Sum

t = int(input().strip())

for _ in range(t):
    user_input = input().strip().split()
    a = int(user_input[0])
    b = int(user_input[1])
    c = int(user_input[2])

    if a + b == c:
        print('YES')
        continue

    if a + c == b:
        print('YES')
        continue

    if b + c == a:
        print('YES')
        continue

    print('NO')