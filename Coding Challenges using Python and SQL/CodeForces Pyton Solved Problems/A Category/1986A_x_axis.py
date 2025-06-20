# 1986A - X Axis

t = int(input().strip())

for _ in range(t):
    coordinates = input().strip().split()
    coordinates = [int(coordinate) for coordinate in coordinates]

    values = []

    for i in range(1, 11):
        total = 0

        for j in range(len(coordinates)):
            total += abs(coordinates[j] - i)

        values.append(total)
    
    print(min(values))