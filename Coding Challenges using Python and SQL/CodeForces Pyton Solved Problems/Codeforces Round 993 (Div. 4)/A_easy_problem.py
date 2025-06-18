# 2044A - Easy Problem

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    maximum_number_to_consider = n * 2
    count = 0

    for a in range(1, maximum_number_to_consider + 1):
        for b in range(1, maximum_number_to_consider + 1):
            if (n - b) == a:
                count += 1

    print(count)