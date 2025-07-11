# 988A - Diverse Team

first_line = input().strip().split()
n = int(first_line[0])
k = int(first_line[1])
a = input().strip().split()
a = [int(num) for num in a]

members_with_distinct_ratings = []
answer = []

for i in range(len(a)):
    if a[i] not in members_with_distinct_ratings:
        members_with_distinct_ratings.append(a[i])
        answer.append(i + 1)

team = answer[:k]

if len(team) == k:
    team = ' '.join([str(num) for num in team])
    print('YES')
    print(team)

else:
    print('NO')