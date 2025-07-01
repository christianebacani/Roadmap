# 2091A - Olympiad Date

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    numbers = input().strip().split()
    numbers = [int(num) for num in numbers]

    numbers_pulled = []
    the_date_was_accomplished = False

    for i in range(len(numbers)):
        numbers_pulled.append(numbers[i])

        if numbers_pulled.count(0) < 3:
            continue

        if numbers_pulled.count(1) < 1:
            continue

        if numbers_pulled.count(3) < 1:
            continue

        if numbers_pulled.count(2) < 2:
            continue
        
        if numbers_pulled.count(5) < 1:
            continue
        
        the_date_was_accomplished = True
        break

    if the_date_was_accomplished:
        print(len(numbers_pulled))
    
    else:
        print(0)