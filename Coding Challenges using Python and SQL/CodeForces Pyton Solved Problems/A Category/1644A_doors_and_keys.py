# 1644A - Doors and Keys

t = int(input().strip())

for _ in range(t):
    characters = input().strip()
    available_keys = []

    the_knight_can_open_all_the_doors = True

    for i in range(len(characters)):
        if characters[i].islower():
            available_keys.append(characters[i])
            continue
        
        the_knight_can_open_the_current_door = False

        for j in range(len(available_keys)):
            if str(available_keys[j]).upper() == characters[i]:
                the_knight_can_open_the_current_door = True
                break
        
        if not the_knight_can_open_the_current_door:
            the_knight_can_open_all_the_doors = False
            break
    
    if the_knight_can_open_all_the_doors:
        print('YES')
    
    else:
        print('NO')