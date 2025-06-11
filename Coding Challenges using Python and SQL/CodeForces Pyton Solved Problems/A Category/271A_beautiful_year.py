# 271A - Beautiful Year

year = int(input().strip()) + 1

while len(set(str(year))) != len(list(str(year))):
    year += 1

print(year)