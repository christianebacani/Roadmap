# 214A - System of Equations

test_input = input().strip().split()
n = int(test_input[0])
m = int(test_input[1])
pairs = 0

for a in range(max([n, m]) + 1):
    for b in range(max([n, m]) + 1):
        if (a ** 2) + b != n:
            continue

        if a + (b ** 2) != m:
            continue
        
        pairs += 1

print(pairs)