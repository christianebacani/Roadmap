# A - Lever

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = input().strip().split()
    a = [int(num) for num in a]
    b = input().strip().split()
    b = [int(num) for num in b]
    
    total_iteration = 0

    while True:
        first_step_was_ignored = True

        for i in range(n):
            if a[i] > b[i]:
                a[i] = a[i] - 1
                first_step_was_ignored = False
                break

        for i in range(n):
            if a[i] < b[i]:
                a[i] = a[i] + 1

        total_iteration += 1

        if first_step_was_ignored:
            break
    
    print(total_iteration)