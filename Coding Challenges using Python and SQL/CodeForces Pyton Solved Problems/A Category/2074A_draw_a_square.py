# 2074A - Draw a Square

t = int(input().strip())

for _ in range(t):
    points = input().strip().split()
    points = [int(num) for num in points]

    if len(set(points)) == 1:
        print('Yes')

    else:
        print('No')