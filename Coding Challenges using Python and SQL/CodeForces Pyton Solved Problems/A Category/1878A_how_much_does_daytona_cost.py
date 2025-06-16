# 1878A - How Much Does Daytona Cost?

t = int(input().strip())

for _ in range(t):
    user_input = input().strip().split()

    n = int(user_input[0])
    k = int(user_input[1])

    a = input().strip().split()
    a = [int(num) for num in a]

    if k in a:
        print('YES')
    
    else:
        print('NO')