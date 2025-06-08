# A - False Alarm

number_of_test_cases = int(input().strip())

for _ in range(number_of_test_cases):
    user_input = input().strip().split()
    seconds = int(user_input[1])
    
    doors = input().strip().split()
    yousef_can_reach_the_exit = False
    door = []

    for i in range(len(doors)):
        if doors[i] == '0':
            continue
        
        index = i + seconds
        door = doors[index:]
        break

    if '1' not in door:
        print('YES')
    
    else:
        print('NO')