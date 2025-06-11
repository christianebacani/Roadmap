# 1692A - Marathon

t = int(input().strip())

for _ in range(t):
    distinct_integers = input().strip().split()
    a = int(distinct_integers[0])
    b = int(distinct_integers[1])
    c = int(distinct_integers[2])
    d = int(distinct_integers[3])

    count = 0

    if a < b:
        count += 1
    
    if a < c:
        count += 1
    
    if a < d:
        count += 1
    
    print(count)