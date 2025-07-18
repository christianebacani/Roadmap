# 1092B - Teams Forming

n = int(input().strip())
a = input().strip().split()
a = [int(num) for num in a]

a.sort()
teams = []

for i in range(0, len(a), 2):
    team = a[i : i + 2]
    teams.append(team)

minimum_problems_to_solve = 0

for i in range(len(teams)):
    minimum_problems_to_solve += (abs(teams[i][0] - teams[i][1]))

answer = minimum_problems_to_solve
print(answer)