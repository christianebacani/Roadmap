# 999A - Mishka and Contest

first_line = input().strip().split()

n = int(first_line[0])
k = int(first_line[1])
a = input().strip().split()
a = [int(num) for num in a]
total = 0

while True:
    if len(a) == 0:
        break

    if a[0] > k and a[-1] > k:
        break
    
    if a[0] <= k:
        total += 1
        a = a[1:]

    else:
        total += 1
        a = a[:-1]

print(total)        