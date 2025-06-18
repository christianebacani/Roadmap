# 1996A - Legs

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    total_animals = 0

    while n >= 4 or n >= 2:
        if n >= 4:
            n -= 4
            total_animals += 1
        
        elif n >= 2:
            n -= 2
            total_animals += 1
        
        else:
            pass
    
    print(total_animals)