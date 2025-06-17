# 1772A - A+B?

t = int(input().strip())

for _ in range(t):
    expression = input().strip().split('+')
    first_digit = int(expression[0])
    second_digit = int(expression[1])

    print(first_digit + second_digit)