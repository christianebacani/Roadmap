# 703A - Mishka and Game

n = input().strip()
dice_values = []

for _ in range(int(n)):
    dice_value = input().strip().split()
    dice_value = [int(value) for value in dice_value]
    dice_values.append(dice_value)

mishka_score = 0
chris_score = 0

for i in range(len(dice_values)):
    if dice_values[i][0] > dice_values[i][1]:
        mishka_score += 1
    
    elif dice_values[i][0] < dice_values[i][1]:
        chris_score += 1
    
    else:
        pass

if mishka_score == chris_score:
    print('Friendship is magic!^^')

elif mishka_score > chris_score:
    print('Mishka')

else:
    print('Chris')