# 1619A - Square String?

t = int(input().strip())

for _ in range(t):
    s = input().strip()

    if len(s) % 2 != 0:
        print('NO')
        continue

    index_delimiter = len(s) // 2
    first_part = s[:index_delimiter]
    second_part = s[index_delimiter:]

    if first_part == second_part:
        print('YES')
    
    else:
        print('NO')