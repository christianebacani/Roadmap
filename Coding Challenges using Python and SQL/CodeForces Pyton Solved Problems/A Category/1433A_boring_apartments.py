# 1433A - Boring Apartments

boring_numbers = []

for i in range(1, 10):
    for j in range(1, 6):
        digit = str(i) * j
        
        if int(digit) > 10000:
            continue
        
        if int(digit) < 1:
            continue

        boring_numbers.append(digit)

t = int(input().strip())

for _ in range(t):
    x = input().strip()
    target_index = boring_numbers.index(x)
    list_of_aparments_he_called = boring_numbers[:target_index + 1]
    total = 0

    for i in range(len(list_of_aparments_he_called)):
        total += len(list_of_aparments_he_called[i])

    print(total)