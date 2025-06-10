# 723A - The New Year: Meeting Friends

points = input().strip().split()
points = [int(num) for num in points]
points.sort()
differences = []

for i in range(len(points)):
    total_difference = 0

    for j in range(len(points)):
        if i != j:
            total_difference += abs(points[i] - points[j])

    differences.append(total_difference)

print(min(differences))