# 1850A - To My Critics

t = int(input().strip())

for _ in range(t):
    user_input = input().strip().split()
    a = int(user_input[0])
    b = int(user_input[1])
    c = int(user_input[2])

    if a + b >= 10 or b + c >= 10 or a + c >= 10:
        print('YES')

    else:
        print('NO')