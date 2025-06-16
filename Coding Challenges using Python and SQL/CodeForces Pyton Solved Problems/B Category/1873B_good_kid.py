# 1873B - Good Kid

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = input().strip().split()
    a = [int(num) for num in a]
    
    minimum_number = min(a)

    for i in range(len(a)):
        if a[i] == minimum_number:
            a[i] = a[i] + 1
            break
    
    total_product = 1

    for i in range(len(a)):
        total_product *= a[i]
    
    print(total_product)