# 688A - Opponents

first_line_input = input().strip().split()
n = int(first_line_input[0])
d = int(first_line_input[1])

opponents = []

for _ in range(d):
    opponents.append(input().strip())

max_consecutive_days = 0

for i in range(1, len(opponents) + 1):
    for j in range(len(opponents)):
        segment = opponents[j : j + i]

        if len(segment) != i:
            continue

        is_every_day_arya_can_beat_her_opponent = True

        for k in range(len(segment)):
            if ''.join(list(set(segment[k]))) == '1':
                is_every_day_arya_can_beat_her_opponent = False
                break
            
        if is_every_day_arya_can_beat_her_opponent:
            max_consecutive_days = len(segment)
        
print(max_consecutive_days)