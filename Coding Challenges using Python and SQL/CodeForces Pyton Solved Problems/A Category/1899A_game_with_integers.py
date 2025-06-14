# 1899A - Game with Integers

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    
    vasya_won = False
    vasya_move = 0
    vova_won = False
    vova_move = 0

    while True:
        vasya_move += 1
        vova_move += 1

        if vasya_move == 10 and vasya_won is False:
            vova_won = True
            break
        
        else:
            pass
        
        if (n - 1) % 3 == 0 or (n + 1) % 3 == 0:
            vasya_won = True
            break
        
        if (n - 1) % 3 == 0 or (n + 1) % 3 == 0:
            vova_won = True
            break
        
        else:
            pass
    
    if vasya_won:
        print('First')
        continue

    if vova_won:
        print('Second')