# 1759A - Yes-Yes?

t = int(input().strip())

answer = 'Yes' * 50

for _ in range(t):
    s = input().strip()

    if s in answer:
        print('YES')
    
    else:
        print('NO')