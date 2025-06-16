# 1283A - Minutes Before the New Year

t = int(input().strip())

for _ in range(t):
    user_input = input().strip().split()
    h = int(user_input[0])
    m = int(user_input[1])

    remaining_hours = 23 - h
    remaining_minutes = 60 - m

    total_minutes_before_new_year = (remaining_hours * 60) + remaining_minutes

    print(total_minutes_before_new_year)