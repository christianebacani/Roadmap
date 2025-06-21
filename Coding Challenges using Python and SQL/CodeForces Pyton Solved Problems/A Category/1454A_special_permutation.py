# 1454A - Special Permutation

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    permutation = []

    for i in range(1, n + 1):
        permutation.append(i)
    
    for i in range(len(permutation)):
        try:
            if i + 1 == permutation[i]:
                current_digit = permutation[i]
                next_digit = permutation[i + 1]
            
                permutation[i] = next_digit
                permutation[i + 1] = current_digit

        except IndexError:
            previous_digit = permutation[i - 1]
            current_digit = permutation[i]

            permutation[i - 1] = current_digit
            permutation[i] = previous_digit

    print(' '.join([str(num) for num in permutation]))