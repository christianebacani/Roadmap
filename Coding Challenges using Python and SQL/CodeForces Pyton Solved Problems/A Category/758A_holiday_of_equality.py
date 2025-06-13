# 758A - Holiday Of Equality

n = input()
burles = [int(burle) for burle in input().strip().split()]
equalized_burles = []

for _ in range(len(burles)):
    equalized_burles.append(max(burles))

total = 0

for i in range(len(equalized_burles)):
    total += abs(equalized_burles[i] - burles[i])

answer = total
print(answer)