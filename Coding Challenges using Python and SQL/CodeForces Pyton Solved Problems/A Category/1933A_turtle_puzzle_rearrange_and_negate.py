# 1933A - Turtle Puzzle: Rearrange and Negate

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = input().strip().split()
    a = [int(num) for num in a]

    a = sorted(a)
    maximum_length = 0

    for i in range(1, len(a) + 1):
        for j in range(len(a)):
            segment = a[j : j + i]

            if len(segment) != i:
                continue

            if max(segment) >= 0:
                continue
            
            if len(segment) > maximum_length:
                maximum_length = len(segment)
    
    for i in range(1, len(a) + 1):
        the_operation_was_performed = False

        for j in range(len(a)):
            segment = a[j : j + i]

            if len(segment) != i:
                continue

            if max(segment) >= 0:
                continue
            
            if len(segment) != maximum_length:
                continue

            for k in range(len(segment)):
                segment[k] = segment[k] * -1
            
            a = a[:j] + segment + a[j + i:]
            the_operation_was_performed = True
            break

        if the_operation_was_performed:
            break

    print(sum(a))