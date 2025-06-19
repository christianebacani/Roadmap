# 1807A - Plus or Minus

t = int(input().strip())

for _ in range(t):
    user_input = input().strip().split()
    a = int(user_input[0])
    b = int(user_input[1])
    c = int(user_input[2])
    
    if a + b == c:
        print('+')
    
    else:
        print('-')