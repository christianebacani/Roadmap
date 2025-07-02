# A - Lucky?

t = int(input().strip())

for _ in range(t):
    ticket = input().strip()
    
    first_three_digits = list(ticket[:3])
    first_three_digits = [int(digit) for digit in first_three_digits]

    last_three_digits = list(ticket[3:])
    last_three_digits = [int(digit) for digit in last_three_digits]

    if sum(first_three_digits) == sum(last_three_digits):
        print('YES')
    
    else:
        print('NO')