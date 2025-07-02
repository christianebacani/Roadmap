# 540A - Combination Lock

def forward_move(digit: int, target_digit: int) -> int:
    total = 0

    while digit != target_digit:
        if digit == 9:
            digit = 0
            total += 1

        else:
            digit += 1
            total += 1
    
    return total

def backward_move(digit: int, target_digit: int) -> int:
    total = 0
    
    while digit != target_digit:
        if digit == 0:
            digit = 9
            total +=1
        
        else:
            digit -= 1
            total += 1
    
    return total

n = int(input().strip())
original_state_of_disk = input().strip()
target_state_of_disk = input().strip()
answer = 0

for i in range(len(original_state_of_disk)):
    total_forward_move = forward_move(int(original_state_of_disk[i]), int(target_state_of_disk[i]))
    total_backward_move = backward_move(int(original_state_of_disk[i]), int(target_state_of_disk[i]))
    
    if total_forward_move <= total_backward_move:
        answer += total_forward_move
    
    else:
        answer += total_backward_move
    
print(answer)