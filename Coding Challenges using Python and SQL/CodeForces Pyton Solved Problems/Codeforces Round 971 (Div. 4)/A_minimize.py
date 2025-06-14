# 2009A - Minimize!

t = int(input().strip())

for _ in range(t):
    user_input = input().strip().split()
    a = int(user_input[0])
    b = int(user_input[1])
    possible_values = []

    for c in range(a, b + 1):
        possible_values.append((c - a) + (b - c))
    
    print(min(possible_values, default=0))