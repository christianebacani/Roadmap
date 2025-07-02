# 1709A - Three Doors

number_of_test_cases = int(input().strip())

for _ in range(number_of_test_cases):
    key_in_my_hand = int(input().strip())
    key_behind_each_doors = input().strip().split()
    key_behind_each_doors = [int(num) for num in key_behind_each_doors]

    collected_keys = [key_in_my_hand]
    current_key = key_in_my_hand

    while True:
        the_door_is_empty = False

        for i in range(len(key_behind_each_doors)):
            if current_key != (i + 1):
                continue
            
            if key_behind_each_doors[i] == 0:
                the_door_is_empty = True
                break

            current_key = key_behind_each_doors[i]
            key_behind_each_doors[i] = 0
            collected_keys.append(current_key)
        
        if the_door_is_empty:
            break
    
    if len(collected_keys) == 3:
        print('YES')
    
    else:
        print('NO')