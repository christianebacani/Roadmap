# 148A - Insomnia cure

k = int(input().strip())
l = int(input().strip())
m = int(input().strip())
n = int(input().strip())
d = int(input().strip())

dragons = [num for num in range(1, d + 1)]
damaged_dragons = 0

for i in range(len(dragons)):
    if dragons[i] % k == 0:
        damaged_dragons += 1
        continue

    if dragons[i] % l == 0:
        damaged_dragons += 1
        continue

    if dragons[i] % m == 0:
        damaged_dragons += 1
        continue

    if dragons[i] % n == 0:
        damaged_dragons += 1

answer = damaged_dragons
print(answer)