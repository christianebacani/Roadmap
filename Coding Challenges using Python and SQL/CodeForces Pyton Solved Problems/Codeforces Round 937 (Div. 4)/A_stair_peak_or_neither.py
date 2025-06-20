# A - Stair, Peak, or Neither?

t = input().strip()

for _ in range(int(t)):
    user_input = input().strip().split()
    a = int(user_input[0])
    b = int(user_input[1])
    c = int(user_input[2])

    if a < b and b < c:
        print('STAIR')
        continue

    if a < b and b > c:
        print('PEAK')
    
    else:
        print('NONE')