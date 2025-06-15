# 1829A - Love Story

t = int(input().strip())
codeforces_string = 'codeforces'

for _ in range(t):
    s = input().strip()
    total = 0

    for i in range(len(s)):
        if s[i] != codeforces_string[i]:
            total += 1

    print(total)            