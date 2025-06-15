# 80A - panoramix prediction

user_input = input().strip().split()
n = int(user_input[0])
m = int(user_input[1])

while True:
    number_is_prime = True
    n += 1

    for i in range(2, n):
        if n % i == 0:
            number_is_prime = False
            break
    
    if number_is_prime:
        break

if n == m:
    print('YES')

else:
    print('NO')