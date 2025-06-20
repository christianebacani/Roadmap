# 1462A - Favorite Sequence

t = int(input().strip())

for _ in range(t):
    n = input()
    a = input().strip().split()
    a = [int(num) for num in a]

    move = 0
    total_moves = len(a)

    original_sequence = []

    while move < total_moves:
        if move % 2 == 0:
            original_sequence.append(str(a[0]))
            a = a[1:]

        else:
            original_sequence.append(str(a[-1]))
            a = a[:-1]

        move += 1

    print(' '.join(original_sequence))