# 581A - Vasya the Hipster

user_input = input().strip().split()
a = int(user_input[0])
b = int(user_input[1])

different_pair_of_socks = 0
same_pair_of_socks = 0

while True:
    if a > 0 and b > 0:
        a -= 1
        b -= 1
        different_pair_of_socks += 1
    
    else:
        break

while True:
    if a >= 2:
        a -= 2
        same_pair_of_socks += 1
    
    elif b >= 2:
        b -= 2
        same_pair_of_socks += 1
    
    else:
        break

print(f'{different_pair_of_socks} {same_pair_of_socks}')