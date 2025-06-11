# 41A - Translation

s = input().strip()
t = input().strip()

if t[::-1] == s:
    print('YES')

else:
    print('NO')