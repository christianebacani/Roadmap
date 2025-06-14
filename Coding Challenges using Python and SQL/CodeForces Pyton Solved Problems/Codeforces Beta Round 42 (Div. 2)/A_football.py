# 43A - Football

n = int(input().strip())
goal_logs = []

for _ in range(n):
    goal_logs.append(input().strip())

distinct_goal_logs = list(set(goal_logs))
team_and_number_of_goals = {}

for i in range(len(distinct_goal_logs)):
    team_and_number_of_goals[distinct_goal_logs[i]] = goal_logs.count(distinct_goal_logs[i])

maximum_goals = max(list(team_and_number_of_goals.values()))

for team, number_of_goals in team_and_number_of_goals.items():
    if maximum_goals == number_of_goals:
        print(team)