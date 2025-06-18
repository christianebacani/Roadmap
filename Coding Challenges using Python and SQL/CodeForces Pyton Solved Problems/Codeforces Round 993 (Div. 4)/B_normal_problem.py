# B - Normal Problem

t = int(input().strip())

for _ in range(t):
    a = input().strip()
    b = ''

    for i in range(len(a[::-1])):
        if a[::-1][i] == 'p':
            b += 'q'

        elif a[::-1][i] == 'q':
            b += 'p'

        else:
            b += 'w'

    print(b)