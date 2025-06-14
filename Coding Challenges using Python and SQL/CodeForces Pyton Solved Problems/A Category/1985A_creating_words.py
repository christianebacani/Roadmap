# 1985A - Creating Words

t = int(input().strip())

for _ in range(t):
    words = input().strip().split()
    a = words[0]
    b = words[1]

    first_letter_of_a = a[0]
    first_letter_of_b = b[0]

    a = first_letter_of_b + a[1:]
    b = first_letter_of_a + b[1:]

    print(f'{a} {b}')