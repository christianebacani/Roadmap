# 492A - Vanya and Cubes

n = int(input().strip())
copy_of_n = n
pyramid = []

while n > 0:
    if pyramid == []:
        pyramid.append([1])
        n -= 1
        continue

    last_digit = pyramid[-1][-1] + 1
    row = []

    for i in range(1, last_digit + 1):
        row.append(i)
        n -= i
    
    pyramid.append(row)

total = 0
maximum_height = 0

for i in range(len(pyramid)):
    total += sum(pyramid[i])

    if total <= copy_of_n:
        maximum_height += 1

print(maximum_height)