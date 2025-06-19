# 935A - Fafa and his Company

n = int(input().strip())
count = 0

for i in range(n + 1):
    team_leaders = i
    employees = n - i

    if team_leaders == 0 or employees == 0:
        continue

    if employees % team_leaders == 0:
        count += 1

print(count)