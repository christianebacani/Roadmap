# 378A - Playing with Dice

first_line = input().strip().split()
a = int(first_line[0])
b = int(first_line[1])

player_one_win = 0
draw = 0
player_two_win = 0

for i in range(1, 6 + 1):
    if abs(i - a) < abs(i - b):
        player_one_win += 1
    
    elif abs(i - a) > abs(i - b):
        player_two_win += 1
    
    else:
        draw += 1

answer = f'{player_one_win} {draw} {player_two_win}'
print(answer)