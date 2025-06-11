# 155A - I_love_%username%

n = input().strip()
points = input().strip().split()
points = [int(num) for num in points]
amazing_performances = 0

for i in range(len(points)):
    if i == 0:
        continue

    greater_than_the_past_competition_points = 0
    less_than_the_past_competition_points = 0

    past_competitions = points[:i]

    for j in range(len(past_competitions)):
        if points[i] > past_competitions[j]:
            greater_than_the_past_competition_points += 1
        
        elif points[i] < past_competitions[j]:
            less_than_the_past_competition_points += 1
        
        continue

    if greater_than_the_past_competition_points == len(past_competitions) or less_than_the_past_competition_points == len(past_competitions):
        amazing_performances += 1

print(amazing_performances)